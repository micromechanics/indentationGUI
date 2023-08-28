""" Graphical user interface calculate tip radius """
import numpy as np
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module
from PySide6.QtGui import QColor # pylint: disable=no-name-in-module
from micromechanics import indentation
from micromechanics.indentation.definitions import Vendor
from .CorrectThermalDrift import correctThermalDrift
from .WaitingUpgrade_of_micromechanics import IndentationXXX

#define the function of Hertzian contact
def Hertzian_contact_funct(depth, prefactor, h0):
  """
  function of Hertzian contact

  Args:
  depth (float): depth [µm]
  prefactor (float): constant term
  h0 (float): constant term
  """
  diff = depth-h0
  if isinstance(diff, np.float64):
    diff = max(diff,0.0)
  else:
    diff[diff<0.0] = 0.0
  return prefactor* (diff)**(3./2.)

def Analyse_PopIn(self): #pylint: disable=too-many-locals
  """ Graphical user interface to analyse the pop-in effect """
  #set Progress Bar
  progressBar = self.ui.progressBar_tabPopIn
  progressBar.setValue(0)
  #get Inputs
  fileName = f"{self.ui.lineEdit_path_tabPopIn.text()}"
  Poisson = self.ui.doubleSpinBox_Poisson_tabPopIn.value()
  E_Tip = self.ui.doubleSpinBox_E_Tip_tabPopIn.value()
  Poisson_Tip = self.ui.doubleSpinBox_Poisson_Tip_tabPopIn.value()
  TipRadius = self.ui.doubleSpinBox_TipRadius_tabPopIn.value()
  unloaPMax = self.ui.doubleSpinBox_Start_Pmax_tabPopIn.value()
  unloaPMin = self.ui.doubleSpinBox_End_Pmax_tabPopIn.value()
  relForceRateNoise = self.ui.doubleSpinBox_relForceRateNoise_tabPopIn.value()
  max_size_fluctuation = self.ui.spinBox_max_size_fluctuation_tabPopIn.value()
  UsingRate2findSurface = self.ui.checkBox_UsingRate2findSurface_tabPopIn.isChecked()
  Rate2findSurface = self.ui.doubleSpinBox_Rate2findSurface_tabPopIn.value()
  DataFilterSize = self.ui.spinBox_DataFilterSize_tabPopIn.value()
  if DataFilterSize%2==0:
    DataFilterSize+=1
  FrameCompliance=float(self.ui.lineEdit_FrameCompliance_tabPopIn.text())
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
  self.i_tabPopIn = IndentationXXX(fileName=fileName, tip=Tip, nuMat= Poisson, surface=Surface, model=Model, output=Output)
  #show Test method
  Method=self.i_tabPopIn.method.value
  self.ui.comboBox_method_tabPopIn.setCurrentIndex(Method-1)
  #show Equipment
  Equipment = self.i_tabPopIn.vendor.value
  self.ui.comboBox_equipment_tabHE.setCurrentIndex(Equipment-1)
  #changing i.allTestList to calculate using the checked tests
  OriginalAlltest = list(self.i_tabPopIn.allTestList)
  for k, theTest in enumerate(OriginalAlltest):
    try:
      IsCheck = self.ui.tableWidget_tabPopIn.item(k,0).checkState()
    except:
      pass
    else:
      if IsCheck==Qt.Unchecked:
        self.i_tabPopIn.allTestList.remove(theTest)
  self.i_tabPopIn.restartFile()
  #plot load-depth of test 1
  ax0=self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabPopIn
  ax0[0].cla()
  ax0[1].cla()
  ax0[0].set_title(f"{self.i_tabPopIn.testName}")
  self.i_tabPopIn.output['ax']=ax0
  if self.ui.checkBox_UsingDriftUnloading_tabPopIn.isChecked():
    correctThermalDrift(indentation=self.i_tabPopIn, reFindSurface=True) #calibrate the thermal drift using the collection during the unloading
  self.i_tabPopIn.stiffnessFromUnloading(self.i_tabPopIn.p, self.i_tabPopIn.h, plot=True)
  self.static_canvas_load_depth_tab_inclusive_frame_stiffness_tabPopIn.figure.set_tight_layout(True)
  self.i_tabPopIn.output['ax']=None
  self.static_canvas_load_depth_tab_inclusive_frame_stiffness_tabPopIn.draw()
  #calculate the pop-in force and the Hertzian contact parameters
  try:
    fPopIn, certainty = self.i_tabPopIn.popIn(plot=False, correctH=False)
  except:
    pass
  else:
    #calculate the index of pop-in and surface
    iJump = np.where(self.i_tabPopIn.p>=fPopIn)[0][0]
    iMin  = np.where(self.i_tabPopIn.h>=0)[0][0]
    #plot Hertzian fitting of test 1
    ax1 = self.static_ax_HertzianFitting_tabPopIn
    ax1.cla()
    ax1.plot(self.i_tabPopIn.h,self.i_tabPopIn.p,marker='.',alpha=0.8)
    fitElast = [certainty['prefactor'],certainty['h0']]
    ax1.plot(self.i_tabPopIn.h[iMin:int(1.2*iJump)], Hertzian_contact_funct(self.i_tabPopIn.h[iMin:int(1.2*iJump)],*fitElast), color='tab:red', label='fitted loading')
    ax1.axvline(self.i_tabPopIn.h[iJump], color='tab:orange', linestyle='dashed', label='Depth at pop-in')
    ax1.axhline(fPopIn, color='k', linestyle='dashed', label='Force at pop-in')
    ax1.set_xlim(left=-0.0001,right=4*self.i_tabPopIn.h[iJump])
    ax1.set_ylim(top=1.5*self.i_tabPopIn.p[iJump], bottom=-0.0001)
    ax1.set_xlabel('Depth [µm]')
    ax1.set_ylabel('Force [mN]')
    ax1.set_title(f"{self.i_tabPopIn.testName}")
    ax1.legend()
    self.static_canvas_HertzianFitting_tabPopIn.figure.set_tight_layout(True)
    self.set_aspectRatio(ax=ax1)
    self.static_canvas_HertzianFitting_tabPopIn.draw()
  #initialize parameters to collect hertzian fitting results
  fPopIn_collect=[]
  prefactor_collect=[]
  Notlist=[]
  testName_collect=[]
  test_Number_collect=[]
  success_identified_PopIn = []
  #settig initial test number
  if self.i_tabPopIn.vendor is Vendor.Micromaterials:
    test_number = 1
  i = self.i_tabPopIn
  #analyse pop-in for all tests
  while True:
    i.h -= i.tip.compliance*i.p
    try:
      fPopIn, certainty = i.popIn(plot=False, correctH=False)
    except:
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
        if i.vendor is Vendor.Micromaterials:
          test_Number_collect.append(test_number)
          test_number += 1
        else:
          test_Number_collect.append(int(i.testName[4:]))
        if not i.testList:
          break
      i.nextTest()
      if self.ui.checkBox_UsingDriftUnloading_tabPopIn.isChecked():
        correctThermalDrift(indentation=i, reFindSurface=True) #calibrate the thermal drift using the collection during the unloading
  #calculate Young's Modulus
  prefactor_collect = np.asarray(prefactor_collect)
  Er = prefactor_collect * 3/ (4 * TipRadius**0.5)
  modulus = i.YoungsModulus(Er)
  #calculate the maxium shear stress
  fPopIn_collect = np.asarray(fPopIn_collect)
  max_shear_Stress = 0.31 * ( 6 * Er**2 * fPopIn_collect / (np.pi**3 * TipRadius**2) )**(1./3.)
  #plot Young's Modulus
  ax2 = self.static_ax_E_tabPopIn
  ax2.cla()
  ax2.scatter(test_Number_collect,modulus, marker='o')
  ax2.axhline(np.mean(modulus), color='k', linestyle='-', label='mean Value')
  ax2.axhline(np.mean(modulus)+np.std(modulus,ddof=1), color='k', linestyle='dashed', label='standard deviation')
  ax2.axhline(np.mean(modulus)-np.std(modulus,ddof=1), color='k', linestyle='dashed')
  ax2.set_xlabel('Indent\'s Number')
  ax2.set_ylabel('Young\'s Modulus [GPa]')
  self.ui.lineEdit_E_tabPopIn.setText(f"{np.mean(modulus):.10f}")
  self.ui.lineEdit_E_errorBar_tabPopIn.setText(f"{np.std(modulus,ddof=1):.10f}")
  self.static_canvas_E_tabPopIn.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax2)
  self.static_canvas_E_tabPopIn.draw()
  #plot the cumulative probability distribution of the max. shear stress
  ax3 = self.static_ax_maxShearStress_tabPopIn
  ax3.cla()
  sortedData = np.sort(max_shear_Stress)
  probability = (np.arange(len(sortedData))+1) / float(len(sortedData))
  ax3.plot(sortedData,probability,'-o')
  ax3.axhline(0, color='k', linestyle='-')
  ax3.axhline(1, color='k', linestyle='-')
  ax3.set_xlabel('maximum shear stress [GPa]')
  ax3.set_ylabel('cumulative probability distribution')
  self.static_canvas_maxShearStress_tabPopIn.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax3)
  self.static_canvas_maxShearStress_tabPopIn.draw()
  #plot the cumulative probability distribution of Pop-in Load
  ax4 = self.static_ax_PopInLoad_tabPopIn
  ax4.cla()
  sortedData = np.sort(fPopIn_collect)
  probability = (np.arange(len(sortedData))+1) / float(len(sortedData))
  ax4.plot(sortedData,probability,'-o')
  ax4.axhline(0, color='k', linestyle='-')
  ax4.axhline(1, color='k', linestyle='-')
  ax4.set_xlabel('Pop-in Load [mN]')
  ax4.set_ylabel('cumulative probability distribution')
  self.static_canvas_PopInLoad_tabPopIn.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax3)
  self.static_canvas_PopInLoad_tabPopIn.draw()
  #prepare for export
  self.tabPopIn_prefactor_collect=prefactor_collect
  self.tabPopIn_fPopIn_collect=fPopIn_collect
  self.tabPopIn_E_collect=modulus
  self.tabPopIn_maxShearStress_collect=max_shear_Stress
  self.tabPopIn_testName_collect=testName_collect
  #listing Test
  self.ui.tableWidget_tabPopIn.setRowCount(len(OriginalAlltest))
  for k, theTest in enumerate(OriginalAlltest):
    qtablewidgetitem=QTableWidgetItem(theTest)
    if theTest in self.i_tabPopIn.allTestList:
      qtablewidgetitem.setCheckState(Qt.Checked)
      if theTest in self.i_tabPopIn.output['successTest']:
        self.ui.tableWidget_tabPopIn.setItem(k,1,QTableWidgetItem("Yes"))
      else:
        self.ui.tableWidget_tabPopIn.setItem(k,1,QTableWidgetItem("No"))
        self.ui.tableWidget_tabPopIn.item(k,1).setBackground(QColor(125,125,125))
      if theTest in success_identified_PopIn:
        self.ui.tableWidget_tabPopIn.setItem(k,2,QTableWidgetItem("Yes"))
      else:
        self.ui.tableWidget_tabPopIn.setItem(k,2,QTableWidgetItem("No"))
        self.ui.tableWidget_tabPopIn.item(k,2).setBackground(QColor(125,125,125))
    else:
      qtablewidgetitem.setCheckState(Qt.Unchecked)
    self.ui.tableWidget_tabPopIn.setItem(k,0,qtablewidgetitem)
