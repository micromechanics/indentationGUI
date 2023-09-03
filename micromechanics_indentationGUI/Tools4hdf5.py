""" Module for tools for hdf5 """
import pandas as pd

def convertXLSXtoHDF5(XLSX_File,progressbar=None):
  """
  using pandas to convert xlsx-file to hdf5-file

  Args:
    XLSX_File (string): the full file path of the xlsx-file
    progressbar (def) : to describe the percent of progress
  """
  df = pd.ExcelFile(XLSX_File)
  store = pd.HDFStore(f"{XLSX_File[:-5]}.h5", mode='w', complevel=9, complib='zlib')
  print (df.sheet_names)
  for idx, sheet_name in enumerate(df.sheet_names):
    data = df.parse(sheet_name)
    for i, _ in enumerate(data.columns):
      if i==0:
        if data.columns[i] == 'Markers':
          data.iloc[:,i]=data.iloc[:,i].astype(str)
        else:
          data.iloc[:,i] = pd.to_numeric(data.iloc[:,i], errors='coerce')
      elif i>0:
        data.iloc[:,i] = pd.to_numeric(data.iloc[:,i], errors='coerce')
    try:
      store.put(sheet_name, data, format='table', append=True)
    except:
      store.put(sheet_name, data, format='fixed')
      print('fixed', sheet_name)
    if progressbar is not None:
      progressbar(idx/len(df.sheet_names)*100, 'convert')
  print (store.keys())
  store.close()
