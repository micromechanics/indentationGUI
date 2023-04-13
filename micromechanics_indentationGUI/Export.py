""" Graphical user interface to export results """
import pandas as pd

def export(self, win):
  """ 
  Graphical user interface to export calculated hardness and young's modulus

  Args:
      win (class): MainWindow
  """
  #create a writer
  writer = pd.ExcelWriter("%s"%self.ui.lineEdit_ExportPath.text())
  #define the data frame of experimental parameters
  df = pd.DataFrame([ 
                      ['Tested Material'],
                      ['%s'%win.ui.lineEdit_MaterialName_tabHE.text()],
                      ['%s'%win.ui.lineEdit_path_tabHE.text()],
                      ['%f'%win.ui.doubleSpinBox_Poisson_tabHE.value()],
                      ['Tip'],
                      ['%s'%win.ui.lineEdit_TipName_tabHE.text()],
                      ['%f'%win.ui.doubleSpinBox_E_Tip_tabHE.value()],
                      ['%f'%win.ui.doubleSpinBox_Poisson_Tip_tabHE.value()],
                      [' '],
                      ['%s'%win.ui.lineEdit_TAF1_tabHE.text()],
                      ['%s'%win.ui.lineEdit_TAF2_tabHE.text()],
                      ['%s'%win.ui.lineEdit_TAF3_tabHE.text()],
                      ['%s'%win.ui.lineEdit_TAF4_tabHE.text()],
                      ['%s'%win.ui.lineEdit_TAF5_tabHE.text()],
                      [' '],
                      ['%s'%win.ui.lineEdit_FrameCompliance_tabHE.text()],
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
                          ], 
                      columns=[' '])
  #write to excel
  df.to_excel(writer,sheet_name='Experimental Parameters')
  #set the width of column
  writer.sheets['Experimental Parameters'].set_column(0, 1, 30) 
  writer.sheets['Experimental Parameters'].set_column(0, 2, 60) 
  #define the data frame of each tests
  for i in range(len(win.tabHE_testName_collect)):
      sheetName = win.tabHE_testName_collect[i]
      df = pd.DataFrame(
                        [
                          win.tabHE_hc_collect[i],
                          win.tabHE_Pmax_collect[i],
                          win.tabHE_H_collect[i],
                          win.tabHE_E_collect[i],
                        ],
                        index =[
                                  'hc[µm]',
                                  'Pmax[mN]',
                                  'H[GPa]',
                                  'E[GPa]',
                                ],
                        )
      df = df.T
      #write to excel
      df.to_excel(writer,sheet_name=sheetName, index=False)
      for j in range(4):
          #set the width of column
          writer.sheets[sheetName].set_column(0, j, 20)
  #save the writer and create the excel file (.xlsx)
  writer.save()
  return