""" Module for tools for hdf5 """
import warnings

import pandas as pd
from tables import NaturalNameWarning

def _normalize_excel_sheet_for_hdf5(data):
  """Convert Excel sheet columns to HDF5-friendly NumPy/object dtypes."""
  if data.empty and len(data.columns) == 0:
    return data
  normalized_columns = []
  for i, col_name in enumerate(data.columns):
    column = data.iloc[:, i]
    if i == 0 and col_name == 'Markers':
      column = column.map(lambda value: '' if pd.isna(value) else str(value)).astype(object)
    else:
      column = pd.Series(
        pd.to_numeric(column, errors='coerce').to_numpy(dtype='float64'),
        index=data.index,
      )
    normalized_columns.append(column)
  normalized_data = pd.DataFrame(
    {i: column.to_numpy() for i, column in enumerate(normalized_columns)},
    index=data.index,
  )
  normalized_data.columns = data.columns
  return normalized_data

def convertXLSXtoHDF5(XLSX_File,progressbar=None):
  """
  using pandas to convert xlsx-file to hdf5-file

  Args:
    XLSX_File (string): the full file path of the xlsx-file
    progressbar (def) : to describe the percent of progress
  """
  print('XLSX_File!!!!!!!!!!!!!!!',XLSX_File)
  df = pd.ExcelFile(XLSX_File)
  print (df.sheet_names)
  with pd.HDFStore(f"{XLSX_File[:-5]}.h5", mode='w', complevel=9, complib='zlib') as store:
    for idx, sheet_name in enumerate(df.sheet_names):
      data = df.parse(sheet_name)
      data = _normalize_excel_sheet_for_hdf5(data)
      with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=NaturalNameWarning)
        try:
          store.put(sheet_name, data, format='table', append=True)
        except:
          store.put(sheet_name, data, format='fixed')
          print('fixed', sheet_name)
      if progressbar is not None:
        progressbar(idx/len(df.sheet_names)*100, 'convert')
    print (store.keys())
