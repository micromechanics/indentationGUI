""" Graphical user interface to plot load-depth curves """
from micromechanics import indentation
from .CorrectThermalDrift import correctThermalDrift


def set_aspectRatio(ax,ratio=0.618):
  """
  set the aspect ratio of a matplotlib.figure

  Args:
    ax (class): the ax of a mtaplotlib.figure
    ratio (float): the aspect ratio
  """
  x_left, x_right = ax.get_xlim()
  y_low, y_high = ax.get_ylim()
  ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)


def plot_load_depth(self,tabName,If_inclusive_frameStiffness='inclusive'):
  """
  Graphical user interface to plot the load-depth curves of the chosen tests

  Args:
    tabName (string): the name of Tab Widget
    If_inclusive_frameStiffness (string): 'inclusive' or 'exclusive'
  """
  #define indentation
  i = eval(f"self.i_{tabName}") # pylint: disable = eval-used
  #reset testList
  i.testList = list(i.allTestList)
  #read ax to plot load depth curves
  ax=eval(f"self.static_ax_load_depth_tab_{If_inclusive_frameStiffness}_frame_stiffness_{tabName}") # pylint: disable = eval-used
  ax.cla()
  #read static canvas
  static_canvas=eval(f"self.static_canvas_load_depth_tab_{If_inclusive_frameStiffness}_frame_stiffness_{tabName}") # pylint: disable = eval-used
  #read inputs from GUI
  showFindSurface = eval(f"self.ui.checkBox_showFindSurface_tab_{If_inclusive_frameStiffness}_frame_stiffness_{tabName}.isChecked()") # pylint: disable = eval-used # showFindSurface verifies plotting dP/dh slope
  selectedTests=eval(f"self.ui.tableWidget_{tabName}.selectedItems()") # pylint: disable = eval-used
  show_iLHU=eval(f"self.ui.checkBox_iLHU_{If_inclusive_frameStiffness}_frame_stiffness_{tabName}.isChecked()") # pylint: disable = eval-used  #plot the load-depth curves of the seclected tests
  #re-read the parameters for finding surface
  UsingRate2findSurface = eval(f"self.ui.checkBox_UsingRate2findSurface_{tabName}.isChecked()") # pylint: disable = eval-used
  Rate2findSurface = eval(f"self.ui.doubleSpinBox_Rate2findSurface_{tabName}.value()") # pylint: disable = eval-used
  DataFilterSize = eval(f"self.ui.spinBox_DataFilterSize_{tabName}.value()") # pylint: disable = eval-used
  if UsingRate2findSurface:
    Surface = {"abs(dp/dh)": Rate2findSurface, "median filter": DataFilterSize}
    i.surface.update(Surface)
  #re-read the parameters for indentifing Loading-Holding-UnloadingStart-UnloadingEnd
  unloaPMax = eval(f"self.ui.doubleSpinBox_Start_Pmax_{tabName}.value()") # pylint: disable = eval-used
  unloaPMin = eval(f"self.ui.doubleSpinBox_End_Pmax_{tabName}.value()") # pylint: disable = eval-used
  relForceRateNoise = eval(f"self.ui.doubleSpinBox_relForceRateNoise_{tabName}.value()") # pylint: disable = eval-used
  max_size_fluctuation = eval(f"self.ui.spinBox_max_size_fluctuation_{tabName}.value()") # pylint: disable = eval-used
  Model = {"unloadPMax": unloaPMax, "unloadPMin": unloaPMin, "relForceRateNoise": relForceRateNoise, "maxSizeFluctuations": max_size_fluctuation}
  i.model.update(Model)
  for Test in selectedTests:
    column=Test.column()
    if column==0:  #Test Names are located at column 0
      i.testName=Test.text()
      if i.vendor == indentation.definitions.Vendor.Agilent:
        if show_iLHU:
          i.output['plotLoadHoldUnload'] = True # plot iLHU
        i.nextAgilentTest(newTest=False)
        i.output['plotLoadHoldUnload'] = False
        i.nextTest(newTest=False,plotSurface=showFindSurface)
      ax.set_title(f"{i.testName}")
      i.output['ax']=ax
      try:
        correctDrift = eval(f"self.ui.checkBox_UsingDriftUnloading_{tabName}.isChecked()") # pylint: disable = eval-used
      except:
        correctDrift = False
      if correctDrift:
        correctThermalDrift(indentation=i) #calibrate the thermal drift using the collection during the unloading
      if i.method in (indentation.definitions.Method.ISO, indentation.definitions.Method.MULTI):
        i.stiffnessFromUnloading(i.p, i.h, plot=True)
      elif i.method== indentation.definitions.Method.CSM:
        i.output['ax'].plot(i.h, i.p)
      set_aspectRatio(ax=i.output['ax'])
      i.output['ax']=None
  static_canvas.figure.set_tight_layout(True)
  static_canvas.draw()
