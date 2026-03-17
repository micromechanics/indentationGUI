#pylint: disable=possibly-used-before-assignment, used-before-assignment, disable=duplicate-code

""" Graphical user interface to plot load-depth curves """
from micromechanics import indentation
from micromechanics.indentation.definitions import Method
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pylab as plt
from .load_depth import pick
from .CorrectThermalDrift import correctThermalDrift, correctThermalDrift_useFunction, correctThermalDrift_assumingConstantE

def plot_load_depth_time(self,tabName,If_inclusive_frameStiffness='inclusive'):
  """
  Graphical user interface to plot the load-depth curves of the chosen tests

  Args:
    tabName (string): the name of Tab Widget
    If_inclusive_frameStiffness (string): 'inclusive' or 'exclusive'
  """
  self.pars_plot_load_depth ={'plot_multiTest': False}
  #close all matplot figures before plotting new figures
  plt.close('all')
  #define indentation
  i = getattr(self, f"i_{tabName}")
  #reset testList
  i.testList = list(i.allTestList)
  #read ax to plot load depth curves
  ax = getattr(self, f"static_ax_load_depth_time_tab_{If_inclusive_frameStiffness}_frame_stiffness_{tabName}")
  ax[0].cla()
  ax[1].cla()
  ax[2].cla()
  #read static canvas
  static_canvas = getattr(self, f"static_canvas_load_depth_time_tab_{If_inclusive_frameStiffness}_frame_stiffness_{tabName}")
  #read inputs from GUI
  selectedTests = getattr(self.ui, f"tableWidget_{tabName}").selectedItems()
  progressbar = getattr(self.ui, f"progressBar_DepthTime_{tabName}")
  progressbar.setValue(0)
  Poisson = self.ui.doubleSpinBox_Poisson_tabCreep.value()
  eTarget = float(self.ui.lineEdit_E_tabCreep.text())
  modulusRedGoal = i.ReducedModulus(eTarget, Poisson)
  #re-read the parameters for finding surface
  showDrift = False
  showFindSurface = False
  show_iLHU = False
  UsingRate2findSurface = getattr(self.ui, f"checkBox_UsingRate2findSurface_{tabName}").isChecked()
  Rate2findSurface = getattr(self.ui, f"doubleSpinBox_Rate2findSurface_{tabName}").value()
  DataFilterSize = getattr(self.ui, f"spinBox_DataFilterSize_{tabName}").value()
  if DataFilterSize%2==0:
    DataFilterSize+=1
  if UsingRate2findSurface:
    Surface = {"abs(dp/dh)": Rate2findSurface, "median filter": DataFilterSize}
    i.surface.update(Surface)
  #re-read the parameters for indentifing Loading-Holding-UnloadingStart-UnloadingEnd
  unloaPMax = getattr(self.ui, f"doubleSpinBox_Start_Pmax_{tabName}").value()
  unloaPMin = getattr(self.ui, f"doubleSpinBox_End_Pmax_{tabName}").value()
  relForceRateNoise = getattr(self.ui, f"doubleSpinBox_relForceRateNoise_{tabName}").value()
  max_size_fluctuation = getattr(self.ui, f"spinBox_max_size_fluctuation_{tabName}").value()
  try:
    Range_correctDrift_Post = getattr(self.ui, f"doubleSpinBox_UsingDriftUnloading_{tabName}").value()
  except:
    Range_correctDrift_Post = 70
  try:
    Range_correctDrift_Pre = getattr(self.ui, f"doubleSpinBox_UsingDriftPre_{tabName}").value()
  except:
    Range_correctDrift_Pre = 70
  Model = {"unloadPMax": unloaPMax, "unloadPMin": unloaPMin,
           "relForceRateNoise": relForceRateNoise,
           "maxSizeFluctuations": max_size_fluctuation,
           "Range_PostDrift": Range_correctDrift_Post,
           "Range_PreDrift": Range_correctDrift_Pre,
           "modulusRedGoal":modulusRedGoal, #pylint: disable=duplicate-code
           }
  i.model.update(Model)
  plot_multiTest = False
  # check how to correction drift
  try:
    correctDrift_Post = getattr(self.ui, f"checkBox_UsingDriftUnloading_{tabName}").isChecked()
  except:
    correctDrift_Post = False
  try:
    correctDrift_Pre = getattr(self.ui, f"checkBox_UsingDriftPre_{tabName}").isChecked()
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
  if len(selectedTests) > 1:
    plot_multiTest = True
  self.pars_plot_load_depth['plot_multiTest'] = plot_multiTest
  for j, Test in enumerate(selectedTests):
    column=Test.column()
    if column==0:  #Test Names are located at column 0
      i.testName=Test.text()
      if i.vendor == indentation.definitions.Vendor.Agilent:
        if show_iLHU and not plot_multiTest:
          i.output['ax'] = None
          i.output['plotLoadHoldUnload'] = True # plot iLHU
        i.nextAgilentTest(newTest=False) # read the data
        i.nextTest(newTest=False,plotSurface=(showFindSurface and not plot_multiTest)) # find the surface
        i.output['plotLoadHoldUnload'] = False
      if i.vendor == indentation.definitions.Vendor.Micromaterials:
        if show_iLHU and not plot_multiTest:
          i.output['ax'] = None
          i.output['plotLoadHoldUnload'] = True # plot iLHU
        i.nextMicromaterialsTest(newTest=False)
        i.nextTest(newTest=False,plotSurface=(showFindSurface and not plot_multiTest))
        i.output['plotLoadHoldUnload'] = False
      ax[0].set_title(f"{i.testName}")
      i.output['ax']=ax
      if correctDrift and (If_inclusive_frameStiffness == 'inclusive'):
        ax_thermalDrift = False
        ax2_thermalDrift = False
        if showDrift and not plot_multiTest:
          if correctDrift in [1,3]:
            fig_thermalDrift, ax_thermalDrift = plt.subplots()
          if correctDrift in [2,3]:
            fig2_thermalDrift, ax2_thermalDrift = plt.subplots()
        #calibrate the thermal drift using the collection during the unloading
        correctThermalDrift(indentation=i, ax=ax_thermalDrift, ax2=ax2_thermalDrift, reFindSurface=True, correctDrift=correctDrift)
        if showDrift:
          try:
            if correctDrift in [1,3]:
              fig_thermalDrift.legend()
              fig_thermalDrift.show()
            if correctDrift in [2,3]:
              fig2_thermalDrift.legend()
              fig2_thermalDrift.show()
          except Exception as e: #pylint: disable=broad-except
            suggestion = 'If you want to plot load-depth curves of more than 1 test, please do not check "show thermal drift"' #pylint: disable=anomalous-backslash-in-string
            self.show_error(str(e), suggestion)
      elif correctDrift:
        correctThermalDrift(indentation=i, reFindSurface=True, correctDrift=correctDrift) #calibrate the thermal drift using the collection during the unloading
      # inclusice or exclusive the frame stiffness
      if If_inclusive_frameStiffness=='exclusive':
        if i.method == Method.CSM:
          i.analyse(calculate_HE=False,calculate_CreepRate=False)
          correctThermalDrift_assumingConstantE(i,ax,already_removed_frameCompliance=True,progressbar=progressbar)
          i.CalculateCreepRate(ax=ax)
          if j==len(selectedTests)-1:
            ax[0].figure.canvas.mpl_connect("pick_event", pick)
            ax[0].set_ylabel(r'force [$\mathrm{mN}$]')
            ax[1].set_ylabel(r'depth [nm]')
            ax[2].set_ylabel(r'hardness [GPa]')
            ax[2].set_xlabel(r'time [s]')
            # ax[0].set_ylim(-5,)
            ax[1].legend(fontsize=8)
            ax[2].legend(fontsize=8)
        elif i.method == Method.MULTI:
          i.analyse(calculate_HE=False,calculate_CreepRate=False)
          correctThermalDrift_useFunction(i,ax)
          i.CalculateCreepRate(ax=ax)
          if j==len(selectedTests)-1:
            ax[0].figure.canvas.mpl_connect("pick_event", pick)
            ax[0].set_ylabel(r'force [$\mathrm{mN}$]')
            ax[1].set_ylabel(r'depth [nm]')
            ax[2].set_ylabel(r'drift [nm/s]')
            ax[2].set_xlabel(r'time [s]')
            ax[0].set_ylim(-30,)
            ax[1].set_ylim(-30,)
            ax[1].legend(fontsize=8)
            ax[2].legend(fontsize=8)
      i.output['ax']=None
  static_canvas.figure.set_constrained_layout(True)
  static_canvas.draw()
  progressbar.setValue(100)
  return

def CalculateCreepRate(self,ax=[False, False,False]):
  """
    Calculate creep rate during indentation experiments.

    Parameters
    ----------
    ax : list
        Optional matplotlib axes for plotting results:
        ax[1] -> creep depth fit
        ax[2] -> hardness during creep
  """
  # Creep model function: logarithmic creep behavior
  # h(t) = a * log(t + t0) + h0
  def creep_func(t, a, h0, t0):
    return a * np.log(t+t0) + h0
  # Derivative of creep function dh/dt
  # Used to calculate creep rate
  def derivate(t, a, h0, t0):
    return a/(t+t0)
  # --------- CASE 1: Continuous Stiffness Measurement (CSM) ---------
  if self.method == Method.CSM:
    # Correct thermal drift and obtain smoothed depth and stiffness
    t, p, h_smooth_solutions, slope_duringCreep_smooth = correctThermalDrift_assumingConstantE(indentation=self)
    try:
      params,_=curve_fit(creep_func, t, h_smooth_solutions, #pylint: disable=unbalanced-tuple-unpacking
                          bounds=([0, 0, -np.min(t)], [10, np.max(h_smooth_solutions)*10, -np.min(t)+10000]),
                          maxfev=100000
                          )
    except:
      print("**ERROR: CalculateCreepRate")
    else:
      # Calculate fitted creep depth
      h_cal1 = creep_func(t, *params)
      # Compute creep rate: (dh/dt) / h
      self.CreepRate = derivate(t, *params)/h_cal1 # /s
      # Calculate contact depth
      hc_cal1 = h_cal1 - 0.75*p/slope_duringCreep_smooth
      # Calculate contact area using tip area function
      Ac_cal1 = self.tip.areaFunction(hc_cal1)
      # Hardness during creep
      self.hardness_duringCreep = p/Ac_cal1
      # Store time array during creep
      self.time_duringCreep = t
      # Optional plotting: fitted creep depth
      if ax[1]:
        t_new = np.arange(np.min(t), np.max(t)+1, 1)
        h_cal2 = creep_func(t_new, *params)
        ax[1].plot(t_new,h_cal2*1000,color='tab:orange', zorder=5,label='fitted creep depth')
      # Optional plotting: hardness evolution
      if ax[2]:
        ax[2].plot(t, self.hardness_duringCreep, alpha=1,color='tab:orange',zorder=5,
                    label="using fitted creep depth\n+ denoised cont. dyn. stiffness",
                    picker=True, )
  # --------- CASE 2: MULTI-CYCLE INDENTATION ---------
  elif self.method == Method.MULTI:
    # Store creep rate for each cycle
    self.CreepRate = []
    # Initialize mask for selecting creep segments
    mask = np.zeros_like(self.h, dtype=bool)
    # Loop over all loading/unloading cycles
    for _, cycle in enumerate(self.iLHU):
      loadStart, loadEnd, unloadStart, unloadEnd = cycle #!!!!!!
      # Check if indices are ordered correctly
      if loadStart>loadEnd or loadEnd>unloadStart or unloadStart>unloadEnd:
        print('*ERROR* stiffnessFromUnloading: indicies not in order:',cycle)
      # Reset mask
      mask = np.zeros_like(self.h, dtype=bool)
      # Select time window for creep segment
      mask[loadEnd+int((unloadStart-loadEnd)*0)+10:unloadStart] = True
      # Extract time and depth
      t = self.t[mask]
      h = self.h[mask]
      # Remove invalid values
      valid = np.isfinite(t) & np.isfinite(h)
      t = t[valid]
      h = h[valid]
      try:
        # Fit creep model
        params, _=curve_fit(creep_func, t, h,               #pylint: disable=unbalanced-tuple-unpacking
                          bounds=([0, 0, 0, 0], [np.inf, 1, np.inf, np.inf]),
                          maxfev=100000
                          )
      except:
        # If fitting fails -> fallback to linear fitting
        print(f"Error with cycle {cycle}: using linear fitting")
        length = len(t)
        # Linear fit on second half of the creep segment
        popt = np.polyfit(t[-int(length/2):],h[-int(length/2):], 1)
        # Linear creep rate estimate
        CreepRate = popt[0]/h[-1]
        self.CreepRate.append(CreepRate) # /s
      else:
         # Calculate creep rate from fitted function
        CreepRate = derivate(t[-1], *params)/h[-1]
        self.CreepRate.append(CreepRate) # /s
        # Optional plot of fitted creep curve
        if ax[1]:
          t_new = np.arange(np.min(t), np.max(t)+1, 1)
          h_cal2 = creep_func(t_new, *params)
          ax[1].plot(t_new,h_cal2*1000,color='orange')
  return
