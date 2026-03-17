""" Module for tools for analysing in GUI """

import numpy as np

def split_mean_var_with_index(arr, n_segments): #pylint: disable=missing-param-doc
  """
  Split an array into segments and compute mean and variance for each.

  Parameters
  ----------
  arr : array-like
    Input data.
  n_segments : int
    Number of segments.

  Returns
  -------
  means : numpy.ndarray
    Mean of each segment.
  vars_ : numpy.ndarray
    Variance of each segment.
  indices : numpy.ndarray
    Segment boundary indices.
  """
  arr = np.asarray(arr)
  n = len(arr)
  indices = np.linspace(0, n, n_segments + 1, dtype=int)
  means = []
  vars_  = []
  for i in range(n_segments):
    seg = arr[indices[i]:indices[i+1]]
    means.append(seg.mean())
    vars_.append(seg.var())
  return np.array(means), np.array(vars_), indices
