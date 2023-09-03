""" Graphical user interface to calculate hardness and young's modulus """
import numpy as np
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module
from micromechanics import indentation
from micromechanics.indentation.definitions import Vendor
from .CorrectThermalDrift import correctThermalDrift
from .WaitingUpgrade_of_micromechanics import IndentationXXX
from .load_depth import pick

def Calculate_Hardness_Modulus(self): # pylint: disable=too-many-locals
  """ Graphical user interface to calculate hardness and young's modulus """
  #set Progress Bar
  progressBar = self.ui.progressBar_tabHE
  progressBar.setValue(0)
  #Reading Inputs
  fileName = f"{self.ui.lineEdit_path_tabHE.text()}"
  Poisson = self.ui.doubleSpinBox_Poisson_tabHE.value()
  E_Tip = self.ui.doubleSpinBox_E_Tip_tabHE.value()
  Poisson_Tip = self.ui.doubleSpinBox_Poisson_Tip_tabHE.value()
  unloaPMax = self.ui.doubleSpinBox_Start_Pmax_tabHE.value()
  unloaPMin = self.ui.doubleSpinBox_End_Pmax_tabHE.value()
  relForceRateNoise = self.ui.doubleSpinBox_relForceRateNoise_tabHE.value()
  max_size_fluctuation = self.ui.spinBox_max_size_fluctuation_tabHE.value()
  UsingRate2findSurface = self.ui.checkBox_UsingRate2findSurface_tabHE.isChecked()
  Rate2findSurface = self.ui.doubleSpinBox_Rate2findSurface_tabHE.value()
  DataFilterSize = self.ui.spinBox_DataFilterSize_tabHE.value()
  DecreaseDataDensity = self.ui.spinBox_DecreaseDataDensity_tabHE.value()
  min_hc4mean = self.ui.doubleSpinBox_minhc4mean_tabHE.value()
  max_hc4mean = self.ui.doubleSpinBox_maxhc4mean_tabHE.value()
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
              'maxSizeFluctuations': max_size_fluctuation # maximum size of small fluctuations that are removed in identifyLoadHoldUnload
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
  self.i_tabHE = IndentationXXX(fileName=fileName, tip=Tip, nuMat= Poisson, surface=Surface, model=Model, output=Output)
  #close waiting dialog
  self.close_wait()
  i = self.i_tabHE
  #show Test method
  Method = i.method.value
  self.ui.comboBox_method_tabHE.setCurrentIndex(Method-1)
  #show Equipment
  try:
    Equipment = i.vendor.value
  except Exception as e: #pylint: disable=broad-except
    suggestion = 'Check if the Path is completed. \n A correct example: C:\G200X\\20230101\Example.xlsx' #pylint: disable=anomalous-backslash-in-string
    self.show_error(str(e), suggestion)
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
  #plot load-depth of test 1
  i.output['ax'] = self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabHE
  i.output['ax'][0].cla()
  i.output['ax'][1].cla()
  i.output['ax'][0].set_title(f"{i.testName}")
  if self.ui.checkBox_UsingDriftUnloading_tabHE.isChecked():
    correctThermalDrift(indentation=i, reFindSurface=True) #calibrate the thermal drift using the collection during the unloading
  if i.method in (indentation.definitions.Method.ISO, indentation.definitions.Method.MULTI):
    i.stiffnessFromUnloading(i.p, i.h, plot=True)
  elif i.method== indentation.definitions.Method.CSM:
    i.output['ax'][0].scatter(i.h, i.p, s=1)
    i.output['ax'][0].axhline(0, linestyle='-.', color='tab:orange', label='zero Load or Depth') #!!!!!!
    i.output['ax'][0].axvline(0, linestyle='-.', color='tab:orange') #!!!!!!
    i.output['ax'][0].legend()
    i.output['ax'][0].set_ylabel(r'force [$\mathrm{mN}$]')
    i.output['ax'][1].set_ylabel(r"$\frac{P_{cal}-P_{mea}}{P_{mea}}x100$ [%]")
    i.output['ax'][1].set_xlabel(r'depth [$\mathrm{\mu m}$]')
  self.static_canvas_load_depth_tab_inclusive_frame_stiffness_tabHE.figure.set_tight_layout(True)
  i.output['ax'] = [None, None]
  self.static_canvas_load_depth_tab_inclusive_frame_stiffness_tabHE.draw()
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
  Notlist=[]
  testName_collect=[]
  test_number_collect=[]
  X_Position_collect=[]
  Y_Position_collect=[]
  ax_H_hc = self.static_ax_H_hc_tabHE
  ax_E_hc = self.static_ax_E_hc_tabHE
  ax_H_hc.cla()
  ax_E_hc.cla()
  #settig initial test number
  if i.vendor is Vendor.Micromaterials:
    test_number = 1
  while True:
    i.analyse()
    progressBar_Value=int((2*len(i.allTestList)-len(i.testList))/(2*len(i.allTestList))*100)
    progressBar.setValue(progressBar_Value)
    if i.testName not in Notlist:
      Pmax_collect.append(i.Ac*i.hardness)
      hc_collect.append(i.hc)
      hmax_collect.append(i.h.max())
      H_collect.append(i.hardness)
      E_collect.append(i.modulus)
      X_Position_collect.append(i.X_Position)
      Y_Position_collect.append(i.Y_Position)
      marker4mean= np.where((i.hc>=min_hc4mean) & (i.hc<=max_hc4mean))
      Hmean_collect.append(np.mean(i.hardness[marker4mean]))
      H4mean_collect.append(i.hardness[marker4mean])
      Emean_collect.append(np.mean(i.modulus[marker4mean]))
      E4mean_collect.append(i.modulus[marker4mean])
      if len(i.hardness[marker4mean]) > 1:
        Hstd_collect.append(np.std(i.hardness[marker4mean], ddof=1))
        Estd_collect.append(np.std(i.modulus[marker4mean], ddof=1))
      elif len(i.hardness[marker4mean]) == 1:
        Hstd_collect.append(0)
        Estd_collect.append(0)
      testName_collect.append(i.testName)
      if i.vendor is Vendor.Micromaterials:
        test_number_collect.append(test_number)
        test_number += 1
      else:
        test_number_collect.append(int(i.testName[4:]))
      #plotting hardness and young's modulus
      ax_H_hc.plot(i.hc[::DecreaseDataDensity],i.hardness[::DecreaseDataDensity],'.-', linewidth=1, picker=True, label=i.testName)
      ax_E_hc.plot(i.hc[::DecreaseDataDensity],i.modulus[::DecreaseDataDensity], '.-', linewidth=1, picker=True, label=i.testName)
      if not i.testList:
        break
    i.nextTest()
    if self.ui.checkBox_UsingDriftUnloading_tabHE.isChecked():
      correctThermalDrift(indentation=i, reFindSurface=True) #calibrate the thermal drift using the collection during the unloading
  ax_H_hc.axvline(min_hc4mean,color='gray',linestyle='dashed', label='min./max. hc for calculating mean values')
  ax_E_hc.axvline(min_hc4mean,color='gray',linestyle='dashed', label='min./max. hc for calculating mean values')
  if np.max(hc_collect[0])*1.1 > max_hc4mean:
    ax_H_hc.axvline(max_hc4mean,color='gray',linestyle='dashed')
    ax_E_hc.axvline(max_hc4mean,color='gray',linestyle='dashed')
  # show error if the calculated hc of some test is not in the selected hc range for calculating the mean values of H and E
  if True in np.isnan(Hmean_collect):
    suggestion = 'There is Nan in H or E list. Please try to decrease min. (or max.) hc' #pylint: disable=anomalous-backslash-in-string
    self.show_error(suggestion)
  ax_H_hc.set_ylim(np.mean(Hmean_collect)-np.mean(Hmean_collect)*2,np.mean(Hmean_collect)+np.mean(Hmean_collect)*2)
  ax_E_hc.set_ylim(np.mean(Emean_collect)-np.mean(Emean_collect)*2,np.mean(Emean_collect)+np.mean(Emean_collect)*2)
  if len(H_collect)<10:
    ax_H_hc.legend()
    ax_E_hc.legend()
  #pick the label of datapoints
  self.static_canvas_H_hc_tabHE.figure.canvas.mpl_connect("pick_event", pick)
  self.static_canvas_E_hc_tabHE.figure.canvas.mpl_connect("pick_event", pick)
  #prepare for export
  self.tabHE_hc_collect=hc_collect
  self.tabHE_hmax_collect=hmax_collect
  self.tabHE_Pmax_collect=Pmax_collect
  self.tabHE_H_collect=H_collect
  self.tabHE_Hmean_collect=Hmean_collect
  self.tabHE_Hstd_collect=Hstd_collect
  self.tabHE_E_collect=E_collect
  self.tabHE_Emean_collect=Emean_collect
  self.tabHE_Estd_collect=Estd_collect
  self.tabHE_X_Position_collect=X_Position_collect
  self.tabHE_Y_Position_collect=Y_Position_collect
  self.tabHE_testName_collect=testName_collect
  #listing Test
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
  ax_H_hc.set_xlabel('Contact depth [µm]')
  ax_H_hc.set_ylabel('Hardness [GPa]')
  ax_H_Index.set_xlabel('Indents\'s Nummber')
  ax_H_Index.set_ylabel('Hardness [GPa]')
  ax_E_hc.set_xlabel('Contact depth [µm]')
  ax_E_hc.set_ylabel('Young\'s Modulus [GPa]')
  ax_E_Index.set_xlabel('Indents\'s Nummber')
  ax_E_Index.set_ylabel('Young\'s Modulus [GPa]')
  ax_H_Index.legend()
  ax_E_Index.legend()
  self.static_canvas_H_hc_tabHE.figure.set_tight_layout(True)
  self.static_canvas_E_hc_tabHE.figure.set_tight_layout(True)
  self.static_canvas_H_Index_tabHE.figure.set_tight_layout(True)
  self.static_canvas_E_Index_tabHE.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax_H_hc)
  self.set_aspectRatio(ax=ax_E_hc)
  self.set_aspectRatio(ax=ax_H_Index)
  self.set_aspectRatio(ax=ax_E_Index)
  self.static_canvas_H_hc_tabHE.draw()
  self.static_canvas_E_hc_tabHE.draw()
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
  #close waiting dialog
  self.close_wait(info='Calculation of Hardness and Modulus is finished!')
