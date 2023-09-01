""" Graphical user interface to export results """
from pandas import ExcelWriter, DataFrame
import numpy as np

def export(self, win):
  """
  Graphical user interface to export calculated hardness and young's modulus

  Args:
    win (class): MainWindow
  """
  Index_ExportTab = self.ui.comboBox_ExportTab.currentIndex()
  Index_ExportFormat = self.ui.comboBox_ExportFormat.currentIndex()
  #create a writer
  slash = '\\'
  if '\\' in __file__:
    slash = '\\'
  elif '/' in __file__:
    slash = '/'
  try:
    writer = ExcelWriter(f"{self.ui.lineEdit_ExportFolder.text()}{slash}{self.ui.lineEdit_ExportFileName.text()}", engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
  except Exception as e: #pylint:disable=broad-except
    suggestion = 'Close the opened Excel file.'
    win.show_error(str(e), suggestion)
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

  #write to excel
  df.to_excel(writer,sheet_name='Experimental Parameters')
  #set the width of column
  writer.sheets['Experimental Parameters'].set_column(0, 1, 30)
  writer.sheets['Experimental Parameters'].set_column(0, 2, 60)
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
                          win.tabHE_hmax_collect[j] * np.ones(len(win.tabHE_E_collect[j])),
                          win.tabHE_Pmax_collect[j],
                          win.tabHE_H_collect[j],
                          win.tabHE_E_collect[j],
                          win.tabHE_X_Position_collect[j] * np.ones(len(win.tabHE_E_collect[j])),
                          win.tabHE_Y_Position_collect[j] * np.ones(len(win.tabHE_E_collect[j])),
                        ],
                        index =[
                                  'hc[µm]',
                                  'hmax[µm]',
                                  'Pmax[mN]',
                                  'H[GPa]',
                                  'E[GPa]',
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
      All_X_Position_collect=win.tabHE_X_Position_collect
      All_Y_Position_collect=win.tabHE_Y_Position_collect
      for j, _ in enumerate(win.tabHE_testName_collect):
        All_testName_collect.append(win.tabHE_testName_collect[j])
        All_hc_collect.append(win.tabHE_hc_collect[j][-1])
        All_hmax_collect.append(win.tabHE_hmax_collect[-1])
        All_Pmax_collect.append(win.tabHE_Pmax_collect[j][-1])
        All_Hmean_collect.append(win.tabHE_Hmean_collect[j])
        All_Hstd_collect.append(win.tabHE_Hstd_collect[j])
        All_Emean_collect.append(win.tabHE_Emean_collect[j])
        All_Estd_collect.append(win.tabHE_Estd_collect[j])
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
        except:
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

    df = df.T
    sheetName = 'Results'
    #write to excel
    df.to_excel(writer,sheet_name=sheetName, index=False)
    for k in range(10):
      #set the width of column
      writer.sheets[sheetName].set_column(0, k, 20)


  #save the writer and create the excel file (.xlsx)
  writer.close()
  return
