""" Graphical user interface to calculate the frame stiffness """

#pylint: disable= unsubscriptable-object

from micromechanics import indentation
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module
from .WaitingUpgrade_of_micromechanics import IndentationXXX
from .load_depth import pick

def FrameStiffness(self,tabName):
  """
  Graphical user interface to calculate the frame stiffness
  Args:
    tabName (string): the name of Tab Widget
  """
  #set Progress Bar
  progressBar = eval(f"self.ui.progressBar_{tabName}")    # pylint: disable = eval-used
  progressBar.setValue(0)
  #get inputs
  fileName =eval(f"self.ui.lineEdit_path_{tabName}.text()") # pylint: disable = eval-used
  unloaPMax = eval(f"self.ui.doubleSpinBox_Start_Pmax_{tabName}.value()") # pylint: disable = eval-used
  unloaPMin = eval(f"self.ui.doubleSpinBox_End_Pmax_{tabName}.value()") # pylint: disable = eval-used
  relForceRateNoise = eval(f"self.ui.doubleSpinBox_relForceRateNoise_{tabName}.value()") # pylint: disable = eval-used
  max_size_fluctuation = eval(f"self.ui.spinBox_max_size_fluctuation_{tabName}.value()") # pylint: disable = eval-used
  UsingRate2findSurface = eval(f"self.ui.checkBox_UsingRate2findSurface_{tabName}.isChecked()") # pylint: disable = eval-used
  Rate2findSurface = eval(f"self.ui.doubleSpinBox_Rate2findSurface_{tabName}.value()") # pylint: disable = eval-used
  DataFilterSize = eval(f"self.ui.spinBox_DataFilterSize_{tabName}.value()") # pylint: disable = eval-used
  if DataFilterSize%2==0:
    DataFilterSize+=1
  TAF_terms = []
  for j in range(9):
    lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_{tabName}") # pylint: disable=eval-used
    TAF_terms.append(float(lineEdit.text()))
  TAF_terms.append('iso')
  #define the Tip
  Tip = indentation.Tip(compliance= 0, shape=TAF_terms)
  #define Inputs (Model, Output, Surface)
  Model = {
            'unloadPMax':unloaPMax,        # upper end of fitting domain of unloading stiffness: Vendor-specific change
            'unloadPMin':unloaPMin,         # lower end of fitting domain of unloading stiffness: Vendor-specific change
            'relForceRateNoise':relForceRateNoise, # threshold of dp/dt use to identify start of loading: Vendor-specific change
            'maxSizeFluctuations': max_size_fluctuation # maximum size of small fluctuations that are removed in identifyLoadHoldUnload
            }
  def guiProgressBar(value, location):
    if location=='convert':
      value = value/2
      progressBar.setValue(value)
    if location=='calibrateStiffness':
      value = (value/2 + 1/2) *100
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
  i_FrameStiffness = IndentationXXX(fileName=fileName, tip=Tip, surface=Surface, model=Model, output=Output)
  #show Test method
  Method=i_FrameStiffness.method.value
  exec(f"self.ui.comboBox_method_{tabName}.setCurrentIndex({Method-1})") # pylint: disable = exec-used
  #setting to correct thermal drift
  try:
    correctDrift = eval(f"self.ui.checkBox_UsingDriftUnloading_{tabName}.isChecked()") #setting to correct thermal drift pylint: disable = eval-used
  except:
    correctDrift = False
  if correctDrift:
    i_FrameStiffness.model['driftRate'] = True
  else:
    i_FrameStiffness.model['driftRate'] = False
  #changing i.allTestList to calculate using the checked tests
  try:
    OriginalAlltest = list(i_FrameStiffness.allTestList)
  except Exception as e: # pylint:disable=broad-except
    suggestion = 'Check if the Path is completed. \n A correct example: C:\G200X\\20230101\Example.xlsx' # pylint: disable=anomalous-backslash-in-string
    self.show_error(str(e), suggestion)
  for k, theTest in enumerate(OriginalAlltest):
    try:
      IsCheck = eval(f"self.ui.tableWidget_{tabName}.item(k,0).checkState()") # pylint: disable = eval-used
    except:
      pass
    else:
      if IsCheck==Qt.Unchecked:
        i_FrameStiffness.allTestList.remove(theTest)
  i_FrameStiffness.restartFile()
  #plot load-depth of test 1
  ax_load_depth = eval(f"self.static_ax_load_depth_tab_inclusive_frame_stiffness_{tabName}") # pylint: disable = eval-used
  canvas_load_depht = eval(f"self.static_canvas_load_depth_tab_inclusive_frame_stiffness_{tabName}") # pylint: disable = eval-used
  ax_load_depth[0].cla()
  ax_load_depth[1].cla()
  ax_load_depth[0].set_title(f"{i_FrameStiffness.testName}")
  i_FrameStiffness.output['ax'] = ax_load_depth
  if i_FrameStiffness.method in (indentation.definitions.Method.ISO, indentation.definitions.Method.MULTI):
    i_FrameStiffness.stiffnessFromUnloading(i_FrameStiffness.p, i_FrameStiffness.h, plot=True)
  elif i_FrameStiffness.method== indentation.definitions.Method.CSM:
    i_FrameStiffness.output['ax'][0].scatter(i_FrameStiffness.h, i_FrameStiffness.p, s=1) #pylint: disable = unsubscriptable-object
    i_FrameStiffness.output['ax'][0].axhline(0, linestyle='-.', color='tab:orange', label='zero Load or Depth') #!!!!!!
    i_FrameStiffness.output['ax'][0].axvline(0, linestyle='-.', color='tab:orange') #!!!!!!
    i_FrameStiffness.output['ax'][0].legend()
    i_FrameStiffness.output['ax'][0].set_ylabel(r'force [$\mathrm{mN}$]')
    i_FrameStiffness.output['ax'][1].set_ylabel(r"$\frac{P_{cal}-P_{mea}}{P_{mea}}x100$ [%]")
    i_FrameStiffness.output['ax'][1].set_xlabel(r'depth [$\mathrm{\mu m}$]')
  canvas_load_depht.figure.set_tight_layout(True)
  i_FrameStiffness.output['ax'] = None
  canvas_load_depht.draw()
  #calculate FrameStiffness
  ax = eval(f"self.static_ax_{tabName}") # pylint: disable = eval-used
  ax[0].cla()
  ax[1].cla()
  i_FrameStiffness.output['ax'] = ax
  critDepth=eval(f"self.ui.doubleSpinBox_critDepthStiffness_{tabName}.value()") # pylint: disable = eval-used
  critForce=eval(f"self.ui.doubleSpinBox_critForceStiffness_{tabName}.value()") # pylint: disable = eval-used
  Index_CalculationMethod = eval(f"self.ui.comboBox_CalculationMethod_{tabName}.currentIndex()") # pylint: disable = eval-used
  if Index_CalculationMethod == 0:
    i_FrameStiffness.restartFile()
    i_FrameStiffness.calibrateStiffness(critDepth=critDepth, critForce=critForce, plotStiffness=False, returnData=True)
    frameCompliance = i_FrameStiffness.tip.compliance
  elif Index_CalculationMethod == 1:
    i_FrameStiffness.output['ax'] = [None,None]
    i_FrameStiffness.calibrateStiffness_iterativeMethod(critDepth=critDepth, critForce=critForce, plotStiffness=False)
    i_FrameStiffness.output['ax'] = ax
    i_FrameStiffness.calibrateStiffness_OneIteration(eTarget=False, critDepth=critDepth, critForce=critForce, plotStiffness=False)
    frameCompliance = i_FrameStiffness.tip.compliance
  #pick the label of datapoints
  ax[0].figure.canvas.mpl_connect("pick_event", pick)
  i_FrameStiffness.model['driftRate'] = False #reset
  exec(f"self.static_canvas_{tabName}.draw()") # pylint: disable = exec-used
  i_FrameStiffness.output['ax'] = [None,None]
  exec(f"self.ui.lineEdit_FrameCompliance_{tabName}.setText('{frameCompliance:.10f}')") # pylint: disable = exec-used
  exec(f"self.ui.lineEdit_FrameStiffness_{tabName}.setText('{(1/frameCompliance):.10f}')") # pylint: disable = exec-used
  exec(f"self.i_{tabName} = i_FrameStiffness") # pylint: disable = exec-used
  #listing Test
  tableWidget=eval(f"self.ui.tableWidget_{tabName}") # pylint: disable = eval-used
  tableWidget.setRowCount(len(OriginalAlltest))
  for k, theTest in enumerate(OriginalAlltest):
    qtablewidgetitem=QTableWidgetItem(theTest)
    if theTest in i_FrameStiffness.allTestList:
      qtablewidgetitem.setCheckState(Qt.Checked)
    else:
      qtablewidgetitem.setCheckState(Qt.Unchecked)
    exec(f"self.ui.tableWidget_{tabName}.setItem({k},0,qtablewidgetitem)") # pylint: disable = exec-used
    if theTest in i_FrameStiffness.output['successTest']:
      tableWidget.setItem(k,1,QTableWidgetItem("Yes"))
    else:
      tableWidget.setItem(k,1,QTableWidgetItem("No"))
  #the End of frame stiffness calibration
  progressBar.setValue(100)
