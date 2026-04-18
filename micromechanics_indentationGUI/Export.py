#pylint: disable=possibly-used-before-assignment, used-before-assignment

""" Graphical user interface to export results """
import os
import warnings
import pandas as pd
from pandas import ExcelWriter, DataFrame
import numpy as np
from tables import NaturalNameWarning
from .Tools4LoadingData import read_file_list

def export(self, win):
  """
  Graphical user interface to export calculated hardness and young's modulus

  Args:
    win (class): MainWindow
  """
  Index_ExportTab = self.ui.comboBox_ExportTab.currentIndex()
  Index_ExportFormat = self.ui.comboBox_ExportFormat.currentIndex()
  Index_ExportFileType = self.ui.comboBox_ExportFileType.currentIndex()
  output_path = os.path.join(self.ui.lineEdit_ExportFolder.text(), self.ui.lineEdit_ExportFileName.text())
  writer = None
  if Index_ExportFileType == 0:
    try:
      writer = ExcelWriter(output_path, engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
    except Exception as e: #pylint:disable=broad-except
      suggestion = 'Close the opened Excel file.'
      win.show_error(str(e), suggestion)
      return
  #define the data frame of experimental parameters
  if Index_ExportTab == 0:
    #define the data frame of experimental parameters of tabHE
    df = DataFrame([
                    ['Tested Material'],
                    [win.ui.lineEdit_MaterialName_tabHE.text()],
                    [win.ui.lineEdit_path_tabHE.text()],
                    [win.ui.doubleSpinBox_Poisson_tabHE.value()],
                    ['Tip'],
                    [win.ui.lineEdit_TipName_tabHE.text()],
                    [win.ui.doubleSpinBox_E_Tip_tabHE.value()],
                    [win.ui.doubleSpinBox_Poisson_Tip_tabHE.value()],
                    [' '],
                    [win.ui.lineEdit_TAF1_tabHE.text()],
                    [win.ui.lineEdit_TAF2_tabHE.text()],
                    [win.ui.lineEdit_TAF3_tabHE.text()],
                    [win.ui.lineEdit_TAF4_tabHE.text()],
                    [win.ui.lineEdit_TAF5_tabHE.text()],
                    [' '],
                    [win.ui.lineEdit_FrameCompliance_tabHE.text()],
                    ['Unloading Range to Calculate Stiffness'],
                    [win.ui.doubleSpinBox_Start_Pmax_tabHE.value()],
                    [win.ui.doubleSpinBox_End_Pmax_tabHE.value()],
                    ['Range for calculating mean value'],
                    [win.ui.doubleSpinBox_minhc4mean_tabHE.value()],
                    [win.ui.doubleSpinBox_maxhc4mean_tabHE.value()],

                  ],
                  index=[
                          ' ',
                          'Name of Tested Material',
                          'Path',
                          'Poisson\'s Ratio',
                          ' ',
                          'Tip Name',
                          'Young\'s Modulus of Tip [GPa]',
                          'Poisson\'s Ratio of Tip [GPa]',
                          'Terms of Tip Area Function (TAF)',
                          'C0',
                          'C1',
                          'C2',
                          'C3',
                          'C4',
                          ' ',
                          'Frame Compliance [µm/mN]',
                          ' ',
                          'Start[100\% of Pmax]', #pylint: disable=anomalous-backslash-in-string
                          'End[100\% of Pmax]', #pylint: disable=anomalous-backslash-in-string
                          ' ',
                          'min. hc [µm]', #pylint: disable=anomalous-backslash-in-string
                          'max. hc [µm]', #pylint: disable=anomalous-backslash-in-string
                        ],
                    columns=[' '])
  elif Index_ExportTab == 1:
    #define the data frame of experimental parameters of tabPopIn
    df = DataFrame([
                    ['Tested Material'],
                    [win.ui.lineEdit_MaterialName_tabPopIn.text()],
                    [win.ui.lineEdit_path_tabPopIn.text()],
                    [win.ui.doubleSpinBox_Poisson_tabPopIn.value()],
                    ['Tip'],
                    [win.ui.lineEdit_TipName_tabPopIn.text()],
                    [win.ui.doubleSpinBox_E_Tip_tabPopIn.value()],
                    [win.ui.doubleSpinBox_Poisson_Tip_tabPopIn.value()],
                    [win.ui.doubleSpinBox_TipRadius_tabPopIn.value()],
                    [' '],
                    [win.ui.lineEdit_FrameCompliance_tabPopIn.text()],
                  ],
                  index=[
                          ' ',
                          'Name of Tested Material',
                          'Path',
                          'Poisson\'s Ratio',
                          ' ',
                          'Tip Name',
                          'Young\'s Modulus of Tip [GPa]',
                          'Poisson\'s Ratio of Tip [GPa]',
                          'Tip Radius [µm]',
                          ' ',
                          'Frame Compliance [µm/mN]',
                        ],
                    columns=[' '])
  elif Index_ExportTab == 2:
    #define the data frame of experimental parameters of tabClassification
    df = DataFrame([
                    [win.ui.textEdit_Files_tabClassification.toPlainText()],
                    ['Parameters'],
                    [win.ui.spinBox_NumberClusters_tabClassification.value()],
                    [win.ui.doubleSpinBox_WeightingRatio_tabClassification.value()],
                    [win.ui.comboBox_FlipMapping_tabClassification.currentIndex()],
                  ],
                  index=[
                          'Files',
                          ' ',
                          'Number of Clusters [-]',
                          'Weighting ratio, y/x [-]',
                          'Flip mapping (0=None, 1=Left-Right, 2=Top-Bottom, 3=Both)',
                        ],
                    columns=[' '])
  elif Index_ExportTab == 3:
    #define the data frame of experimental parameters of tabCreep
    file_list = read_file_list(win.ui.tableWidget_path_tabCreep)
    df = DataFrame([
                    [file_list[0] if file_list else ''],
                    [win.ui.doubleSpinBox_Poisson_tabCreep.value()],
                    [win.ui.doubleSpinBox_E_Tip_tabCreep.value()],
                    [win.ui.doubleSpinBox_Poisson_Tip_tabCreep.value()],
                    [win.ui.lineEdit_FrameCompliance_tabCreep.text()],
                    [win.ui.doubleSpinBox_DataSegment4Smooth_tabCreep.value()],
                  ],
                  index=[
                          'Path',
                          'Poisson\'s Ratio',
                          'Young\'s Modulus of Tip [GPa]',
                          'Poisson\'s Ratio of Tip',
                          'Frame Compliance [µm/mN]',
                          'Data Segment for Smoothing [s]',
                        ],
                    columns=[' '])

  if Index_ExportFileType == 1:
    _export_hdf5(output_path, Index_ExportTab, df, win)
    return

  #write to excel
  df.to_excel(writer,sheet_name='Experimental Parameters')
  #set the width of column
  writer.sheets['Experimental Parameters'].set_column(0, 1, 30)
  writer.sheets['Experimental Parameters'].set_column(0, 2, 60)
  if Index_ExportTab == 2:
    #set the height of column
    writer.sheets['Experimental Parameters'].set_row(1, 30)
  if Index_ExportFormat == 0:
    if Index_ExportTab == 0:
      #define the data frame of each tests for tabHE
      for j, _ in enumerate(win.tabHE_testName_collect):
        sheetName = win.tabHE_testName_collect[j]
        if win.tabHE_X_Position_collect[j] is None:
          win.tabHE_X_Position_collect[j]=0
          win.tabHE_Y_Position_collect[j]=0
        df = DataFrame(
                        [
                          win.tabHE_hc_collect[j],
                          win.tabHE_hmax_collect[j],
                          win.tabHE_Pmax_collect[j],
                          win.tabHE_H_collect[j],
                          win.tabHE_E_collect[j],
                          win.tabHE_Er_collect[j],
                          win.tabHE_X_Position_collect[j] * np.ones(len(win.tabHE_E_collect[j])),
                          win.tabHE_Y_Position_collect[j] * np.ones(len(win.tabHE_E_collect[j])),
                        ],
                        index =[
                                  'hc[µm]',
                                  'hmax[µm]',
                                  'Pmax[mN]',
                                  'H[GPa]',
                                  'E[GPa]',
                                  'Er[GPa]',
                                  'X Position [µm]',
                                  'Y Position [µm]',
                                ],
                        )
        df = df.T
        #write to excel
        df.to_excel(writer,sheet_name=sheetName, index=False)
        for k in range(10):
          #set the width of column
          writer.sheets[sheetName].set_column(0, k, 20)
    if Index_ExportTab == 1:
      #define the data frame of each tests for tabPopIn
      for j, _ in enumerate(win.tabPopIn_testName_collect):
        sheetName = win.tabPopIn_testName_collect[j]
        df = DataFrame(
                        [
                          win.tabPopIn_fPopIn_collect[j],
                          win.tabPopIn_prefactor_collect[j],
                          win.tabPopIn_E_collect[j],
                          win.tabPopIn_maxShearStress_collect[j],
                        ],
                        index =[
                                  'Pop-in Load [mN]',
                                  'fitted Hertzian prefactor[mN*µm^(-3/2)]',
                                  'calculated E [GPa]',
                                  'calculated max. shear stress [GPa]',
                                ],
                        )
        df = df.T
        #write to excel
        df.to_excel(writer,sheet_name=sheetName, index=False)
        for k in range(10):
          #set the width of column
          writer.sheets[sheetName].set_column(0, k, 20)
    if Index_ExportTab == 3:
      #define the data frame of each tests for tabCreep
      for j, _ in enumerate(win.tabCreep_testName_collect):
        sheetName = win.tabCreep_testName_collect[j]
        n = len(win.tabCreep_equivStress_collect[j])
        time_values = _tab_creep_time_values(win, j, n)
        df = DataFrame(
                        [
                          time_values,
                          win.tabCreep_equivStress_collect[j],
                          win.tabCreep_CreepRate_collect[j],
                        ],
                        index =[
                                  'time[s]',
                                  'equiv stress[GPa]',
                                  'creep rate[s-1]',
                                ],
                        )
        df = df.T
        #write to excel
        df.to_excel(writer,sheet_name=sheetName, index=False)
        for k in range(10):
          #set the width of column
          writer.sheets[sheetName].set_column(0, k, 20)
  elif Index_ExportFormat == 1:
    if Index_ExportTab == 0:
      #define the data frame of all tests for tabHE
      All_testName_collect = []
      All_hc_collect = []
      All_hmax_collect = []
      All_Pmax_collect = []
      All_Hmean_collect = []
      All_Hstd_collect = []
      All_Emean_collect = []
      All_Estd_collect = []
      All_Er_mean_collect = []
      All_Er_std_collect = []
      All_X_Position_collect=win.tabHE_X_Position_collect
      All_Y_Position_collect=win.tabHE_Y_Position_collect
      for j, _ in enumerate(win.tabHE_testName_collect):
        All_testName_collect.append(win.tabHE_testName_collect[j])
        All_hc_collect.append(win.tabHE_hc_collect[j][-1])
        All_hmax_collect.append(win.tabHE_hmax_collect[j])
        All_Pmax_collect.append(win.tabHE_Pmax_collect[j][-1])
        All_Hmean_collect.append(win.tabHE_Hmean_collect[j])
        All_Hstd_collect.append(win.tabHE_Hstd_collect[j])
        All_Emean_collect.append(win.tabHE_Emean_collect[j])
        All_Estd_collect.append(win.tabHE_Estd_collect[j])
        All_Er_mean_collect.append(win.tabHE_Er_mean_collect[j])
        All_Er_std_collect.append(win.tabHE_Er_std_collect[j])
      df = DataFrame(
                      [
                        All_testName_collect,
                        All_hc_collect,
                        All_hmax_collect,
                        All_Pmax_collect,
                        All_Hmean_collect,
                        All_Hstd_collect,
                        All_Emean_collect,
                        All_Estd_collect,
                        All_Er_mean_collect,
                        All_Er_std_collect,
                        All_X_Position_collect,
                        All_Y_Position_collect,
                      ],
                      index =[
                              'Test Name',
                              'max. hc [µm]',
                              'max. hmax [µm]',
                              'max. Pmax [mN]',
                              'mean of H [GPa]',
                              'std of H [GPa]',
                              'mean of E [GPa]',
                              'std of E [GPa]',
                              'mean of Er [GPa]',
                              'std of Er [GPa]',
                              'X Position [µm]',
                              'Y Position [µm]',
                              ],
                      )
    elif Index_ExportTab == 1:
      #define the data frame of all tests for tabPopIn
      All_testName_collect = []
      All_fPopIn_collect = []
      All_prefactor_collect = []
      All_E_collect = []
      All_maxShearStress_collect = []
      for j, _ in enumerate(win.tabPopIn_testName_collect):
        try:
          for k, _ in enumerate(win.tabPopIn_fPopIn_collect[j]):
            All_testName_collect.append(win.tabPopIn_testName_collect[j])
            All_fPopIn_collect.append(win.tabPopIn_fPopIn_collect[j][k])
            All_prefactor_collect.append(win.tabPopIn_prefactor_collect[j][k])
            All_E_collect.append(win.tabPopIn_E_collect[j][k])
            All_maxShearStress_collect.append(win.tabPopIn_maxShearStress_collect[j][k])
        except (TypeError, IndexError):
          All_testName_collect.append(win.tabPopIn_testName_collect[j])
          All_fPopIn_collect.append(win.tabPopIn_fPopIn_collect[j])
          All_prefactor_collect.append(win.tabPopIn_prefactor_collect[j])
          All_E_collect.append(win.tabPopIn_E_collect[j])
          All_maxShearStress_collect.append(win.tabPopIn_maxShearStress_collect[j])

      df = DataFrame(
                      [
                        All_testName_collect,
                        All_fPopIn_collect,
                        All_prefactor_collect,
                        All_E_collect,
                        All_maxShearStress_collect,
                      ],
                      index =[
                                'Test Name',
                                'Pop-in Load [mN]',
                                'fitted Hertzian prefactor[mN*µm^(-3/2)]',
                                'calculated E [GPa]',
                                'calculated max. shear stress [GPa]',
                              ],
                      )
    elif Index_ExportTab == 2:
      #define the data frame of all tests for tabClassification
      df = DataFrame(
                      [
                        win.tabClassification_FileNumber_collect,
                        win.tabClassification_TestName_collect,
                        win.tabClassification_ClusterLabels,
                        win.tabClassification_H_collect,
                        win.tabClassification_E_collect,
                        win.tabClassification_Er_collect,
                      ],
                      index =[
                              'File Number',
                              'Test Name',
                              'Cluster Number',
                              'mean of H [GPa]',
                              'mean of E [GPa]',
                              'mean of Er [GPa]',
                              ],
                      )
    elif Index_ExportTab == 3:
      #define the data frame of all tests for tabCreep
      All_testName_collect = []
      All_time_collect = []
      All_equivStress_collect = []
      All_CreepRate_collect = []
      for j, _ in enumerate(win.tabCreep_testName_collect):
        time_values = _tab_creep_time_values(win, j, len(win.tabCreep_equivStress_collect[j]))
        for k, _ in enumerate(win.tabCreep_equivStress_collect[j]):
          All_testName_collect.append(win.tabCreep_testName_collect[j])
          All_time_collect.append(time_values[k])
          All_equivStress_collect.append(win.tabCreep_equivStress_collect[j][k])
          All_CreepRate_collect.append(win.tabCreep_CreepRate_collect[j][k])
      df = DataFrame(
                      [
                        All_testName_collect,
                        All_time_collect,
                        All_equivStress_collect,
                        All_CreepRate_collect,
                      ],
                      index =[
                              'Test Name',
                              'time[s]',
                              'equiv stress[GPa]',
                              'creep rate[s-1]',
                              ],
                      )

    df = df.T
    sheetName = 'Results'
    #write to excel
    df.to_excel(writer,sheet_name=sheetName, index=False)
    for k in range(15):
      #set the width of column
      writer.sheets[sheetName].set_column(0, k, 20)

  #save the writer and create the excel file (.xlsx)
  writer.close()
  return


def _export_hdf5(output_path, index_export_tab, df_params, win):
  """Export results to a pandas/PyTables HDF5 file."""
  with pd.HDFStore(output_path, mode='w', complevel=9, complib='zlib') as h5_file:
    h5_file.root._v_attrs.export_format = 'pandas_hdfstore'
    _write_hdf_dataframe(h5_file, '/experimental_parameters', df_params)
    if index_export_tab == 0:
      summary_df = DataFrame({
        'Test Name': win.tabHE_testName_collect,
        'max. hc [µm]': [values[-1] for values in win.tabHE_hc_collect],
        'max. hmax [µm]': win.tabHE_hmax_collect,
        'max. Pmax [mN]': [values[-1] for values in win.tabHE_Pmax_collect],
        'mean of H [GPa]': win.tabHE_Hmean_collect,
        'std of H [GPa]': win.tabHE_Hstd_collect,
        'mean of E [GPa]': win.tabHE_Emean_collect,
        'std of E [GPa]': win.tabHE_Estd_collect,
        'mean of Er [GPa]': win.tabHE_Er_mean_collect,
        'std of Er [GPa]': win.tabHE_Er_std_collect,
        'X Position [µm]': win.tabHE_X_Position_collect,
        'Y Position [µm]': win.tabHE_Y_Position_collect,
      })
      _write_hdf_dataframe(h5_file, '/results', summary_df)
      test_keys = set()
      for i, test_name in enumerate(win.tabHE_testName_collect):
        x_pos = win.tabHE_X_Position_collect[i] if win.tabHE_X_Position_collect[i] is not None else 0
        y_pos = win.tabHE_Y_Position_collect[i] if win.tabHE_Y_Position_collect[i] is not None else 0
        n = len(win.tabHE_E_collect[i])
        per_test_df = DataFrame({
          'Test Name': [test_name] * n,
          'hc[µm]': win.tabHE_hc_collect[i],
          'hmax[µm]': win.tabHE_hmax_collect[i] * np.ones(n),
          'Pmax[mN]': win.tabHE_Pmax_collect[i],
          'H[GPa]': win.tabHE_H_collect[i],
          'E[GPa]': win.tabHE_E_collect[i],
          'Er[GPa]': win.tabHE_Er_collect[i],
          'X Position [µm]': x_pos * np.ones(n),
          'Y Position [µm]': y_pos * np.ones(n),
        })
        _write_hdf_dataframe(h5_file, _hdf_test_key(test_name, test_keys), per_test_df)
    elif index_export_tab == 1:
      rows = []
      for j, test_name in enumerate(win.tabPopIn_testName_collect):
        try:
          for k, _ in enumerate(win.tabPopIn_fPopIn_collect[j]):
            rows.append({
              'Test Name': test_name,
              'Pop-in Load [mN]': win.tabPopIn_fPopIn_collect[j][k],
              'fitted Hertzian prefactor[mN*µm^(-3/2)]': win.tabPopIn_prefactor_collect[j][k],
              'calculated E [GPa]': win.tabPopIn_E_collect[j][k],
              'calculated max. shear stress [GPa]': win.tabPopIn_maxShearStress_collect[j][k],
            })
        except (TypeError, IndexError):
          rows.append({
            'Test Name': test_name,
            'Pop-in Load [mN]': win.tabPopIn_fPopIn_collect[j],
            'fitted Hertzian prefactor[mN*µm^(-3/2)]': win.tabPopIn_prefactor_collect[j],
            'calculated E [GPa]': win.tabPopIn_E_collect[j],
            'calculated max. shear stress [GPa]': win.tabPopIn_maxShearStress_collect[j],
          })
      _write_hdf_dataframe(h5_file, '/results', DataFrame(rows))
    elif index_export_tab == 2:
      classification_df = DataFrame({
        'File Number': win.tabClassification_FileNumber_collect,
        'Test Name': win.tabClassification_TestName_collect,
        'Cluster Number': win.tabClassification_ClusterLabels,
        'mean of H [GPa]': win.tabClassification_H_collect,
        'mean of E [GPa]': win.tabClassification_E_collect,
        'mean of Er [GPa]': win.tabClassification_Er_collect,
      })
      _write_hdf_dataframe(h5_file, '/results', classification_df)
    elif index_export_tab == 3:
      summary_df = DataFrame({
        'Test Name': win.tabCreep_testName_collect,
        'mean of H [GPa]': win.tabCreep_Hmean_collect,
        'std of H [GPa]': win.tabCreep_Hstd_collect,
        'mean of E [GPa]': win.tabCreep_Emean_collect,
        'std of E [GPa]': win.tabCreep_Estd_collect,
        'X Position [µm]': win.tabCreep_X_Position_collect,
        'Y Position [µm]': win.tabCreep_Y_Position_collect,
      })
      _write_hdf_dataframe(h5_file, '/results', summary_df)
      test_keys = set()
      for i, test_name in enumerate(win.tabCreep_testName_collect):
        n = len(win.tabCreep_equivStress_collect[i])
        time_values = _tab_creep_time_values(win, i, n)
        per_test_df = DataFrame({
          'Test Name': [test_name] * n,
          'time[s]': time_values,
          'equiv stress[GPa]': win.tabCreep_equivStress_collect[i],
          'creep rate[s-1]': win.tabCreep_CreepRate_collect[i],
        })
        _write_hdf_dataframe(h5_file, _hdf_test_key(test_name, test_keys), per_test_df)


def _write_hdf_dataframe(store, key, df):
  """Write a DataFrame in the pandas/PyTables format expected by ViTables."""
  df = df.copy()
  for col_name in df.columns:
    if not pd.api.types.is_numeric_dtype(df[col_name]):
      df[col_name] = df[col_name].map(_stringify_hdf_value)
  hdf_format = 'fixed' if df.empty else 'table'
  with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=NaturalNameWarning)
    store.put(key, df, format=hdf_format)


def _stringify_hdf_value(value):
  """Convert object values to strings without treating array-like values as missing."""
  if value is None:
    return ''
  try:
    is_missing = pd.isna(value)
  except (TypeError, ValueError):
    is_missing = False
  if isinstance(is_missing, (bool, np.bool_)) and is_missing:
    return ''
  return str(value)


def _tab_creep_time_values(win, index, length):
  """Return creep time values matching one exported creep-rate test."""
  time_collect = getattr(win, 'tabCreep_time_collect', [])
  if index < len(time_collect):
    try:
      values = np.asarray(time_collect[index], dtype=float)
    except (TypeError, ValueError):
      values = np.asarray(time_collect[index])
    if len(values) == length:
      return values
  return np.arange(length, dtype=float)


def _hdf_test_key(test_name, used_keys):
  """Return a unique HDF5 key whose leaf matches the exported test name."""
  key_name = _sanitize_hdf_key_name(test_name)
  key = f'/tests/{key_name}'
  if key not in used_keys:
    used_keys.add(key)
    return key
  counter = 2
  while f'{key}_{counter}' in used_keys:
    counter += 1
  unique_key = f'{key}_{counter}'
  used_keys.add(unique_key)
  return unique_key


def _sanitize_hdf_key_name(value):
  """Make a test name safe as one HDF5 path component."""
  name = str(value).strip().replace('/', '_')
  return name or 'test'
