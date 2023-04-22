""" Graphical user interface to calculate the frame stiffness """
from micromechanics import indentation
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module

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
  #define Inputs (Model, Output, Surface)
  Model = {
            'unloadPMax':unloaPMax,        # upper end of fitting domain of unloading stiffness: Vendor-specific change
            'unloadPMin':unloaPMin,         # lower end of fitting domain of unloading stiffness: Vendor-specific change
            'relForceRateNoise':relForceRateNoise, # threshold of dp/dt use to identify start of loading: Vendor-specific change
            'maxSizeFluctuations': max_size_fluctuation # maximum size of small fluctuations that are removed in identifyLoadHoldUnload
            }
  def guiProgressBar(value, location):
    if location=='load':
      value = value/2
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
  i_FrameStiffness = indentation.Indentation(fileName=fileName, surface=Surface, model=Model, output=Output)
  #show Test method
  Method=i_FrameStiffness.method.value
  exec(f"self.ui.comboBox_method_{tabName}.setCurrentIndex({Method-1})") # pylint: disable = exec-used
  #plot load-depth of test 1
  ax_load_depth = eval(f"self.static_ax_load_depth_tab_inclusive_frame_stiffness_{tabName}") # pylint: disable = eval-used
  canvas_load_depht = eval(f"self.static_canvas_load_depth_tab_inclusive_frame_stiffness_{tabName}") # pylint: disable = eval-used
  ax_load_depth.cla()
  ax_load_depth.set_title(f"{i_FrameStiffness.testName}")
  i_FrameStiffness.output['ax'] = ax_load_depth
  i_FrameStiffness.stiffnessFromUnloading(i_FrameStiffness.p, i_FrameStiffness.h, plot=True)
  if i_FrameStiffness.method in (indentation.definitions.Method.ISO, indentation.definitions.Method.MULTI):
    i_FrameStiffness.stiffnessFromUnloading(i_FrameStiffness.p, i_FrameStiffness.h, plot=True)
  elif i_FrameStiffness.method== indentation.definitions.Method.CSM:
    i_FrameStiffness.output['ax'].plot(i_FrameStiffness.h, i_FrameStiffness.p)
  canvas_load_depht.figure.set_tight_layout(True)
  canvas_load_depht.draw()
  i_FrameStiffness.output['ax'] = None
  #calculate FrameStiffness
  ax = eval(f"self.static_ax_{tabName}") # pylint: disable = eval-used
  ax.cla()
  i_FrameStiffness.output['ax'] = ax
  critDepth=eval(f"self.ui.doubleSpinBox_critDepthStiffness_{tabName}.value()") # pylint: disable = eval-used
  critForce=eval(f"self.ui.doubleSpinBox_critForceStiffness_{tabName}.value()") # pylint: disable = eval-used
  frameCompliance = i_FrameStiffness.calibrateStiffness(critDepth=critDepth, critForce=critForce, plotStiffness=False)
  exec(f"self.static_canvas_{tabName}.draw()") # pylint: disable = exec-used
  i_FrameStiffness.output['ax'] = None
  exec(f"self.ui.lineEdit_FrameCompliance_{tabName}.setText('{frameCompliance:.10f}')") # pylint: disable = exec-used
  exec(f"self.ui.lineEdit_FrameStiffness_{tabName}.setText('{(1/frameCompliance):.10f}')") # pylint: disable = exec-used
  exec(f"self.i_{tabName} = i_FrameStiffness") # pylint: disable = exec-used
  #listing Test
  tableWidget=eval(f"self.ui.tableWidget_{tabName}") # pylint: disable = eval-used
  tableWidget.setRowCount(0)
  tableWidget.setRowCount(len(i_FrameStiffness.allTestList))
  for k, theTest in enumerate(i_FrameStiffness.allTestList):
    tableWidget.setItem(k,0,QTableWidgetItem(theTest))
    if theTest in i_FrameStiffness.output['successTest']:
      tableWidget.setItem(k,1,QTableWidgetItem("Yes"))
    else:
      tableWidget.setItem(k,1,QTableWidgetItem("No"))
  #the End of frame stiffness calibration
  progressBar.setValue(100)
