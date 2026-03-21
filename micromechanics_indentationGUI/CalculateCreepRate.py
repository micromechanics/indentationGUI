""" Graphical user interface to calculate hardness and young's modulus """
import numpy as np
import matplotlib.pylab as plt
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module
from micromechanics import indentation
from micromechanics.indentation.definitions import Vendor, Method
from .WaitingUpgrade_of_micromechanics import IndentationXXX
from .load_depth import pick, right_click_set_ContactSurface
from .Tools4LoadingData import read_file_list, Convert2inGUI
from .Tools4analyse import split_mean_var_with_index

def Calculate_CreepRate(self): # pylint: disable=too-many-locals,too-many-statements
  """ Graphical user interface to calculate hardness and young's modulus """
  #close opened HDF5 file
  try:
    self.i_tabCreep.datafile.close()
  except:
    pass
  #set Progress Bar
  progressBar = self.ui.progressBar_tabCreep
  progressBar.setValue(0)
  #Reading Inputs
  fileNameList = read_file_list(self.ui.tableWidget_path_tabCreep)
  Poisson = self.ui.doubleSpinBox_Poisson_tabCreep.value()
  eTarget = float(self.ui.lineEdit_E_tabCreep.text())
  E_Tip = self.ui.doubleSpinBox_E_Tip_tabCreep.value()
  Poisson_Tip = self.ui.doubleSpinBox_Poisson_Tip_tabCreep.value()
  unloaPMax = self.ui.doubleSpinBox_Start_Pmax_tabCreep.value()
  unloaPMin = self.ui.doubleSpinBox_End_Pmax_tabCreep.value()
  relForceRateNoise = self.ui.doubleSpinBox_relForceRateNoise_tabCreep.value()
  max_size_fluctuation = self.ui.spinBox_max_size_fluctuation_tabCreep.value()
  UsingRate2findSurface = self.ui.checkBox_UsingRate2findSurface_tabCreep.isChecked()
  UsingSurfaceIndex = self.ui.checkBox_UsingSurfaceIndex_tabCreep.isChecked()
  UsingAreaPileUp = self.ui.checkBox_UsingAreaPileUp_tabCreep.isChecked()
  Rate2findSurface = self.ui.doubleSpinBox_Rate2findSurface_tabCreep.value()
  DataFilterSize = self.ui.spinBox_DataFilterSize_tabCreep.value()
  DecreaseDataDensity = self.ui.spinBox_DecreaseDataDensity_tabCreep.value()
  min_hc4mean = self.ui.doubleSpinBox_minhc4mean_tabCreep.value()
  max_hc4mean = self.ui.doubleSpinBox_maxhc4mean_tabCreep.value()
  DataSegment4Smooth = self.ui.doubleSpinBox_DataSegment4Smooth_tabCreep.value()
  if DataFilterSize%2==0:
    DataFilterSize+=1
  TAF_terms = []
  for j in range(9):
    lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabCreep") # pylint: disable=eval-used
    TAF_terms.append(float(lineEdit.text()))
  TAF_terms.append('iso')
  FrameCompliance=float(self.ui.lineEdit_FrameCompliance_tabCreep.text())
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
  self.i_tabCreep = IndentationXXX(fileName=fileName, tip=Tip, nuMat= Poisson, surface=Surface, model=Model, output=Output)
  modulusRedGoal = self.i_tabCreep.ReducedModulus(eTarget, Poisson)
  self.i_tabCreep.model['modulusRedGoal'] = modulusRedGoal
  #initial surfaceIdx
  self.i_tabCreep.surface['surfaceIdx']={}
  #initial AreaPileUp
  self.i_tabCreep.AreaPileUp_collect={}
  #close waiting dialog
  self.close_wait()
  i = self.i_tabCreep
  #show Test method
  Method_value = i.method.value
  self.ui.comboBox_method_tabCreep.setCurrentIndex(Method_value-1)
  #setting to correct thermal drift
  try:
    correctDrift_Post = self.ui.checkBox_UsingDriftUnloading_tabCreep.isChecked()
  except:
    correctDrift_Post = False
  try:
    correctDrift_Pre = self.ui.checkBox_UsingDriftPre_tabCreep.isChecked()
  except:
    correctDrift_Pre = False
  try:
    correctDrift_Func = self.ui.checkBox_UsingDriftFunc_tabCreep.isChecked()
  except:
    correctDrift_Func = False
  if correctDrift_Func:
    correctDrift = 4
  elif correctDrift_Post and correctDrift_Pre:
    correctDrift = 3
  elif correctDrift_Post:
    correctDrift = 1
  elif correctDrift_Pre:
    correctDrift = 2
  else:
    correctDrift = 0
  i.model['driftRate'] = correctDrift
  Range_correctDrift_Post = self.ui.doubleSpinBox_UsingDriftUnloading_tabCreep.value()
  Range_correctDrift_Pre = self.ui.doubleSpinBox_UsingDriftPre_tabCreep.value()
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
  self.ui.comboBox_equipment_tabCreep.setCurrentIndex(Equipment-1)
  #changing i.allTestList to calculate using the checked tests
  OriginalAlltest = list(self.i_tabCreep.allTestList)
  for k, theTest in enumerate(OriginalAlltest):
    try:
      IsCheck = self.ui.tableWidget_tabCreep.item(k,0).checkState()
    except:
      pass
    else:
      if IsCheck==Qt.Unchecked:
        self.i_tabCreep.allTestList.remove(theTest)
  self.i_tabCreep.restartFile()
  # searching SurfaceIdx, AreaPileUp in the table
  if UsingSurfaceIndex or UsingAreaPileUp:
    for k, theTest in enumerate(OriginalAlltest):
      if UsingSurfaceIndex:
        qtablewidgetitem = self.ui.tableWidget_tabCreep.item(k, 2)
        self.i_tabCreep.testName=theTest
        if self.i_tabCreep.vendor == indentation.definitions.Vendor.Agilent:
          self.i_tabCreep.nextAgilentTest(newTest=False)
          self.i_tabCreep.nextTest(newTest=False)
        if self.i_tabCreep.vendor == indentation.definitions.Vendor.Micromaterials:
          self.i_tabCreep.nextMicromaterialsTest(newTest=False)
          self.i_tabCreep.nextTest(newTest=False)
        try:
          indexX = int(qtablewidgetitem.text())
          self.i_tabCreep.surface['surfaceIdx'].update({theTest:indexX})
        except:
          pass
      if UsingAreaPileUp:
        qtablewidgetitem = self.ui.tableWidget_tabCreep.item(k, 3)
        self.i_tabCreep.testName=theTest
        try:
          AreaPileUp = float(qtablewidgetitem.text())
          self.i_tabCreep.AreaPileUp_collect.update({theTest:AreaPileUp})
        except:
          pass
    self.i_tabCreep.restartFile()
  # save test 1 and set the data in the load depht curve can be picked
  i.output['ax'] = self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabCreep
  i.output['ax'][0].figure.canvas.mpl_connect("pick_event", self.right_click_set_ContactSurface)
  self.indentation_inLoadDepth_tabCreep = i
  i.output['ax'] = [None, None]
  #calculate Hardnss and Modulus for all Tests
  hc_collect=[]
  hmax_collect=[]
  Pmax_collect=[]
  H_collect=[]
  # time_collect=[]
  Hmean_collect=[]
  H4mean_collect=[]
  Hstd_collect=[]
  E_collect=[]
  H4ylim_collect=[]
  E4ylim_collect=[]
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
  # ax_h_t = self.static_ax_load_depth_time_tab_inclusive_frame_stiffness_tabCreep[0]
  ax_H_hc = self.static_ax_H_hc_tabCreep
  ax_E_hc = self.static_ax_E_hc_tabCreep
  ax_CreepRate1 = self.static_ax_CreepRate_tabCreep[0]
  ax_CreepRate2 = self.static_ax_CreepRate_tabCreep[1]
  ax_H_hc.cla()
  ax_E_hc.cla()
  #plotting H/E**2 - hc
  ax_HE2_hc = self.static_ax_HE2_hc_tabCreep
  ax_HE2_hc.cla()
  ax_CreepRate1.cla()
  ax_CreepRate2.cla()
  #pick the label of datapoints
  self.static_canvas_CreepRate_tabCreep.figure.canvas.mpl_connect("pick_event", pick)
  #settig initial test number
  if i.vendor is Vendor.Micromaterials:
    test_number = 1
  if correctDrift == 4:
    remove_frameCompliance = False # the frame compliance was removed during drift correction #pylint: disable=unused-variable
  else:
    remove_frameCompliance = True #pylint: disable=unused-variable
  labeld_smoothCurve = False
  hardness_duringCreep_min_collect = []
  hardness_duringCreep_max_collect = []
  CreepRate_min_collect = []
  CreepRate_max_collect = []
  while True:
    print('first while loop')
    # i.analyse(remove_frameCompliance=remove_frameCompliance,calculate_CreepRate=False)
    i.analyse(calculate_CreepRate=True)
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
      marker4mean= np.where((i.hc>=min_hc4mean) & (i.hc<=max_hc4mean))
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
      ax_H_hc.plot(i.hc[::DecreaseDataDensity],i.hardness[::DecreaseDataDensity],'.-', linewidth=1, picker=True, label=i.testName)
      ax_E_hc.plot(i.hc[::DecreaseDataDensity],i.modulus[::DecreaseDataDensity], '.-', linewidth=1, picker=True, label=i.testName)
      #plotting Creep rate
      if i.method == Method.CSM:
        Number_segments = int((i.time_duringCreep[-1] - i.time_duringCreep[0])/DataSegment4Smooth)
        hardness_duringCreep_mean, hardness_duringCreep_std, _ = split_mean_var_with_index(i.hardness_duringCreep, n_segments=Number_segments)#pylint: disable=unused-variable
        CreepRate_mean, CreepRate_std, _ = split_mean_var_with_index(i.CreepRate, n_segments=Number_segments)#pylint: disable=unused-variable
        Label = "smoothed" if not labeld_smoothCurve else None
        ax_CreepRate1.plot(hardness_duringCreep_mean/3, CreepRate_mean,
          linewidth=2, alpha=0.9,label=Label,zorder=2, color='black')
        labeld_smoothCurve = True
        ax_CreepRate1.scatter(i.hardness_duringCreep/3, i.CreepRate,
          marker='o',s=5, alpha=0.6,label=f"{i.testName}",zorder=1,picker=True)
        ax_CreepRate2.plot(hardness_duringCreep_mean/3, CreepRate_mean,
          marker='o',markersize=5, alpha=0.9,label=f"{i.testName}",zorder=2, picker=True)
        coeffs= np.polyfit(np.log10(hardness_duringCreep_mean/3.), np.log10(CreepRate_mean),1, cov=False)
        x = np.logspace(np.log10(np.min(hardness_duringCreep_mean/3.)), np.log10(np.max(hardness_duringCreep_mean/3.)), 10)
        print('x',x)
        f = np.poly1d(coeffs)
        y = 10**f(np.log10(x))
        ax_CreepRate2.plot(x,y,'--',color='gray')
        print('coeffs',coeffs)
        hardness_duringCreep_min_collect.append(np.min(hardness_duringCreep_mean))
        hardness_duringCreep_max_collect.append(np.max(hardness_duringCreep_mean))
        CreepRate_min_collect.append(np.min(CreepRate_mean))
        CreepRate_max_collect.append(np.max(CreepRate_mean))
      elif i.method == Method.MULTI:
        ax_CreepRate1.plot(i.hardness/3, i.CreepRate,marker='o')
        hardness_duringCreep_min_collect.append(np.min(i.hardness))
        hardness_duringCreep_max_collect.append(np.max(i.hardness))
        CreepRate_min_collect.append(np.min(i.CreepRate))
        CreepRate_max_collect.append(np.max(i.CreepRate))
      #plotting H/E**2 - hc
      ax_HE2_hc.plot(i.hc[::DecreaseDataDensity],i.hardness[::DecreaseDataDensity]/i.modulus[::DecreaseDataDensity]**2,'.-', linewidth=1, picker=True, label=i.testName)
    if not i.testList:
      break
    while True:
      try:
        i.nextTest()
      except Exception:
        continue  # failure → try again
      else:
        print(i.testName)
        break   # success → exit loop
  y_interval = 1 * (np.max(CreepRate_max_collect) - np.min(CreepRate_min_collect))
  ymin = max(1e-20, np.min(CreepRate_min_collect) - 1 * y_interval)
  ymax = np.max(CreepRate_max_collect) + 10 * y_interval
  ylim_range = (ymin, ymax)
  print('ylim_range',ylim_range)
  x_interval = 1 * (np.max(hardness_duringCreep_max_collect) - np.min(hardness_duringCreep_min_collect))/3.
  xlim_range = (np.min(hardness_duringCreep_min_collect)/3.-10*x_interval, np.max(hardness_duringCreep_max_collect)/3.+x_interval*30)
  ax_CreepRate1.set_ylim(ylim_range)
  ax_CreepRate1.set_xlim(xlim_range)
  # ax_CreepRate1.set_xlabel('Hardness/3 [GPa]')
  ax_CreepRate1.set_ylabel(r'dh/dt / h [s$^{-1}$]')
  ax_CreepRate1.legend()
  ax_CreepRate2.set_ylim(ylim_range)
  ax_CreepRate2.set_xlim(xlim_range)
  ax_CreepRate2.set_xlabel('Hardness/3 [GPa]')
  ax_CreepRate2.set_ylabel(r'dh/dt / h [s$^{-1}$]')
  ax_CreepRate2.legend()
  ax_CreepRate1.set_xscale("log")
  ax_CreepRate1.set_yscale("log")
  ax_CreepRate2.set_xscale("log")
  ax_CreepRate2.set_yscale("log")
  self.static_canvas_CreepRate_tabCreep.figure.set_tight_layout(True)
  self.static_canvas_CreepRate_tabCreep.draw()

  ax_H_hc.axvline(min_hc4mean,color='gray',linestyle='dashed', label='min./max. hc for calculating mean values')
  ax_E_hc.axvline(min_hc4mean,color='gray',linestyle='dashed', label='min./max. hc for calculating mean values')
  if np.max(hc_collect[0])*1.1 > max_hc4mean:
    ax_H_hc.axvline(max_hc4mean,color='gray',linestyle='dashed')
    ax_E_hc.axvline(max_hc4mean,color='gray',linestyle='dashed')
  try:
    H4ylim_all = np.hstack(H4ylim_collect)
    E4ylim_all = np.hstack(E4ylim_collect)
    Hstd_limited = min(np.std(H4ylim_all,ddof=1), 1)
    Estd_limited = min(np.std(E4ylim_all,ddof=1), 10)
    Hmean_ylim = np.mean(H4ylim_all)
    Emean_ylim = np.mean(E4ylim_all)
    ax_H_hc.set_ylim(Hmean_ylim-Hstd_limited*20,Hmean_ylim+Hstd_limited*20)
    ax_E_hc.set_ylim(Emean_ylim-Estd_limited*20,Emean_ylim+Estd_limited*20)
  except Exception as e: #pylint: disable=broad-except
    suggestion = '1. Decrease "min. hc" \n 2. Increase "min. hc" \n ' #pylint: disable=anomalous-backslash-in-string
    self.show_error(str(e),suggestion)
  if len(H_collect)<10:
    ax_H_hc.legend()
    ax_E_hc.legend()
    ax_HE2_hc.legend()
  #pick the label of datapoints
  self.static_canvas_H_hc_tabCreep.figure.canvas.mpl_connect("pick_event", pick)
  self.static_canvas_E_hc_tabCreep.figure.canvas.mpl_connect("pick_event", pick)
  self.static_canvas_HE2_hc_tabCreep.figure.canvas.mpl_connect("pick_event", pick)
  #prepare for export
  self.tabCreep_hc_collect=hc_collect
  self.tabCreep_hmax_collect=hmax_collect
  self.tabCreep_Pmax_collect=Pmax_collect
  self.tabCreep_H_collect=H_collect
  self.tabCreep_Hmean_collect=Hmean_collect
  self.tabCreep_Hstd_collect=Hstd_collect
  self.tabCreep_E_collect=E_collect
  self.tabCreep_Er_collect=Er_collect
  self.tabCreep_Emean_collect=Emean_collect
  self.tabCreep_Er_mean_collect=Er_mean_collect
  self.tabCreep_Estd_collect=Estd_collect
  self.tabCreep_Er_std_collect=Er_std_collect
  self.tabCreep_X_Position_collect=X_Position_collect
  self.tabCreep_Y_Position_collect=Y_Position_collect
  self.tabCreep_testName_collect=testName_collect
  #listing Test in the Table
  self.ui.tableWidget_tabCreep.setRowCount(len(OriginalAlltest))
  for k, theTest in enumerate(OriginalAlltest):
    qtablewidgetitem=QTableWidgetItem(theTest)
    if theTest in self.i_tabCreep.allTestList:
      qtablewidgetitem.setCheckState(Qt.Checked)
    else:
      qtablewidgetitem.setCheckState(Qt.Unchecked)
    self.ui.tableWidget_tabCreep.setItem(k,0,qtablewidgetitem)
    if f"-{theTest}" in i.output['successTest']:
      self.ui.tableWidget_tabCreep.setItem(k,1,QTableWidgetItem("No"))
    elif f"{theTest}" in i.output['successTest']:
      self.ui.tableWidget_tabCreep.setItem(k,1,QTableWidgetItem("Yes"))
    else:
      self.ui.tableWidget_tabCreep.setItem(k,1,QTableWidgetItem("No"))
  i.model['driftRate'] = False   #reset
  #open waiting dialog
  self.show_wait('GUI is plotting results!')
  #plotting hardness-Indent's Nummber and young's modulus-Indent's Nummber
  ax_H_Index = self.static_ax_H_Index_tabCreep
  ax_E_Index = self.static_ax_E_Index_tabCreep
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
  ax_HE2_hc.set_xlabel('Contact depth [µm]')
  ax_HE2_hc.set_ylabel('H/E² [-]')
  ax_E_Index.set_xlabel('Indents\'s Nummber')
  ax_E_Index.set_ylabel('Young\'s Modulus [GPa]')
  ax_H_Index.legend()
  ax_E_Index.legend()
  self.static_canvas_H_hc_tabCreep.figure.set_tight_layout(True)
  self.static_canvas_E_hc_tabCreep.figure.set_tight_layout(True)
  self.static_canvas_H_Index_tabCreep.figure.set_tight_layout(True)
  self.static_canvas_E_Index_tabCreep.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax_H_hc)
  self.set_aspectRatio(ax=ax_E_hc)
  self.set_aspectRatio(ax=ax_HE2_hc)
  self.set_aspectRatio(ax=ax_H_Index)
  self.set_aspectRatio(ax=ax_E_Index)
  self.static_canvas_H_hc_tabCreep.draw()
  self.static_canvas_E_hc_tabCreep.draw()
  self.static_canvas_HE2_hc_tabCreep.draw()
  self.static_canvas_H_Index_tabCreep.draw()
  self.static_canvas_E_Index_tabCreep.draw()
  #plotting hardness-young's modulus
  ax_HE = self.static_ax_HE_tabCreep
  ax_HE.cla()
  ax_HE.errorbar(Emean_collect, Hmean_collect, xerr=Estd_collect, yerr=Hstd_collect,marker='s', markersize=10, capsize=10, capthick=5,elinewidth=2, color='black',alpha=0.7,linestyle='')
  ax_HE.set_ylabel('Hardness [GPa]')
  ax_HE.set_xlabel('Young\'s Modulus [GPa]')
  self.static_canvas_HE_tabCreep.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax_HE)
  self.static_canvas_HE_tabCreep.draw()
  #select the test 1 and run plot load-depth curve
  item = self.ui.tableWidget_tabCreep.item(0, 0)
  self.ui.tableWidget_tabCreep.setCurrentItem(item)
  self.plot_load_depth(tabName='tabCreep', SimplePlot=True)
  self.plot_load_depth_time(tabName='tabCreep',
                            If_inclusive_frameStiffness='exclusive')
  #close waiting dialog
  self.close_wait(info='Calculation of Creep Rate is finished!')
