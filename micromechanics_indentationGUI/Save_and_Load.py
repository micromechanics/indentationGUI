# pylint: skip-file
""" Module for tools for hdf5 """
import pickle
from datetime import datetime
import numpy as np
from matplotlib import colors as mcolors
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem,QComboBox # pylint: disable=no-name-in-module
from PySide6.QtGui import QColor # pylint: disable=no-name-in-module
from .Classification import colors_clustering
class data4save:
  """ class used for saving all things in a file and reloading """

  def __init__(self):
    allWidgets  = {
                    'lineEdit_MaterialName': None,             #Material's Name
                    'lineEdit_path': None,                     #Material's Path
                    'doubleSpinBox_E': None,                   #Material's Youngs Modulus
                    'doubleSpinBox_Poisson': None,             #Material's Poissons ratio
                    'lineEdit_TipName': None,                  #Tip's Name
                    'doubleSpinBox_E_Tip': None,               #Tip's Youngs Modulus
                    'doubleSpinBox_Poisson_Tip': None,         #Tip's Poissons Ratio
                    'spinBox_number_of_TAFterms': None,        #Number of Terms used for TAF
                    'doubleSpinBox_relForceRateNoise': None,   #criticalLoadingRate4indentifingLHU
                    'spinBox_max_size_fluctuation': None,      #max_size_fluctuation4indentifingLHU
                    'comboBox_method': 0,                      #method
                    'comboBox_equipment': 0,                   #equipment
                    'checkBox_UsingRate2findSurface': None,    #UsingRate2findSurface
                    'doubleSpinBox_Rate2findSurface': None,    #Rate2findSurface
                    'spinBox_DataFilterSize': None,            #DataFilterSize2findSurface
                    'doubleSpinBox_Start_Pmax': None,          #Start_Pmax
                    'doubleSpinBox_End_Pmax': None,            #End_Pmax
                    'doubleSpinBox_critDepthStiffness': None,  #critDepthStiffness
                    'doubleSpinBox_critForceStiffness': None,  #critForceStiffness
                    'progressBar': None,                       #progressBar
                    'lineEdit_FrameStiffness': None,           #FrameStiffness
                    'lineEdit_FrameCompliance': None,          #FrameCompliance
                    'lineEdit_TAF1': 24.5,                     #C0
                    'lineEdit_TAF2': 0,                        #C1
                    'lineEdit_TAF3': 0,                        #C2
                    'lineEdit_TAF4': 0,                        #C3
                    'lineEdit_TAF5': 0,                        #C4
                    'lineEdit_TAF6': 0,                        #C5
                    'lineEdit_TAF7': 0,                        #C6
                    'lineEdit_TAF8': 0,                        #C7
                    'lineEdit_TAF9': 0,                        #C8
                    'lineEdit_TAF1_2': 24.5,                   #C0  reference tip area function
                    'lineEdit_TAF2_2': 0,                      #C1
                    'lineEdit_TAF3_2': 0,                      #C2
                    'lineEdit_TAF4_2': 0,                      #C3
                    'lineEdit_TAF5_2': 0,                      #C4
                    'lineEdit_TAF6_2': 0,                      #C5
                    'lineEdit_TAF7_2': 0,                      #C6
                    'lineEdit_TAF8_2': 0,                      #C7
                    'lineEdit_TAF9_2': 0,                      #C8
                    'checkBox_plotReferenceTAF':None,          #if plot the reference TAF nearby the calculated
                    'doubleSpinBox_minhc4mean': None,          #min. hc used for calculate the average hardness and Modulus
                    'doubleSpinBox_maxhc4mean': None,          #max. hc used for calculate the average hardness and Modulus
                    'lineEdit_TipRadius': None,                #Tip Radius
                    'doubleSpinBox_TipRadius': None,           #Tip Radius
                    'lineEdit_reducedModulus': None,           #reduced Modulus
                    'lineEdit_E': None,                        #Modulus
                    'lineEdit_E_errorBar': None,               #standard deviation of Modulus
                    'checkBox_UsingDriftUnloading':None,       #UsingDriftUnloading
                    'comboBox_CalculationMethod': 0,           #choose the assumption for the calculation
                    'tableWidget': None,                       #the table listing the tests
                    'comboBox_TipType': 0,                     #the tip type used by the iterative method cacluating TAF
                    'doubleSpinBox_idealRadiusSphere': None,   #the ideal radius of the spherical Tip 
                    'doubleSpinBox_half_includedAngle_TabTAF':None, # the half included angle of cone
                    'doubleSpinBox_minhc_Tip':None,            #the minimum depth of Ac
                    'doubleSpinBox_maxhc_Tip': None,           #the maximum depth of Ac
                    'checkBox_IfTermsGreaterThanZero': None,   # if the terms of TAF should be greater than Zero, except the fisrt term of the sphere tip
                    'textEdit_Files': None,
                    'spinBox_NumberClusters': None,
                    'checkBox_ifUsingFoundNumberClusters': None,
                    'checkBox_ifPlotElbow': None,
                    'spinBox_DecreaseDataDensity': None,
                    'doubleSpinBox_WeightingRatio': None,
                    'checkBox_ifShowRealSizeIndent': None,
                    'comboBox_FlipMapping': None,
                    'doubleSpinBox_MSD': None,
                    'comboBox_MarkerType': 0,
                    'comboBox_DimensionX': 1,
                    'comboBox_DimensionY': 0,
                  }
    
    self.tabName_list = [
                          'tabTAF',
                          'tabTipRadius_FrameStiffness',
                          'tabTipRadius',
                          'tabHE_FrameStiffness',
                          'tabHE',
                          'tabPopIn_FrameStiffness',
                          'tabPopIn',
                          'tabClassification'       
                        ]

    self.tabTAF = allWidgets.copy()
    self.tabTipRadius_FrameStiffness = allWidgets.copy()
    self.tabTipRadius = allWidgets.copy()
    self.tabHE_FrameStiffness = allWidgets.copy()
    self.tabHE = allWidgets.copy()
    self.tabPopIn_FrameStiffness = allWidgets.copy()
    self.tabPopIn = allWidgets.copy()
    self.tabClassification = allWidgets.copy()
    self.data_time = None # the date and time of save

    # indentation data
    self.i_tabTAF = None
    self.i_tabTipRadius = None
    self.i_tabTipRadius_FrameStiffness = None
    self.i_tabHE = None
    self.i_tabHE_FrameStiffness = None
    self.i_tabPopIn = None
    self.i_tabPopIn_FrameStiffness = None

def read_data_in_one_Table(Widget,tabName=' '):
  data_in_Table=[]
  rowCount = Widget.rowCount()
  columnCount = Widget.columnCount()
  for j in np.arange(-1,columnCount,1):
    data_in_Table.append([])
    for i in range(rowCount):
      if j==-1:
        #try to save the check state of the first column
        try:
          theItem = Widget.item(i,int(j+1))
          if theItem.checkState() == Qt.Unchecked:
            data_in_Table[-1].append(False)
          else:
            data_in_Table[-1].append(True)
        except:
          pass
      elif j==0 and ('tabClassification' in tabName):
        #save the color index in tabClassification
        currentIndex = Widget.cellWidget(i,1).currentIndex()
        data_in_Table[-1].append(int(currentIndex))
      else:
        theItem = Widget.item(i,j)
        try:
          data_in_Table[-1].append(theItem.text())
        except:
          pass
  return data_in_Table


def reload_data_in_one_Table(Widget, data_in_Table, tabName=' '):
  try:
    rowCount = len(data_in_Table[0])
    columnCount = len(data_in_Table)
  except:
    pass
  else:
    Widget.setRowCount(rowCount)
    if 'tabClassification' in tabName:
      Widget.setColumnCount(7)
    else:
      Widget.setColumnCount(columnCount-1)
    for j in range(columnCount):
      for i in range(rowCount):
        theData = data_in_Table[j][i]
        if j==0 and ('tabClassification' not in tabName):
          theData_next_column=data_in_Table[j+1][i]
          qtablewidgetitem=QTableWidgetItem(theData_next_column)
          if theData == False:
            qtablewidgetitem.setCheckState(Qt.Unchecked)
          else:
            qtablewidgetitem.setCheckState(Qt.Checked)
          Widget.setItem(i,j,qtablewidgetitem)
        elif j==1 and ('tabClassification' in tabName):
          comboBox = QComboBox()
          Widget.setItem(i,1,QTableWidgetItem())
          Widget.setCellWidget(i, 1, comboBox)
          for row, color in enumerate(colors_clustering):
            Color = mcolors.to_rgba(color)
            comboBox.addItem(color)
            model = comboBox.model()
            model.setData(model.index(row, 0), QColor(Color[0]*255,Color[1]*255,Color[2]*255,Color[3]*255), Qt.BackgroundRole)
          if not isinstance(theData, int):
            theData=i
          try:
            Color = mcolors.to_rgba(colors_clustering[theData])
          except:
            Color = mcolors.to_rgba(colors_clustering[0])
          def ComboBoxBGcolorChanged():
            for k in range(rowCount):
              # setting the background color of comboBox
              currentIndex = Widget.cellWidget(k,1).currentIndex()
              Color = mcolors.to_rgba(colors_clustering[currentIndex])
              Widget.cellWidget(k,1).setStyleSheet(f"background-color : rgba({Color[0]*255},{Color[1]*255},{Color[2]*255},{Color[3]*255});")
          #setting the background color of comboBox
          Widget.cellWidget(i,1).setCurrentIndex(theData)
          Widget.cellWidget(i,1).setStyleSheet(f"background-color : rgba({Color[0]*255},{Color[1]*255},{Color[2]*255},{Color[3]*255});")
          Widget.cellWidget(i,1).currentIndexChanged.connect(ComboBoxBGcolorChanged)
        elif j>1:
          Widget.setItem(i,j-1,QTableWidgetItem(theData))
    return


def read_data_in_one_Tab(win,Tab,tabName):
  UI = win.ui
  widgets_list = list(Tab)
  for _, widget in enumerate(widgets_list):
    try:
      Widget = eval(f"UI.{widget}_{tabName}")
    except Exception:
      pass
    else:
      if 'lineEdit' in widget:
        Tab[widget] = Widget.text()
      elif 'textEdit' in widget:
        Tab[widget] = Widget.toPlainText()
      elif ('SpinBox' in widget) or ('spinBox' in widget):
        Tab[widget] = Widget.value()
      elif 'comboBox' in widget:
        Tab[widget] = Widget.currentIndex()
      elif 'checkBox' in widget:
        Tab[widget] = Widget.isChecked()
      elif 'progressBar' in widget:
        Tab[widget] = Widget.value()
      elif 'tableWidget' in widget:
        Tab[widget] = read_data_in_one_Table(Widget,tabName=tabName)
      else:
        print(f"**ERROR: {widget}_{tabName} is not defined in Save_and_Load")


def reload_data_in_one_Tab(win,Tab, tabName):
  UI = win.ui
  widgets_list = list(Tab)
  for _, widget in enumerate(widgets_list):
    try:
      Widget = eval(f"UI.{widget}_{tabName}")
    except Exception:
      pass
    else:
      if 'lineEdit' in widget:
        if Tab[widget]=='':
          Widget.setText(' ')
        else:
          Widget.setText(Tab[widget])
      elif 'textEdit' in widget:
        if Tab[widget]=='':
          Widget.setPlainText(' ')
        else:
          Widget.setPlainText(Tab[widget])
      elif ('SpinBox' in widget) or ('spinBox' in widget):
        Widget.setValue(Tab[widget])
      elif 'comboBox' in widget:
        if Tab[widget] is not None:
          Widget.setCurrentIndex(Tab[widget])
      elif 'checkBox' in widget:
        Widget.setChecked(Tab[widget])
      elif 'progressBar' in widget:
        Widget.setValue(Tab[widget])
      elif 'tableWidget' in widget:
        reload_data_in_one_Table(Widget, data_in_Table=Tab[widget], tabName=tabName)
      else:
        print(f"**ERROR: {widget}_{tabName} is not defined in Save_and_Load")


def SAVE(self, win):
  data = data4save()
  # datetime object containing current date and time
  now = datetime.now()
  # Month-day-year H:M:S
  data.data_time = now.strftime("%b-%d-%Y %H:%M:%S")
  #read data from all tab
  for tabName in data.tabName_list:
    try:
      Tab = eval(f"data.{tabName}")
    except:
      pass
    else:
      read_data_in_one_Tab(win=win, Tab=Tab, tabName=tabName)
  #get the file path
  win.FileName_SAVED = self.ui.lineEdit_SaveAsFileName.text()
  win.Folder_SAVED = self.ui.lineEdit_SaveAsFolder.text()
  FilePath = f"{win.Folder_SAVED}{win.slash}{win.FileName_SAVED}"
  if (FilePath not in win.RecentFiles) and ('type or selcet the path of a folder' not in FilePath):
    win.RecentFiles.insert(0,FilePath)
    win.update_OpenRecent()
  # open a file, where you ant to store the data
  file = open(FilePath, 'wb')
  # dump information to that file
  pickle.dump(data, file)
  # close the file
  file.close()
  win.setWindowTitle(f"GUI for micromechanics.indentation - [saved at {data.data_time}] - {FilePath}")


def LOAD(self, win):
  win.reNew_windows()
  win.FileName_SAVED = self.ui.lineEdit_OpenFileName.text()
  if '\n' in win.FileName_SAVED:
    win.FileName_SAVED = win.FileName_SAVED[:-1]
  win.Folder_SAVED = self.ui.lineEdit_OpenFolder.text()
  FilePath = f"{win.Folder_SAVED}{win.slash}{win.FileName_SAVED}"
  #instert the file to the top
  if FilePath not in win.RecentFiles:
    win.RecentFiles.insert(0,FilePath)
    win.update_OpenRecent()
  #move the file to the top
  else:
    for idex, RecentFile in enumerate(win.RecentFiles):
      if RecentFile == FilePath:
        win.RecentFiles.insert(0,win.RecentFiles.pop(idex))
        win.update_OpenRecent()
        break
  # open a file, where you stored the pickled data
  file = open(FilePath, 'rb')
  # dump information to that file
  data = pickle.load(file)
  #load data to all tab
  for tabName in data4save().tabName_list:
    try:
      Tab = eval(f"data.{tabName}")
    except:
      pass
    else:
      reload_data_in_one_Tab(win=win,Tab=Tab, tabName=tabName)
  # close the file
  file.close()
  try:
    win.setWindowTitle(f"GUI for micromechanics.indentation - {FilePath} - [saved at {data.data_time}]")
  except:
    win.setWindowTitle(f"GUI for micromechanics.indentation - {FilePath} - [saved at unkown time]")

