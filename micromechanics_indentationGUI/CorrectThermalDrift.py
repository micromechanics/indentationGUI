""" Module to calibrate the thermal drift """
import copy
import numpy as np
from scipy import signal, ndimage
from scipy.ndimage import gaussian_filter1d, binary_closing, binary_opening
from scipy.optimize import fsolve, root_scalar
from micromechanics.indentation.definitions import Method

def robust_outlier_mask(S, win1, k=4.0, eps=None): #pylint:disable=missing-param-doc
  """
  Detect local outliers using a rolling median and MAD-based threshold.

  Parameters
  ----------
  S : array-like
    Input signal or data series in which outliers are detected.

  win1 : int
    Window size of the rolling median filter used to estimate
    the local baseline and the median absolute deviation (MAD).

  k : float, optional
    Threshold multiplier for the robust deviation. A point is
    classified as an outlier if |S - median| > k * sigma_robust.
    Default is 4.0.

  eps : float or None, optional
    Small floor added to the robust scale estimate to avoid
    division by zero when the signal is locally constant.
    If None, it is estimated from the signal magnitude.

  Returns
  -------
  outlier : boolean array
    Mask of detected outliers.
  med : ndarray
    Local median baseline.
  """
  S = np.asarray(S, float)
  # Small floor added to the scale estimate to avoid division by zero
  # when the signal is locally constant (noise floor).
  if eps is None:
    eps = 1e-6 * np.median(np.abs(S))  # Noise Floor (Recommended)
  # Local median (robust estimate of the signal baseline).
  med = ndimage.median_filter(S, size=win1, mode="reflect")
  # Absolute deviation from the local median.
  abs_dev = np.abs(S - med)
  # Local MAD (median absolute deviation), a robust scale estimator.
  mad = ndimage.median_filter(abs_dev, size=win1, mode="reflect")
  # Convert MAD to a Gaussian-equivalent standard deviation.
  sigma_robust = 1.4826 * mad + eps
  # Mark points whose deviation exceeds k × robust sigma.
  outlier = abs_dev > (k * sigma_robust)
  return outlier, med

def replace_by_median(S, outlier, med): #pylint:disable=missing-param-doc
  """
  Replace detected outliers with the local median value.

  Parameters
  ----------
  S : array-like
    Original signal or data series.

  outlier : array-like of bool
    Boolean mask indicating which elements of `S` are considered outliers.

  med : array-like
    Local median values (e.g., from a rolling median filter) used
    to replace the outliers.

  Returns
  -------
  S2 : ndarray
    Signal with outliers replaced by the corresponding median values.
  """
  S2 = S.copy()
  S2[outlier] = med[outlier]
  return S2

def interpolate_segments(t, S, mask):
  """Interpolate each contiguous segment where mask=True as a whole"""
  S2 = S.copy()
  good = ~mask
  if good.sum() < 2:
    return S2
  S2[mask] = np.interp(t[mask], t[good], S[good])
  return S2

def denoise_hold_S_scipy(t, S, dt=None, w1_s=15.0, k=4.0, iters=2, #pylint:disable=missing-param-doc
                         segment_interp=True, w2_s=2.0, polyorder=1):
  """
  Denoise a time-series signal by detecting and replacing outliers,
  optionally interpolating anomaly segments, and applying light
  Savitzky–Golay smoothing.

  Parameters
  ----------
  t : array-like
    Time vector corresponding to the signal samples.
    Must be monotonically increasing.

  S : array-like
    Signal values to be denoised.

  dt : float, optional
    Sampling interval. If None, it is estimated from the median
    difference of the time vector `t`.

  w1_s : float, default=15.0
    Time window (in seconds) used for robust outlier detection.

  k : float, default=4.0
    Threshold factor controlling sensitivity of the outlier detection.
    Larger values detect fewer outliers.

  iters : int, default=2
    Number of iterations for the outlier detection and replacement
    process. Multiple iterations help remove clustered spikes.

  segment_interp : bool, default=True
    If True, contiguous segments of detected anomalies are
    interpolated as a whole instead of replacing individual points.

  w2_s : float, default=2.0
    Time window (in seconds) used for Savitzky–Golay smoothing.

  polyorder : int, default=1
    Polynomial order used in the Savitzky–Golay filter.

  Returns
  -------
  S_work : ndarray
    Cleaned signal after outlier removal and optional interpolation.

  S_smooth : ndarray
    Smoothed version of the cleaned signal obtained using a
    Savitzky–Golay filter.

  mask_total : ndarray of bool
    Boolean mask indicating positions where outliers were detected.

  (win1, win2) : tuple of int
    Window sizes (in samples) used for outlier detection and smoothing.
  """
  t = np.asarray(t)
  S = np.asarray(S, float)
  if dt is None:
    dt = np.median(np.diff(t))

  win1 = max(5, int(round(w1_s/dt)))
  if win1 % 2 == 0: win1 += 1

  win2 = max(polyorder + 3, int(round(w2_s/dt)))
  if win2 % 2 == 0: win2 += 1

  S_work = S.copy()
  mask_total = np.zeros_like(S_work, dtype=bool)

  # Iterative cleanup (more effective for clustered spikes)
  for _ in range(iters):
    outlier, med = robust_outlier_mask(S_work, win1, k=k)
    mask_total |= outlier
    S_work = replace_by_median(S_work, outlier, med)

  # Interpolate contiguous anomaly segments as a whole (optional)
  if segment_interp and mask_total.any():
    S_work = interpolate_segments(t, S_work, mask_total)

  # Light smoothing (Savgol preserves shape)
  S_smooth = signal.savgol_filter(S_work, window_length=win2,
                                  polyorder=polyorder, mode="interp")
  return S_work, S_smooth, mask_total, (win1, win2)

def correctThermalDrift_assumingConstantE(indentation,ax=[False,False,False],correctDrift=1, #pylint:disable=missing-param-doc,inconsistent-return-statements
                                          already_removed_frameCompliance=True,progressbar=None):
  """
  Estimate drift-corrected depth during the hold segment assuming a constant reduced modulus.

  Parameters
  ----------
  indentation : IndentationTest
    Object containing CSM indentation data (time, load, depth, stiffness, etc.).

  ax : list of matplotlib.axes.Axes or False, optional
    Axes used for plotting intermediate results:
    ax[0] – load vs time
    ax[1] – reconstructed depth
    ax[2] – hardness evolution
    Set element to False to disable the corresponding plot.

  correctDrift : int, optional
    Flag controlling whether thermal drift correction is applied.

  already_removed_frameCompliance : bool, optional
    If False, frame compliance will be removed before processing.

  progressbar : Qt progress bar or similar, optional
    Progress indicator updated during the root-solving loops.

  Returns
  -------
  t : ndarray
    Time values of the hold segment.

  p : ndarray
    Load values during the hold segment.

  h_smooth_solutions : ndarray
    Reconstructed indentation depth assuming constant modulus
    using denoised dynamic stiffness.

  slope_smooth : ndarray
    Denoised dynamic stiffness during the hold segment.
  """
  # This routine is only valid for CSM data.
  if indentation.method != Method.CSM:
    print('**ERROR: this function is used for CSM')
    return
  # Residual equation used to recover contact depth hc from target contact area Ac:
  # areaFunction(hc) - Ac = 0
  def equation(hc, Ac):
    hc_arr = np.atleast_1d(hc).astype(float)
    return indentation.tip.areaFunction(hc_arr) - Ac
  # Load data.
  slope = indentation.Fullslope
  t = indentation.t
  p = indentation.p
  h = indentation.h
  # Optionally remove frame compliance from displacement and stiffness.
  if not already_removed_frameCompliance:
    h -= indentation.tip.compliance*p
    slope = 1./(1./slope - indentation.tip.compliance)
  # Optional plot: load vs time.
  if ax[0]:
    ax[0].scatter(t, p, s=1, label=f"{indentation.testName}", picker=True,
                  color='black')
  # Window size used later to trim edge artifacts from smoothing.
  win = 51
  # Restrict analysis to the holding segment.
  index_holding = np.arange(indentation.iLHU[0][1],indentation.iLHU[0][2])
  t = t[index_holding]
  slope = slope[index_holding]
  # Denoise continuous dynamic stiffness during hold.
  _,slope_smooth,_,_ = denoise_hold_S_scipy(t=t, S=slope, dt=None, w1_s=10, k=4.0, iters=10,
                         segment_interp=True, w2_s=2.0, polyorder=1)
  # Trim both ends to remove smoothing boundary effects.
  p = p[index_holding][int(win):-int(win)]
  h = h[index_holding][int(win):-int(win)]
  t = t[int(win):-int(win)]
  slope = slope[int(win):-int(win)]
  slope_smooth = slope_smooth[int(win):-int(win)]
  # Target reduced modulus assumed constant during the hold segment.
  modulusRedGoal = indentation.model['modulusRedGoal']
  # Plot original depth vs time if requested.
  if ax[1]:
    ax[1].scatter(t, h*1000, s=1, picker=True,
                  color='gray', label=f"original data-{indentation.testName}",)
  # Compute projected contact area from stiffness using Oliver & Pharr / Oliver 2004 Eq. (26).
  Ac_list = np.array( np.power( slope  / (2.0*modulusRedGoal/np.sqrt(np.pi))  ,2))
  Ac_smooth_list = np.array( np.power( slope_smooth  / (2.0*modulusRedGoal/np.sqrt(np.pi))  ,2))
  # Compute hardness from load divided by projected contact area.
  hardness_ = p/Ac_list
  hardness_smooth = p/Ac_smooth_list
  # Solve for contact depth hc from the area function for raw stiffness-derived area.
  hc_solutions = np.empty(len(Ac_list), dtype=float)
  hc0 = np.sqrt(Ac_list[0] / 24.5)
  for k, Ac in enumerate(Ac_list):
    if progressbar is not None:
      progressbar.setValue(k/len(Ac_list)*50)
    x0 = hc0
    x1 = hc0 * 1.001 + 1e-12
    sol = root_scalar(
      lambda hc: equation(hc, Ac), #pylint: disable=cell-var-from-loop
      x0=x0, x1=x1,
      method="secant",
      xtol=1e-8,
      maxiter=30
      )
    hc = sol.root
    hc_solutions[k] = hc
    hc0 = hc
  # Reconstruct total indentation depth from contact depth:
  # h = hc + epsilon * P/S, with epsilon = 0.75
  h_solutions = hc_solutions + 0.75 * p / slope
  # Repeat the same analyse processing using denoised stiffness.
  hc_smooth_solutions = np.empty(len(Ac_smooth_list), dtype=float)
  hc0 = np.sqrt(Ac_smooth_list[0] / 24.5)
  for k, Ac_smooth in enumerate(Ac_smooth_list):
    if progressbar is not None:
      progressbar.setValue(k/len(Ac_smooth_list)*50 + 50)
    x0 = hc0
    x1 = hc0 * 1.001 + 1e-12
    sol = root_scalar(
      lambda hc: equation(hc, Ac_smooth), #pylint: disable=cell-var-from-loop
      x0=x0, x1=x1,
      method="secant",
      xtol=1e-8,
      maxiter=30
      )
    hc_smooth = sol.root
    hc_smooth_solutions[k] = hc_smooth
    hc0 = hc_smooth
  # Reconstruct depth from denoised contact stiffness.
  h_smooth_solutions = hc_smooth_solutions + 0.75 * p / slope_smooth
  # Plot reconstructed depths.
  if ax[1]:
    ax[1].scatter(t, h_solutions*1000,
                  s=5, label="assuming constant E", picker=True,
                  color='tab:green', alpha = 0.8, zorder=4)
    ax[1].scatter(t, h_smooth_solutions*1000,
                  s=2, label="assuming constant E\n+ denoised cont. dyn. stiffness", picker=True,
                  color='blue', alpha = 0.8, zorder=5)
  # Plot hardness evolution.
  if ax[2]:
    ax[2].scatter(t, hardness_,
                  s=5, label="assuming constant E - original", picker=True,
                  color='tab:green', alpha = 0.8, zorder=2)
    ax[2].scatter(t, hardness_smooth,
                  s=2, label="assuming constant E\n+ denoised cont. dyn. stiffness", picker=True,
                  color='blue', alpha = 0.8, zorder=3)
  # Return processed hold-segment data using the denoised stiffness solution.
  return t, p, h_smooth_solutions, slope_smooth

def correctThermalDrift_useFunction(indentation,ax=[False,False,False],correctDrift=3):
  """
  Correct thermal drift in multi-cycle indentation data using a fitted drift function.

  This function estimates and removes time-dependent thermal drift from displacement
  data in a multi loading–unloading indentation experiment. Drift is determined from
  pre-indent, post-indent, and intermediate unloading segments, then modeled as a
  continuous function over time and integrated to correct the displacement signal.

  Parameters
  ----------
  indentation : object
    Indentation data object containing time (`t`), displacement (`h`), load (`p`),
    unloading indices (`iLHU`), and model parameters. Must use MULTI method.
  ax : list of matplotlib.axes.Axes or bool, optional
    Axes for optional plotting:
    - ax[0]: load vs time
    - ax[1]: displacement (original and corrected)
    - ax[2]: drift rate vs time
    Use False to disable plotting. Default is [False, False, False].
  correctDrift : int, optional
    Drift correction mode passed to `correctThermalDrift`. Default is 3.

  Notes
  -----
  - Only applicable to MULTI indentation method.
  - Drift is computed from multiple segments and interpolated over time.
  - Displacement is corrected by integrating the drift rate function.
  """
  if indentation.method != Method.MULTI:
    print('**ERROR: this function is used for multi loading-unloading')
    return
  def equation(hc, Ac):
    return i.tip.areaFunction(hc) - Ac
  i = indentation
  i.analyse(calculate_HE=False)
  modulusRedGoal = i.model['modulusRedGoal']
  indexU = [row[2] for row in i.iLHU]
  if ax[0]:
    print('i.t, i.p',i.t, i.p)
    ax[0].scatter(i.t, i.p, s=1, label=f"{i.testName}", picker=True, color='black')
  if ax[1]:
    ax[1].scatter(i.t, i.h*1000, s=1, picker=True, color='gray', label='original data')
    # ax[1].scatter(i.t[indexU], i.h[indexU]*1000, s=50, label=f"exp.", picker=True, color='orange',zorder=3)
  Ac_list = np.array( np.power( i.slope  / (2.0*modulusRedGoal/np.sqrt(np.pi))  ,2))  #Eq.(26) Oliver 2004
  hc_solutions=[]
  for Ac in Ac_list:
    hc_solution = fsolve(equation, 0.5, args=(Ac,))[0]
    hc_solutions.append(hc_solution)
  hc_solutions = np.asarray(hc_solutions)
  h_solutions = hc_solutions + 0.75*np.asarray(i.p[[row[2] for row in i.iLHU]])/i.slope
  # h_difference = i.h[indexU] - h_solutions
  # Dfrit_ = (h_difference [1:] - h_difference[:-1])/(i.t[indexU][1:]-i.t[indexU][:-1])
  _,Drift_pre,Drift_post = correctThermalDrift(indentation=i,
                                                reFindSurface=False,
                                                correctDrift=correctDrift,
                                                OnlyReturnTheValues=True,
                                                ) #calibrate the thermal drift using the collection during the unloading
  Drift_pre_Start_used = int(i.iPreDrift[0] + (i.iPreDrift[1]-i.iPreDrift[0]) * (1-i.model['Range_PreDrift']/100.))
  t_middle_at_pre = np.asarray([(i.t[i.iPreDrift[1]]-i.t[Drift_pre_Start_used])/2.+i.t[Drift_pre_Start_used]])
  t_middle_at_post = np.asarray([(i.t[i.iDrift[1]]-i.t[i.iDrift[0]])/2.+i.t[i.iDrift[0]]])
  # t_middle_betweenUnloading = i.t[indexU][:-1] + (i.t[indexU][1:] - i.t[indexU][:-1])/2.
  time_AllDrift = t_middle_at_pre
  AllDrift = Drift_pre
  for j, indexLHU in enumerate(i.iLHU):
    try:
      indexNL =  i.iLHU[j+1][0]
    except:
      pass
    else:
      indexH = indexLHU[3]
      indexH_used = indexH + int((indexNL-indexH)*0.1)
      time_ = i.t[indexH_used] + 0.5 * (i.t[indexNL]-i.t[indexH_used])
      popt = np.polyfit(i.t[indexH_used:indexNL], i.h[indexH_used:indexNL], 1)
      Drift_ = popt[0]
      time_AllDrift = np.hstack((time_AllDrift, time_))
      AllDrift = np.r_[AllDrift, Drift_]
  time_AllDrift = np.hstack((time_AllDrift, t_middle_at_post))
  AllDrift = np.r_[AllDrift, Drift_post]
  # time_AllDrift = np.hstack((t_middle_at_pre, t_middle_betweenUnloading, t_middle_at_post))
  # AllDrift = np.r_[Drift_pre, Dfrit_, Drift_post]
  # time_AllDrift = np.hstack((t_middle_at_pre, t_middle_at_post))
  # AllDrift = np.r_[Drift_pre, Drift_post]
  coeffs = np.polyfit(time_AllDrift, AllDrift, 2)
  func_Drift_t = np.poly1d(coeffs)
  t = np.linspace(np.min(i.t), np.max(i.t), 1500)
  Drift_t = func_Drift_t(t)
  h0=0
  for j, time in enumerate(time_AllDrift[:-1]):
    time_segment = [time, time_AllDrift[j+1]]
    Drift_segment = [AllDrift[j], AllDrift[j+1]]
    coeffs = np.polyfit(time_segment, Drift_segment, 1)
    func_Drift_t = np.poly1d(coeffs)
    func_Drift_t_int = func_Drift_t.integ()
    mask = np.where( (i.t > time) & (i.t < time_AllDrift[j+1]) )
    i.h[mask] = i.h[mask] - func_Drift_t_int(i.t[mask]) + func_Drift_t_int(time_AllDrift[j]) + h0
    h0 = h0 - func_Drift_t_int(time_AllDrift[j+1]) + func_Drift_t_int(time_AllDrift[j])
  i.h = i.h - i.h[i.model['Surface_index']]
  if ax[1]:
    ax[1].scatter(i.t, i.h*1000, s=2, picker=True, facecolors='blue', edgecolors='none', alpha=0.7, label='drift corrected')
    ax[1].scatter(i.t[indexU], h_solutions*1000, s=30, label="assuming constant E", picker=True, color='tab:green',zorder=4)
  if ax[2]:
    ax[2].scatter(time_AllDrift,
                AllDrift*1000, # µm/s to nm/s for plotting
                s=30, label="measured dift rate", picker=True, color='tab:orange')
    ax[2].scatter(np.r_[t_middle_at_pre,t_middle_at_post],
                np.r_[Drift_pre,Drift_post]*1000, # µm/s to nm/s for plotting
                s=30, label="pre or post drift data", picker=True, color='tab:red', marker='^')
    ax[2].plot(t,Drift_t*1000) # µm/s to nm/s for plotting
    ax[2].set_ylim(*(np.array([np.min(np.r_[Drift_t,AllDrift]), np.max(np.r_[Drift_t,AllDrift])]) + np.array([-0.5, 0.5]) * np.ptp(np.r_[Drift_t,AllDrift]))*1000)
  return

def identify_PreDrift(indentation0):
  """
  identify the segment of thermal drift collection before the indentation
  (the first holding segment for more than 30 s)

  Args:
    indentation0 (class): defined in micromechanics

  Returns:
    bool: success of identifying the load-hold-unload
  """
  #create a local variable for indentation0
  indentation = copy.copy(indentation0)
  #identify point in time, which are too close (~0) to eachother
  gradTime = np.diff(indentation.t)
  maskTooClose = gradTime < np.percentile(gradTime,80)/1.e3
  indentation.t     = indentation.t[1:][~maskTooClose]
  indentation.p     = indentation.p[1:][~maskTooClose]
  indentation.h     = indentation.h[1:][~maskTooClose]
  indentation.valid = indentation.valid[1:][~maskTooClose]
  #use force-rate to identify load-hold-unload
  if indentation.model['relForceRateNoiseFilter']=='median':
    p = signal.medfilt(indentation.p, 5)
  else:
    p = gaussian_filter1d(indentation.p, 5)
  # Find boundaries where value changes
  change = np.r_[True, p[1:] != p[:-1], True]
  idx = np.flatnonzero(change)
  if idx[-1] > (len(change)-2):
    idx[-1] = idx[-1] - 1
  # Lengths of runs
  time_lengths = np.diff(indentation.t[idx])
  # Start and End index of the first holding for more than 30 s
  Start = idx[:-1][idx[np.where(time_lengths>30)][0]]
  End = idx[1:][idx[np.where(time_lengths>30)][0]]  # end index (exclusive)
  # pass the iPreDrift back to the global variable indentation0
  indentation0.iPreDrift=[Start,End]
  return True

def identifyDrift(indentation0):
  """
  identify the segment of thermal drift collection before the complete unloading

  Args:
    indentation0 (class): defined in micromechanics

  Returns:
    bool: success of identifying the load-hold-unload
  """
  #create a local variable for indentation0
  indentation = copy.copy(indentation0)
  #identify point in time, which are too close (~0) to eachother
  gradTime = np.diff(indentation.t)
  maskTooClose = gradTime < np.percentile(gradTime,80)/1.e3
  indentation.t     = indentation.t[1:][~maskTooClose]
  indentation.p     = indentation.p[1:][~maskTooClose]
  indentation.h     = indentation.h[1:][~maskTooClose]
  indentation.valid = indentation.valid[1:][~maskTooClose]
  #use force-rate to identify load-hold-unload
  if indentation.model['relForceRateNoiseFilter']=='median':
    p = signal.medfilt(indentation.p, 5)
  else:
    p = gaussian_filter1d(indentation.p, 5)
  rate = np.gradient(p, indentation.t)
  # rate /= np.max(rate)
  loadMask  = np.logical_and(rate >  indentation.model['relForceRateNoise'], p>indentation.model['forceNoise'])
  unloadMask= np.logical_and(rate < -indentation.model['relForceRateNoise'], p>indentation.model['forceNoise'])
  # try to clean small fluctuations
  if len(loadMask)>100 and len(unloadMask)>100:
    size = indentation.model['maxSizeFluctuations']
    # size = 1
    loadMaskTry = binary_closing(loadMask, structure=np.ones((size,)) )
    unloadMaskTry = binary_closing(unloadMask, structure=np.ones((size,)))
    loadMaskTry = binary_opening(loadMaskTry, structure=np.ones((size,)))
    unloadMaskTry = binary_opening(unloadMaskTry, structure=np.ones((size,)))
  if np.any(loadMaskTry) and np.any(unloadMaskTry):
    loadMask = loadMaskTry
    unloadMask = unloadMaskTry
  #find index where masks are changing from true-false
  loadMask  = np.r_[loadMask[0],loadMask] #pad with false on both sides
  unloadMask= np.r_[unloadMask,unloadMask[-1]]
  print('unloadMask',unloadMask)
  unloadIdx = np.flatnonzero(unloadMask[1:] != unloadMask[:-1])
  print('unloadIdx',unloadIdx)
  print('time', indentation.t[unloadIdx])
  #drift segments: only add if it makes sense
  try:
    if rate[-1]<-indentation.model['relForceRateNoise']:
      iDriftS = unloadIdx[-2]
      iDriftE = unloadIdx[-1]
    elif p[-1]<p.max()*0.15:
      iDriftS = unloadIdx[-3]
      iDriftE = unloadIdx[-2]
    else:
      iDriftS = unloadIdx[-1]-1
      iDriftE = -1
    if iDriftE < iDriftS:
      iDriftE = -1
    indentation.iDrift = [iDriftS,iDriftE]
  except:
    iDriftS = unloadIdx[-1]-1
    iDriftE = -1
    indentation.iDrift = [iDriftS,iDriftE]
  if np.absolute(indentation.p[indentation.iDrift[0]]-indentation.p[indentation.iDrift[1]])>0.05:
    if np.absolute(indentation.p[unloadIdx[-1]-1]-indentation.p[-1])<0.05:
      indentation.iDrift = [unloadIdx[-1]-1,-1]
    else:
      indentation.iDrift = [-1,-1]
  # pass the iDrift back to the global variable indentation0
  indentation0.iDrift=indentation.iDrift
  return True

def correctThermalDrift(indentation,ax=False,ax2=False,reFindSurface=False, correctDrift=1, OnlyReturnTheValues=False):
  """
  calculate and correct the thermal (displacement) drift

  Args:
    indentation (class): defined in micromechanics
    ax (class):  the ax of matplotlib for post indentation data
    ax2 (class):  the ax of matplotlib for pre indentation data
    reFindSurface (bool): whether to perform the search surface again
    correctDrift (int): which region (post, pre, post+pre) used for correction
    OnlyReturnTheValues (bool): if Ture, then will return the valus without correcting the depth
  Returns:
    Drift (float) [µm/s]: the calculated thermal drift
    Drift_pre (float) [µm/s]: the thermal drift calculated using the pre indentation data
    Drift_post (float) [µm/s]: the thermal drift calculated using the post indentation data
  """
  Drift = 0
  Drift_pre = 0
  Drift_post = 0
  if correctDrift in [1,3,4]:
    #calculate post thermal drift
    identifyDrift(indentation)
    print(indentation.iDrift)
    Drift_Start=indentation.iDrift[0]
    Drift_End=indentation.iDrift[1]
    #using thermal drift data from the 30s of collection
    # Drift_Start_from30s = np.where( indentation.t < indentation.t[Drift_Start] +30 )[0][-1]
    Drift_Start_used = int(Drift_Start + (Drift_End-Drift_Start) * (1-indentation.model['Range_PostDrift']/100.))
    if Drift_Start == Drift_End:
      Drift_post = 0
    else:
      popt = np.polyfit(indentation.t[Drift_Start_used:Drift_End],indentation.h[Drift_Start_used:Drift_End], 1)
      Drift_post = popt[0]
      if ax:
        ax.plot(indentation.t[Drift_Start:Drift_End],indentation.h[Drift_Start:Drift_End]*1000,'.', label='within the first 30 s')
        ax.plot(indentation.t[Drift_Start_used:Drift_End],indentation.h[Drift_Start_used:Drift_End]*1000, '.', color='tab:orange', label = 'after 30 s')
        func_y_new = np.poly1d(popt)
        x_new = np.arange(indentation.t[Drift_Start], indentation.t[Drift_End],0.1)
        y_new = func_y_new(x_new)
        ax.plot(x_new,y_new*1000,'tab:green', label=f"slope of this is the determined thermal drift: {Drift_post*1000:.3E} nm/s")
        ax.set_xlabel('time [s]')
        ax.set_ylabel('depth [nm]')
  if correctDrift in [2,3,4]:
    #calculate post thermal drift
    identify_PreDrift(indentation)
    Drift_Start=indentation.iPreDrift[0]
    Drift_End=indentation.iPreDrift[1]
    print('indentation.iPreDrift',indentation.iPreDrift)
    #using thermal drift data from the 30s of collection
    # Drift_Start_from30s = np.where( indentation.t < indentation.t[Drift_Start] +30 )[0][-1]
    Drift_Start_used = int(Drift_Start + (Drift_End-Drift_Start) * (1-indentation.model['Range_PreDrift']/100.))
    if Drift_Start == Drift_End:
      Drift_pre = 0
    else:
      popt = np.polyfit(indentation.t[Drift_Start_used:Drift_End], indentation.h[Drift_Start_used:Drift_End], 1)
      Drift_pre = popt[0]
      if ax2:
        ax2.plot(indentation.t[Drift_Start:Drift_End],indentation.h[Drift_Start:Drift_End]*1000,'.', label='within the first 30 s')
        ax2.plot(indentation.t[Drift_Start_used:Drift_End],indentation.h[Drift_Start_used:Drift_End]*1000, '.', color='tab:orange', label = 'after 30 s')
        func_y_new = np.poly1d(popt)
        x_new = np.arange(indentation.t[Drift_Start], indentation.t[Drift_End],0.1)
        y_new = func_y_new(x_new)
        ax2.plot(x_new,y_new*1000,'tab:green', label=f"slope of this is the determined thermal drift: {Drift_pre*1000:.3E} nm/s")
        ax2.set_xlabel('time [s]')
        ax2.set_ylabel('depth [nm]')
  if OnlyReturnTheValues:
    return Drift,Drift_pre,Drift_post
  if correctDrift == 4:
    correctThermalDrift_useFunction(indentation)
    return Drift,Drift_pre,Drift_post
  elif correctDrift == 3:
    Drift = (Drift_pre + Drift_post)/2.
  elif correctDrift == 1:
    Drift = Drift_post
  elif correctDrift == 2:
    Drift = Drift_pre
  indentation.h -= Drift*indentation.t
  if reFindSurface:
    #newly find surface
    indentation.model['driftRate'] = False
    indentation.nextTest(newTest=False)
  return Drift,Drift_pre,Drift_post
