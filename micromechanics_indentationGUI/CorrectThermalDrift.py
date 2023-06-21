""" Module to calibrate the thermal drift """
import numpy as np
from scipy import signal, ndimage
from scipy.ndimage import gaussian_filter1d

def identifyDrift(indentation):
  """
  identify the segment of thermal drift collection before the complete unloading

  Args:
    indentation (class): defined in micromechanics

  Returns:
    bool: success of identifying the load-hold-unload
  """
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
  rate /= np.max(rate)
  loadMask  = np.logical_and(rate >  indentation.model['relForceRateNoise'], p>indentation.model['forceNoise'])
  unloadMask= np.logical_and(rate < -indentation.model['relForceRateNoise'], p>indentation.model['forceNoise'])
  #try to clean small fluctuations
  if len(loadMask)>100 and len(unloadMask)>100:
    #size = indentation.model['maxSizeFluctuations']
    size = 1
    loadMaskTry = ndimage.binary_closing(loadMask, structure=np.ones((size,)) )
    unloadMaskTry = ndimage.binary_closing(unloadMask, structure=np.ones((size,)))
    loadMaskTry = ndimage.binary_opening(loadMaskTry, structure=np.ones((size,)))
    unloadMaskTry = ndimage.binary_opening(unloadMaskTry, structure=np.ones((size,)))
  if np.any(loadMaskTry) and np.any(unloadMaskTry):
    loadMask = loadMaskTry
    unloadMask = unloadMaskTry
  #find index where masks are changing from true-false
  loadMask  = np.r_[False,loadMask,False] #pad with false on both sides
  unloadMask= np.r_[False,unloadMask,False]
  unloadIdx = np.flatnonzero(unloadMask[1:] != unloadMask[:-1])
  #drift segments: only add if it makes sense
  try:
    if rate[-1]<-indentation.model['relForceRateNoise']:
      iDriftS = unloadIdx[-3]-1
      iDriftE = unloadIdx[-2]-1
    elif p[-1]<p.max()*0.1:
      iDriftS = unloadIdx[-3]-1
      iDriftE = unloadIdx[-2]-1
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
  return True

def correctThermalDrift(indentation,ax=False,reFindSurface=False):
  """
  calculate and correct the thermal (displacement) drift

  Args:
    indentation (class): defined in micromechanics
    ax (class):  the ax of matplotlib
    reFindSurface (bool): whether to perform the search surface again
  Returns:
    Drift (float): the calculated thermal drift
  """
  #calculate thermal drift
  identifyDrift(indentation)
  Drift_Start=indentation.iDrift[0]
  Drift_End=indentation.iDrift[1]
  #using thermal drift data from the 30s of collection
  Drift_Start_from30s = np.where( indentation.t < indentation.t[Drift_Start] +30 )[0][-1]
  if Drift_Start == Drift_End:
    Drift = 0
  else:
    popt = np.polyfit(indentation.t[Drift_Start_from30s:Drift_End], indentation.h[Drift_Start_from30s:Drift_End], 1)
    Drift = popt[0]
    if ax:
      ax.plot(indentation.t[Drift_Start:Drift_End],indentation.h[Drift_Start:Drift_End]*1000,'.', label='within the first 30 s')
      ax.plot(indentation.t[Drift_Start_from30s:Drift_End],indentation.h[Drift_Start_from30s:Drift_End]*1000, '.', color='tab:orange', label = 'after 30 s')
      func_y_new = np.poly1d(popt)
      x_new = np.arange(indentation.t[Drift_Start], indentation.t[Drift_End],0.1)
      y_new = func_y_new(x_new)
      ax.plot(x_new,y_new*1000,'tab:green', label=f"slope of this is the determined thermal drift: {Drift*1000:.3E} nm/s")
      ax.set_xlabel('time [s]')
      ax.set_ylabel('depth [nm]')
  # calibrate thermal Drift
  indentation.h -= Drift*indentation.t
  if reFindSurface:
    #newly find surface
    indentation.model['driftRate'] = False
    indentation.nextTest(newTest=False)
  return Drift
