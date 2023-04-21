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
    size = indentation.model['maxSizeFluctuations']
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
    iDriftS = unloadIdx[1::2][-2]+1
    iDriftE = unloadIdx[2::2][-1]-1
    indentation.iDrift = [iDriftS,iDriftE]
  except:
    indentation.iDrift = [-1,-1]
  if np.absolute(indentation.p[indentation.iDrift[0]]-indentation.p[indentation.iDrift[1]])>0.05:
    if np.absolute(indentation.p[unloadIdx[-1]]-indentation.p[-1])<0.05:
      indentation.iDrift = [unloadIdx[-1],-1]
    else:
      indentation.iDrift = [-1,-1]
  return True

def correctThermalDrift(indentation):
  """
  calibrate the thermal drift

  Args:
    indentation (class): defined in micromechanics

  Returns:
    bool: success of calibrating the thermal drift
  """
  #calculate thermal drift
  identifyDrift(indentation)
  Drift_Start=indentation.iDrift[0]
  Drift_End=indentation.iDrift[1]
  if Drift_Start == Drift_End:
    Drift = 0
  else:
    Drift = (indentation.h[Drift_Start]- indentation.h[Drift_End])/(indentation.t[Drift_Start]- indentation.t[Drift_End])
  #calibrate thermal Drift
  indentation.h -= Drift*indentation.t
  #newly find surface
  indentation.nextTest(newTest=False)
  return True
