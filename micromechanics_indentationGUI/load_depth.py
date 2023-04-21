""" Graphical user interface to plot load-depth curves """
from micromechanics import indentation
from .CorrectThermalDrift import correctThermalDrift


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
      i.stiffnessFromUnloading(i.p, i.h, plot=True)
      i.output['ax']=None
  static_canvas.figure.set_tight_layout(True)
  static_canvas.draw()
