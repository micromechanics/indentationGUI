""" Graphical user interface calculate tip radius """

import numpy as np
from micromechanics import indentation
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module
from PySide6.QtGui import QColor # pylint: disable=no-name-in-module
from scipy.optimize import curve_fit
from .AnalysePopIn import Hertzian_contact_funct
from .CorrectThermalDrift import correctThermalDrift
from .WaitingUpgrade_of_micromechanics import IndentationXXX

def Calculate_TipRadius(self): #pylint: disable=too-many-locals
  """ Graphical user interface calculate tip radius """
  #set Progress Bar
  progressBar = self.ui.progressBar_tabTipRadius
  progressBar.setValue(0)
  #get Inputs
  fileName = f"{self.ui.lineEdit_path_tabTipRadius.text()}"
  E_Mat = self.ui.doubleSpinBox_E_tabTipRadius.value()
  Poisson = self.ui.doubleSpinBox_Poisson_tabTipRadius.value()
  E_Tip = self.ui.doubleSpinBox_E_Tip_tabTipRadius.value()
  Poisson_Tip = self.ui.doubleSpinBox_Poisson_Tip_tabTipRadius.value()
  unloaPMax = self.ui.doubleSpinBox_Start_Pmax_tabTipRadius.value()
  unloaPMin = self.ui.doubleSpinBox_End_Pmax_tabTipRadius.value()
  relForceRateNoise = self.ui.doubleSpinBox_relForceRateNoise_tabTipRadius.value()
  max_size_fluctuation = self.ui.spinBox_max_size_fluctuation_tabTipRadius.value()
  UsingRate2findSurface = self.ui.checkBox_UsingRate2findSurface_tabTipRadius.isChecked()
  Rate2findSurface = self.ui.doubleSpinBox_Rate2findSurface_tabTipRadius.value()
  DataFilterSize = self.ui.spinBox_DataFilterSize_tabTipRadius.value()
  if DataFilterSize%2==0:
    DataFilterSize+=1
  FrameCompliance=float(self.ui.lineEdit_FrameCompliance_tabTipRadius.text())
  #define the Tip
  Tip = indentation.Tip(compliance=FrameCompliance)
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
  #Reading Inputs
  self.i_tabTipRadius = IndentationXXX(fileName=fileName, tip=Tip, nuMat= Poisson, surface=Surface, model=Model, output=Output)
  #show Test method
  Method=self.i_tabTipRadius.method.value
  self.ui.comboBox_method_tabPopIn.setCurrentIndex(Method-1)
  #changing i.allTestList to calculate using the checked tests
  OriginalAlltest = list(self.i_tabTipRadius.allTestList)
  for k, theTest in enumerate(OriginalAlltest):
    try:
      IsCheck = self.ui.tableWidget_tabTipRadius.item(k,0).checkState()
    except:
      pass
    else:
      if IsCheck==Qt.Unchecked:
        self.i_tabTipRadius.allTestList.remove(theTest)
  self.i_tabTipRadius.restartFile()
  #plot load-depth of test 1
  self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabTipRadius[0].cla()
  self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabTipRadius[1].cla()
  self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabTipRadius[0].set_title(f"{self.i_tabTipRadius.testName}")
  self.i_tabTipRadius.output['ax']=self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabTipRadius
  if self.ui.checkBox_UsingDriftUnloading_tabTipRadius.isChecked():
    correctThermalDrift(indentation=self.i_tabTipRadius, reFindSurface=True) #calibrate the thermal drift using the collection during the unloading
  self.i_tabTipRadius.stiffnessFromUnloading(self.i_tabTipRadius.p, self.i_tabTipRadius.h, plot=True)
  self.static_canvas_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.figure.set_tight_layout(True)
  self.i_tabTipRadius.output['ax']=None
  self.static_canvas_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.draw()
  #calculate the pop-in force and the Hertzian contact parameters
  fPopIn, certainty = self.i_tabTipRadius.popIn(plot=False, correctH=False)
  #calculate the index of pop-in and surface
  iJump = np.where(self.i_tabTipRadius.p>=fPopIn)[0][0]
  iMin  = np.where(self.i_tabTipRadius.h>=0)[0][0]
  #plot Hertzian fitting of test 1
  ax1 = self.static_ax_HertzianFitting_tabTipRadius
  ax1.cla()
  ax1.plot(self.i_tabTipRadius.h,self.i_tabTipRadius.p,marker='.',alpha=0.8)
  fitElast = [certainty['prefactor'],certainty['h0']]
  ax1.plot(self.i_tabTipRadius.h[iMin:int(1.2*iJump)], Hertzian_contact_funct(self.i_tabTipRadius.h[iMin:int(1.2*iJump)],*fitElast), color='tab:red', label='fitted loading')
  ax1.axvline(self.i_tabTipRadius.h[iJump], color='tab:orange', linestyle='dashed', label='Depth at pop-in')
  ax1.axhline(fPopIn, color='k', linestyle='dashed', label='Force at pop-in')
  ax1.set_xlim(left=-0.0001,right=4*self.i_tabTipRadius.h[iJump])
  ax1.set_ylim(top=1.5*self.i_tabTipRadius.p[iJump], bottom=-0.0001)
  ax1.set_xlabel('Depth [µm]')
  ax1.set_ylabel('Force [mN]')
  ax1.set_title(f"{self.i_tabTipRadius.testName}")
  ax1.legend()
  self.set_aspectRatio(ax=ax1)
  self.static_canvas_HertzianFitting_tabTipRadius.figure.set_tight_layout(True)
  self.static_canvas_HertzianFitting_tabTipRadius.draw()
  #initialize parameters to collect hertzian fitting results
  fPopIn_collect=[]
  prefactor_collect=[]
  Notlist=[]
  testName_collect=[]
  test_Index_collect=[]
  success_identified_PopIn = []
  depth_collect=[]
  loadHertzian_collect=[]
  depth = np.arange(0,0.1,0.001)
  i = self.i_tabTipRadius
  test_Index=1
  ax2 = self.static_ax_CalculatedTipRadius_tabTipRadius #plot the fitted prefactor
  ax2[0].cla()
  #analyse pop-in for all tests
  while True:
    i.h -= i.tip.compliance*i.p
    try:
      fPopIn, certainty = i.popIn(plot=False, correctH=False)
    except:
      test_Index+=1
      i.nextTest()
    else:
      progressBar_Value=int((2*len(i.allTestList)-len(i.testList))/(2*len(i.allTestList))*100)
      progressBar.setValue(progressBar_Value)
      if i.testName not in Notlist:
        if i.testName not in success_identified_PopIn:
          success_identified_PopIn.append(i.testName)
        fPopIn_collect.append(fPopIn)
        prefactor_collect.append(certainty["prefactor"])
        testName_collect.append(i.testName)
        test_Index_collect.append(test_Index)
        loadHertzian = Hertzian_contact_funct(depth=depth, prefactor=certainty["prefactor"], h0=0)
        ax2[0].plot(depth,loadHertzian, color='tab:blue') #plot the fitted prefactor
        depth_collect.append(depth)
        loadHertzian_collect.append(loadHertzian)
        if not i.testList:
          break
      test_Index+=1
      i.nextTest()
      if self.ui.checkBox_UsingDriftUnloading_tabTipRadius.isChecked():
        correctThermalDrift(indentation=i, reFindSurface=True) #calibrate the thermal drift using the collection during the unloading
  #calculate Tip Radius
  Er = self.i_tabTipRadius.ReducedModulus(modulus=E_Mat)
  self.ui.lineEdit_reducedModulus_tabTipRadius.setText(f"{Er:.10f}")
  prefactor_collect = np.asarray(prefactor_collect)
  TipRadius = ( 3*prefactor_collect/(4*Er) )**2
  #set lable of plotting the fitted prefactor
  ax2[0].set_xlabel('Depth [µm]')
  ax2[0].set_ylabel('Load [mN]')
  ax2[0].set_title('the fitted Hertzian Contact Function', fontsize=9)
  #plot the calculated Tip Radius
  ax2[1].cla()
  ax2[1].plot(test_Index_collect,TipRadius,'o')
  ax2[1].axhline(np.mean(TipRadius), color='k', linestyle='-', label='mean Value')
  ax2[1].axhline(np.mean(TipRadius)+np.std(TipRadius,ddof=1), color='k', linestyle='dashed', label='standard deviation')
  ax2[1].axhline(np.mean(TipRadius)-np.std(TipRadius,ddof=1), color='k', linestyle='dashed')
  ax2[1].set_xlabel('Indent\'s Number')
  ax2[1].set_ylabel('Calcultaed Tip Radius [µm]')
  ax2[1].set_title('Calcultaed Tip Radius', fontsize=9)
  #plot the Hertzian-P-h-Curve of the tip radius calculated by fitting all data
  depth_collect = (np.asarray(depth_collect)).flatten()
  loadHertzian_collect = (np.asarray(loadHertzian_collect)).flatten()
  popt, _ = curve_fit(Hertzian_contact_funct, depth_collect, loadHertzian_collect, p0=[100.,0.]) #pylint: disable=unbalanced-tuple-unpacking
  loadHertzian = Hertzian_contact_funct(depth=depth, prefactor=popt[0], h0=0)
  ax2[0].plot(depth,loadHertzian, color='tab:blue', label='for each test')
  ax2[0].plot(depth,loadHertzian, color='tab:orange', label='using all fitted Functions')
  ax2[0].legend()
  self.set_aspectRatio(ax=ax2[0])
  self.set_aspectRatio(ax=ax2[1])
  TipRadius_all_data = ( 3*popt[0]/(4*Er) )**2
  self.ui.lineEdit_TipRadius_tabTipRadius.setText(f"{TipRadius_all_data:.10f}")
  self.static_canvas_CalculatedTipRadius_tabTipRadius.figure.set_tight_layout(True)
  self.static_canvas_CalculatedTipRadius_tabTipRadius.draw()
  #listing Test
  self.ui.tableWidget_tabTipRadius.setRowCount(len(OriginalAlltest))
  for k, theTest in enumerate(OriginalAlltest):
    qtablewidgetitem=QTableWidgetItem(theTest)
    if theTest in self.i_tabTipRadius.allTestList:
      qtablewidgetitem.setCheckState(Qt.Checked)
      if theTest in self.i_tabTipRadius.output['successTest']:
        self.ui.tableWidget_tabTipRadius.setItem(k,1,QTableWidgetItem("Yes"))
      else:
        self.ui.tableWidget_tabTipRadius.setItem(k,1,QTableWidgetItem("No"))
        self.ui.tableWidget_tabTipRadius.item(k,1).setBackground(QColor(125,125,125))
      if theTest in success_identified_PopIn:
        self.ui.tableWidget_tabTipRadius.setItem(k,2,QTableWidgetItem("Yes"))
      else:
        self.ui.tableWidget_tabTipRadius.setItem(k,2,QTableWidgetItem("No"))
        self.ui.tableWidget_tabTipRadius.item(k,2).setBackground(QColor(125,125,125))
    else:
      qtablewidgetitem.setCheckState(Qt.Unchecked)
    self.ui.tableWidget_tabTipRadius.setItem(k,0,qtablewidgetitem)


def plot_Hertzian_fitting(self,tabName):
  """
  Graphical user interface to plot the Hertzian fitting of the chosen tests

  Args:
    tabName (string): the name of Tab Widget
  """
  #define indentation
  i = eval(f"self.i_{tabName}") # pylint: disable=eval-used
  #reset testList
  i.testList = list(i.allTestList)
  #read ax to plot load depth curves
  ax=eval(f"self.static_ax_HertzianFitting_{tabName}") # pylint: disable=eval-used
  ax.cla()
  #read static canvas
  static_canvas=eval(f"self.static_canvas_HertzianFitting_{tabName}") # pylint: disable=eval-used
  #read inputs from GUI
  selectedTests=eval(f"self.ui.tableWidget_{tabName}.selectedItems()") # pylint: disable=eval-used
  #plot the Hertzian fitting of the seclected tests
  plot_with_Label=True
  for Test in selectedTests:
    column=Test.column()
    if column==0:  #Test Names are located at column 0
      i.testName=Test.text()
      if i.vendor == indentation.definitions.Vendor.Agilent:
        i.nextAgilentTest(newTest=False)
        i.nextTest(newTest=False,plotSurface=False)
      if i.vendor == indentation.definitions.Vendor.Micromaterials:
        i.nextMicromaterialsTest(newTest=False)
        i.nextTest(newTest=False,plotSurface=False)
      #calculate the pop-in force and the Hertzian contact parameters
      i.output['plotDepthRate2findPopInLoad'] = False
      if len(selectedTests)==1:
        i.output['plotDepthRate2findPopInLoad'] = True
      fPopIn, certainty = i.popIn(plot=False, correctH=False)
      i.output['plotDepthRate2findPopInLoad'] = False
      #calculate the index of pop-in and surface
      iJump = np.where(i.p>=fPopIn)[0][0]
      iMin  = np.where(i.h>=0)[0][0]
      #plot
      ax.plot(i.h,i.p,marker='.',alpha=0.8,label=i.testName)
      fitElast = [certainty['prefactor'],certainty['h0']]
      if plot_with_Label:
        ax.plot(i.h[iMin:int(1.2*iJump)], Hertzian_contact_funct(i.h[iMin:int(1.2*iJump)],*fitElast), color='tab:red', label='fitted loading')
        ax.axvline(i.h[iJump], color='tab:orange', linestyle='dashed', label='Depth at pop-in')
        ax.axhline(fPopIn, color='k', linestyle='dashed', label='Force at pop-in')
        plot_with_Label=False
      else:
        ax.plot(i.h[iMin:int(1.2*iJump)], Hertzian_contact_funct(i.h[iMin:int(1.2*iJump)],*fitElast), color='tab:red')
        ax.axvline(i.h[iJump], color='tab:orange', linestyle='dashed')
        ax.axhline(fPopIn, color='k', linestyle='dashed')
    ax.set_xlim(left=-0.0001,right=4*i.h[iJump])
    ax.set_ylim(top=1.5*i.p[iJump], bottom=-0.0001)
    ax.set_xlabel('Depth [µm]')
    ax.set_ylabel('Force [mN]')
    ax.set_title(i.testName)
    ax.legend()
    self.set_aspectRatio(ax=ax)
  static_canvas.figure.set_tight_layout(True)
  static_canvas.draw()
