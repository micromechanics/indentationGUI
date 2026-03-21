""" Graphical user interface to calculate hardness and young's modulus """
import numpy as np
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module
from micromechanics import indentation
from micromechanics.indentation.definitions import Vendor, Method
from .WaitingUpgrade_of_micromechanics import IndentationXXX
from .load_depth import pick, right_click_set_ContactSurface
from .Tools4LoadingData import read_file_list, Convert2inGUI

def Calculate_Hardness_Modulus(self): # pylint: disable=too-many-locals, too-many-statements
  """ Graphical user interface to calculate hardness and young's modulus """
  #close opened HDF5 file
  try:
    self.i_tabHE.datafile.close()
  except:
    pass
  #set Progress Bar
  progressBar = self.ui.progressBar_tabHE
  progressBar.setValue(0)
  #Reading Inputs
  fileNameList = read_file_list(self.ui.tableWidget_path_tabHE)
  Poisson = self.ui.doubleSpinBox_Poisson_tabHE.value()
  E_Tip = self.ui.doubleSpinBox_E_Tip_tabHE.value()
  Poisson_Tip = self.ui.doubleSpinBox_Poisson_Tip_tabHE.value()
  unloaPMax = self.ui.doubleSpinBox_Start_Pmax_tabHE.value()
  unloaPMin = self.ui.doubleSpinBox_End_Pmax_tabHE.value()
  relForceRateNoise = self.ui.doubleSpinBox_relForceRateNoise_tabHE.value()
  max_size_fluctuation = self.ui.spinBox_max_size_fluctuation_tabHE.value()
  UsingRate2findSurface = self.ui.checkBox_UsingRate2findSurface_tabHE.isChecked()
  UsingSurfaceIndex = self.ui.checkBox_UsingSurfaceIndex_tabHE.isChecked()
  UsingAreaPileUp = self.ui.checkBox_UsingAreaPileUp_tabHE.isChecked()
  Rate2findSurface = self.ui.doubleSpinBox_Rate2findSurface_tabHE.value()
  DataFilterSize = self.ui.spinBox_DataFilterSize_tabHE.value()
  DecreaseDataDensity = self.ui.spinBox_DecreaseDataDensity_tabHE.value()
  Usinghc4mean = self.ui.checkBox_Usinghc4mean_tabHE.isChecked()
  min_hc4mean = self.ui.doubleSpinBox_minhc4mean_tabHE.value()
  max_hc4mean = self.ui.doubleSpinBox_maxhc4mean_tabHE.value()
  # Usingh4mean = self.ui.checkBox_Usingh4mean_tabHE.isChecked()
  min_h4mean = self.ui.doubleSpinBox_minh4mean_tabHE.value()
  max_h4mean = self.ui.doubleSpinBox_maxh4mean_tabHE.value()
  if DataFilterSize%2==0:
    DataFilterSize+=1
  TAF_terms = []
  for j in range(9):
    lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabHE") # pylint: disable=eval-used
    TAF_terms.append(float(lineEdit.text()))
  TAF_terms.append('iso')
  FrameCompliance=float(self.ui.lineEdit_FrameCompliance_tabHE.text())
  #define the Tip
  Tip = indentation.Tip(compliance= FrameCompliance, shape=TAF_terms)
  #define Inputs (Model, Output, Surface)
  Model = {
              'nuTip':      Poisson_Tip,
              'modulusTip': E_Tip,      # GPa from Oliver,Pharr Method paper
              'unloadPMax':unloaPMax,        # upper end of fitting domain of unloading stiffness: Vendor-specific change
              'unloadPMin':unloaPMin,         # lower end of fitting domain of unloading stiffness: Vendor-specific change
              'relForceRateNoise':relForceRateNoise, # threshold of dp/dt use to identify start of loading: Vendor-specific change
              'maxSizeFluctuations': max_size_fluctuation, # maximum size of small fluctuations that are removed in identifyLoadHoldUnload
              'driftRate': 0
              }
  def guiProgressBar(value, location):
    if location=='convert':
      value = value/2
      progressBar.setValue(value)
  Output = {
              'progressBar': guiProgressBar,   # function to use for plotting progress bar
              }
  Surface = {}
  if UsingRate2findSurface:
    Surface = {
                "abs(dp/dh)":Rate2findSurface, "median filter":DataFilterSize
                }
  #open waiting dialog
  self.show_wait('GUI is reading the file')
  #Reading Inputs
  try:
    fileName = Convert2inGUI(fileNameList)
  except:
    pass
  self.i_tabHE = IndentationXXX(fileName=fileName, tip=Tip, nuMat= Poisson, surface=Surface, model=Model, output=Output)
  #initial surfaceIdx
  self.i_tabHE.surface['surfaceIdx']={}
  #initial AreaPileUp
  self.i_tabHE.AreaPileUp_collect={}
  #close waiting dialog
  self.close_wait()
  i = self.i_tabHE
  #show Test method
  Method_value = i.method.value
  self.ui.comboBox_method_tabHE.setCurrentIndex(Method_value-1)
  #setting to correct thermal drift
  try:
    correctDrift_Post = self.ui.checkBox_UsingDriftUnloading_tabHE.isChecked()
  except:
    correctDrift_Post = False
  try:
    correctDrift_Pre = self.ui.checkBox_UsingDriftPre_tabHE.isChecked()
  except:
    correctDrift_Pre = False
  if correctDrift_Post and correctDrift_Pre:
    correctDrift = 3
  elif correctDrift_Post:
    correctDrift = 1
  elif correctDrift_Pre:
    correctDrift = 2
  else:
    correctDrift = 0
  i.model['driftRate'] = correctDrift
  Range_correctDrift_Post = self.ui.doubleSpinBox_UsingDriftUnloading_tabHE.value()
  Range_correctDrift_Pre = self.ui.doubleSpinBox_UsingDriftPre_tabHE.value()
  i.model['Range_PostDrift'] = Range_correctDrift_Post
  i.model['Range_PreDrift'] = Range_correctDrift_Pre
  #show Equipment
  try:
    Equipment = i.vendor.value
  except Exception as e: #pylint: disable=broad-except
    suggestion = 'Check if the Path is completed. \n A correct example: C:\G200X\\20230101\Example.xlsx' #pylint: disable=anomalous-backslash-in-string
    self.show_error(str(e), suggestion)
  #show Equipment
  if 'zip' in fileNameList[0]:
    Equipment = 2
  self.ui.comboBox_equipment_tabHE.setCurrentIndex(Equipment-1)
  #changing i.allTestList to calculate using the checked tests
  OriginalAlltest = list(self.i_tabHE.allTestList)
  for k, theTest in enumerate(OriginalAlltest):
    try:
      IsCheck = self.ui.tableWidget_tabHE.item(k,0).checkState()
    except:
      pass
    else:
      if IsCheck==Qt.Unchecked:
        self.i_tabHE.allTestList.remove(theTest)
  self.i_tabHE.restartFile()
  # searching SurfaceIdx, AreaPileUp in the table
  if UsingSurfaceIndex or UsingAreaPileUp:
    for k, theTest in enumerate(OriginalAlltest):
      if UsingSurfaceIndex:
        qtablewidgetitem = self.ui.tableWidget_tabHE.item(k, 2)
        self.i_tabHE.testName=theTest
        if self.i_tabHE.vendor == indentation.definitions.Vendor.Agilent:
          self.i_tabHE.nextAgilentTest(newTest=False)
          self.i_tabHE.nextTest(newTest=False)
        if self.i_tabHE.vendor == indentation.definitions.Vendor.Micromaterials:
          self.i_tabHE.nextMicromaterialsTest(newTest=False)
          self.i_tabHE.nextTest(newTest=False)
        try:
          indexX = int(qtablewidgetitem.text())
          self.i_tabHE.surface['surfaceIdx'].update({theTest:indexX})
        except:
          pass
      if UsingAreaPileUp:
        qtablewidgetitem = self.ui.tableWidget_tabHE.item(k, 3)
        self.i_tabHE.testName=theTest
        try:
          AreaPileUp = float(qtablewidgetitem.text())
          self.i_tabHE.AreaPileUp_collect.update({theTest:AreaPileUp})
        except:
          pass
    self.i_tabHE.restartFile()
  # save test 1 and set the data in the load depht curve can be picked
  i.output['ax'] = self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabHE
  i.output['ax'][0].figure.canvas.mpl_connect("pick_event", self.right_click_set_ContactSurface)
  self.indentation_inLoadDepth_tabHE = i
  i.output['ax'] = [None, None]
  #calculate Hardnss and Modulus for all Tests
  hc_collect=[]
  hmax_collect=[]
  Pmax_collect=[]
  H_collect=[]
  Hmean_collect=[]
  H4mean_collect=[]
  Hstd_collect=[]
  E_collect=[]
  Emean_collect=[]
  E4mean_collect=[]
  Estd_collect=[]
  Er_collect=[]
  Er_mean_collect=[]
  Er_4mean_collect=[]
  Er_std_collect=[]
  Notlist=[]
  testName_collect=[]
  test_number_collect=[]
  X_Position_collect=[]
  Y_Position_collect=[]
  ax_H_hc = self.static_ax_H_hc_tabHE
  ax_H_h = self.static_ax_H_h_tabHE
  ax_E_hc = self.static_ax_E_hc_tabHE
  ax_E_h = self.static_ax_E_h_tabHE
  ax_H_hc.cla()
  ax_H_h.cla()
  ax_E_hc.cla()
  ax_E_h.cla()
  H4ylim_collect=[]
  E4ylim_collect=[]
  #plotting H/E**2 - hc
  ax_HE2_hc = self.static_ax_HE2_hc_tabHE
  ax_HE2_hc.cla()
  #settig initial test number
  if i.vendor is Vendor.Micromaterials:
    test_number = 1
  while True:
    i.analyse()
    progressBar_Value=int((2*len(i.allTestList)-len(i.testList))/(2*len(i.allTestList))*100)
    progressBar.setValue(progressBar_Value)
    if i.testName not in Notlist:
      if UsingAreaPileUp and (i.testName in i.AreaPileUp_collect):
        # correct pile-up
        i.PileUpCorrection(i.AreaPileUp_collect[i.testName])
      Pmax_collect.append(i.Ac*i.hardness)
      hc_collect.append(i.hc)
      hmax_collect.append(i.h.max())
      H_collect.append(i.hardness)
      E_collect.append(i.modulus)
      marker4ylim = np.where(i.hc > 0.05)[0]
      if len(marker4ylim) == 0:
        marker4ylim = np.arange(len(i.hc))
      H4ylim_collect.append(i.hardness[marker4ylim])
      E4ylim_collect.append(i.modulus[marker4ylim])
      Er_collect.append(i.modulusRed)
      try:
        X_Position_collect.append(i.X_Position)
      except Exception as e: #pylint: disable=broad-except
        X_Position_collect.append(0)
        # show error
        suggestion = 're-export raw data from the machince to add X- and Y-Position' #pylint: disable=anomalous-backslash-in-string
        self.show_error(str(e),suggestion)
      try:
        Y_Position_collect.append(i.Y_Position)
      except Exception as e: #pylint: disable=broad-except
        Y_Position_collect.append(0)
        # show error
        suggestion = 're-export raw data from the machince to add X- and Y-Position' #pylint: disable=anomalous-backslash-in-string
        self.show_error(str(e),suggestion)
      if Usinghc4mean:
        marker4mean= np.where((i.hc>=min_hc4mean) & (i.hc<=max_hc4mean))
      else:
        marker4mean= np.where((i.h[i.valid]>=min_h4mean) & (i.h[i.valid]<=max_h4mean))
      Hmean_collect.append(np.mean(i.hardness[marker4mean]))
      H4mean_collect.append(i.hardness[marker4mean])
      Emean_collect.append(np.mean(i.modulus[marker4mean]))
      E4mean_collect.append(i.modulus[marker4mean])
      Er_mean_collect.append(np.mean(i.modulusRed[marker4mean]))
      Er_4mean_collect.append(i.modulusRed[marker4mean])
      if len(i.hardness[marker4mean]) > 1:
        Hstd_collect.append(np.std(i.hardness[marker4mean], ddof=1))
        Estd_collect.append(np.std(i.modulus[marker4mean], ddof=1))
        Er_std_collect.append(np.std(i.modulusRed[marker4mean], ddof=1))
      elif len(i.hardness[marker4mean]) == 1:
        Hstd_collect.append(0)
        Estd_collect.append(0)
        Er_std_collect.append(0)
      testName_collect.append(i.testName)
      if i.vendor is Vendor.Micromaterials:
        test_number_collect.append(test_number)
        test_number += 1
      else:
        test_number_collect.append(int(i.testName[4:]))
      #plotting hardness and young's modulus
      if i.method==Method.CSM:
        ax_H_hc.plot(i.hc[::DecreaseDataDensity],i.hardness[::DecreaseDataDensity],'-', linewidth=1, alpha=0.8, picker=True, label=i.testName)
        ax_H_h.plot(i.h[i.valid][::DecreaseDataDensity],i.hardness[::DecreaseDataDensity],'-', linewidth=1, alpha=0.8, picker=True, label=i.testName)
        ax_E_hc.plot(i.hc[::DecreaseDataDensity],i.modulus[::DecreaseDataDensity], '-', linewidth=1, alpha=0.8, picker=True, label=i.testName)
        ax_E_h.plot(i.h[i.valid][::DecreaseDataDensity],i.modulus[::DecreaseDataDensity], '-', linewidth=1, alpha=0.8, picker=True, label=i.testName)
      else:
        ax_H_hc.plot(i.hc[::DecreaseDataDensity],i.hardness[::DecreaseDataDensity],'.-', linewidth=1, picker=True, label=i.testName)
        ax_H_h.plot(i.h[i.valid][::DecreaseDataDensity],i.hardness[::DecreaseDataDensity],'.-', linewidth=1, picker=True, label=i.testName)
        ax_E_hc.plot(i.hc[::DecreaseDataDensity],i.modulus[::DecreaseDataDensity], '.-', linewidth=1, picker=True, label=i.testName)
        ax_E_h.plot(i.h[i.valid][::DecreaseDataDensity],i.modulus[::DecreaseDataDensity], '.-', linewidth=1, picker=True, label=i.testName)
      #plotting H/E**2 - hc
      ax_HE2_hc.plot(i.hc[::DecreaseDataDensity],i.hardness[::DecreaseDataDensity]/i.modulus[::DecreaseDataDensity]**2,'.-', linewidth=1, picker=True, label=i.testName)
    if not i.testList:
      break
    i.nextTest()

  ax_H_hc.axvline(i.hc[marker4mean][0],color='gray',linestyle='dashed', label='min./max. hc for calculating mean values')
  ax_E_hc.axvline(i.hc[marker4mean][0],color='gray',linestyle='dashed', label='min./max. hc for calculating mean values')
  if np.max(hc_collect[0])*1.1 > i.hc[marker4mean][-1]:
    ax_H_hc.axvline(i.hc[marker4mean][-1],color='gray',linestyle='dashed')
    ax_E_hc.axvline(i.hc[marker4mean][-1],color='gray',linestyle='dashed')
  try:
    H4ylim_all = np.hstack(H4ylim_collect)
    E4ylim_all = np.hstack(E4ylim_collect)
    Hstd_limited = min(np.std(H4ylim_all,ddof=1), 1)
    Estd_limited = min(np.std(E4ylim_all,ddof=1), 10)
    Hmean_ylim = np.mean(H4ylim_all)
    Emean_ylim = np.mean(E4ylim_all)
    ax_H_hc.set_ylim(Hmean_ylim-Hstd_limited*20,Hmean_ylim+Hstd_limited*20)
    ax_H_h.set_ylim(Hmean_ylim-Hstd_limited*20,Hmean_ylim+Hstd_limited*20)
    ax_E_hc.set_ylim(Emean_ylim-Estd_limited*20,Emean_ylim+Estd_limited*20)
    ax_E_h.set_ylim(Emean_ylim-Estd_limited*20,Emean_ylim+Estd_limited*20)
  except Exception as e: #pylint: disable=broad-except
    suggestion = '1. Decrease "min. hc" \n 2. Increase "min. hc" \n ' #pylint: disable=anomalous-backslash-in-string
    self.show_error(str(e),suggestion)
  if len(H_collect)<10:
    ax_H_hc.legend()
    ax_H_h.legend()
    ax_E_hc.legend()
    ax_E_h.legend()
    ax_HE2_hc.legend()
  #pick the label of datapoints
  self.static_canvas_H_hc_tabHE.figure.canvas.mpl_connect("pick_event", pick)
  self.static_canvas_H_h_tabHE.figure.canvas.mpl_connect("pick_event", pick)
  self.static_canvas_E_hc_tabHE.figure.canvas.mpl_connect("pick_event", pick)
  self.static_canvas_E_h_tabHE.figure.canvas.mpl_connect("pick_event", pick)
  self.static_canvas_HE2_hc_tabHE.figure.canvas.mpl_connect("pick_event", pick)
  #prepare for export
  self.tabHE_hc_collect=hc_collect
  self.tabHE_hmax_collect=hmax_collect
  self.tabHE_Pmax_collect=Pmax_collect
  self.tabHE_H_collect=H_collect
  self.tabHE_Hmean_collect=Hmean_collect
  self.tabHE_Hstd_collect=Hstd_collect
  self.tabHE_E_collect=E_collect
  self.tabHE_Er_collect=Er_collect
  self.tabHE_Emean_collect=Emean_collect
  self.tabHE_Er_mean_collect=Er_mean_collect
  self.tabHE_Estd_collect=Estd_collect
  self.tabHE_Er_std_collect=Er_std_collect
  self.tabHE_X_Position_collect=X_Position_collect
  self.tabHE_Y_Position_collect=Y_Position_collect
  self.tabHE_testName_collect=testName_collect
  #listing Test in the Table
  self.ui.tableWidget_tabHE.setRowCount(len(OriginalAlltest))
  for k, theTest in enumerate(OriginalAlltest):
    qtablewidgetitem=QTableWidgetItem(theTest)
    if theTest in self.i_tabHE.allTestList:
      qtablewidgetitem.setCheckState(Qt.Checked)
    else:
      qtablewidgetitem.setCheckState(Qt.Unchecked)
    self.ui.tableWidget_tabHE.setItem(k,0,qtablewidgetitem)
    if f"{theTest}" in i.output['successTest']:
      self.ui.tableWidget_tabHE.setItem(k,1,QTableWidgetItem("Yes"))
    else:
      self.ui.tableWidget_tabHE.setItem(k,1,QTableWidgetItem("No"))
  i.model['driftRate'] = False   #reset
  #open waiting dialog
  self.show_wait('GUI is plotting results!')
  #plotting hardness-Indent's Nummber and young's modulus-Indent's Nummber
  ax_H_Index = self.static_ax_H_Index_tabHE
  ax_E_Index = self.static_ax_E_Index_tabHE
  ax_H_Index.cla()
  ax_E_Index.cla()
  H4mean_collect=np.hstack(H4mean_collect)
  E4mean_collect=np.hstack(E4mean_collect)
  ax_H_Index.errorbar(test_number_collect,Hmean_collect,yerr=Hstd_collect,marker='s', markersize=10, capsize=10, capthick=5,elinewidth=2, color='black',alpha=0.7,linestyle='')
  ax_H_Index.axhline(np.mean(H4mean_collect), color = 'tab:orange', label = f"average Hardenss: {np.mean(H4mean_collect)} GPa",zorder=3)
  ax_H_Index.axhline(np.mean(H4mean_collect)+np.std(H4mean_collect,ddof=1), color = 'tab:orange', linestyle='dashed', label = f"standard Deviation: +- {np.std(H4mean_collect,ddof=1)} GPa",zorder=3)
  ax_H_Index.axhline(np.mean(H4mean_collect)-np.std(H4mean_collect,ddof=1), color = 'tab:orange', linestyle='dashed',zorder=3)
  ax_E_Index.errorbar(test_number_collect,Emean_collect,yerr=Estd_collect,marker='s', markersize=10, capsize=10, capthick=5,elinewidth=2, color='black',alpha=0.7,linestyle='')
  ax_E_Index.axhline(np.mean(E4mean_collect), color = 'tab:orange', label = f"average Young's Modulus: {np.mean(E4mean_collect)} GPa",zorder=3)
  ax_E_Index.axhline(np.mean(E4mean_collect)+np.std(E4mean_collect,ddof=1), color = 'tab:orange', linestyle='dashed', label = f"standard Deviation: +- {np.std(E4mean_collect,ddof=1)} GPa",zorder=3)
  ax_E_Index.axhline(np.mean(E4mean_collect)-np.std(E4mean_collect,ddof=1), color = 'tab:orange', linestyle='dashed',zorder=3)
  ax_H_hc.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.7)
  ax_H_hc.set_xlabel('Contact depth [µm]')
  ax_H_hc.set_ylabel('Hardness [GPa]')
  ax_H_h.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.7)
  ax_H_h.set_xlabel('Depth [µm]')
  ax_H_h.set_ylabel('Hardness [GPa]')
  ax_H_Index.set_xlabel('Indents\'s Nummber')
  ax_H_Index.set_ylabel('Hardness [GPa]')
  ax_E_hc.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.7)
  ax_E_hc.set_xlabel('Contact depth [µm]')
  ax_E_hc.set_ylabel('Young\'s Modulus [GPa]')
  ax_E_h.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.7)
  ax_E_h.set_xlabel('Depth [µm]')
  ax_E_h.set_ylabel('Young\'s Modulus [GPa]')
  ax_HE2_hc.set_xlabel('Contact depth [µm]')
  ax_HE2_hc.set_ylabel('H/E² [-]')
  ax_E_Index.set_xlabel('Indents\'s Nummber')
  ax_E_Index.set_ylabel('Young\'s Modulus [GPa]')
  ax_H_Index.legend()
  ax_E_Index.legend()
  self.static_canvas_H_hc_tabHE.figure.set_tight_layout(True)
  self.static_canvas_H_h_tabHE.figure.set_tight_layout(True)
  self.static_canvas_E_hc_tabHE.figure.set_tight_layout(True)
  self.static_canvas_E_h_tabHE.figure.set_tight_layout(True)
  self.static_canvas_H_Index_tabHE.figure.set_tight_layout(True)
  self.static_canvas_E_Index_tabHE.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax_H_hc)
  self.set_aspectRatio(ax=ax_H_h)
  self.set_aspectRatio(ax=ax_E_hc)
  self.set_aspectRatio(ax=ax_E_h)
  self.set_aspectRatio(ax=ax_HE2_hc)
  self.set_aspectRatio(ax=ax_H_Index)
  self.set_aspectRatio(ax=ax_E_Index)
  self.static_canvas_H_hc_tabHE.draw()
  self.static_canvas_H_h_tabHE.draw()
  self.static_canvas_E_hc_tabHE.draw()
  self.static_canvas_E_h_tabHE.draw()
  self.static_canvas_HE2_hc_tabHE.draw()
  self.static_canvas_H_Index_tabHE.draw()
  self.static_canvas_E_Index_tabHE.draw()
  #plotting hardness-young's modulus
  ax_HE = self.static_ax_HE_tabHE
  ax_HE.cla()
  ax_HE.errorbar(Emean_collect, Hmean_collect, xerr=Estd_collect, yerr=Hstd_collect,marker='s', markersize=10, capsize=10, capthick=5,elinewidth=2, color='black',alpha=0.7,linestyle='')
  ax_HE.set_ylabel('Hardness [GPa]')
  ax_HE.set_xlabel('Young\'s Modulus [GPa]')
  self.static_canvas_HE_tabHE.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax_HE)
  self.static_canvas_HE_tabHE.draw()
  #select the test 1 and run plot load-depth curve
  item = self.ui.tableWidget_tabHE.item(0, 0)
  self.ui.tableWidget_tabHE.setCurrentItem(item)
  self.plot_load_depth(tabName='tabHE', SimplePlot=True)
  #close waiting dialog
  self.close_wait(info='Calculation of Hardness and Modulus is finished!')
