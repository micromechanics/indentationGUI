""" Using iterative method to calibrate Tip area function (TAF) and frame compliance """

# pylint: disable=line-too-long, invalid-unary-operand-type, missing-param-doc, differing-param-doc, differing-type-doc

import numpy as np
import matplotlib.pyplot as plt
from micromechanics.indentation.definitions import Method
from scipy.signal import savgol_filter # pylint: disable=ungrouped-imports
from scipy.stats import binned_statistic
from scipy import interpolate # pylint: disable=ungrouped-imports
import lmfit

def calibrateStiffness_OneIteration(self, eTarget, critDepths, critForces,plotStiffness=False, returnData=False):
  """
  Calibrate the frame-stiffness using the known Ac=f(hc) according to Eq.(22) in paper of Ovliver 2004

  Args:
    eTarget (float): the targert elastic modulus for the calibration
    critDepths (tuple[float, float]): (min_depth, max_depth) range of data to use.
    critForces (tuple[float, float]): (min_force, max_force) range of data to use.
    plotStiffness (bool): plot stiffness graph with compliance
    returnData (bool): return data for external plotting

  Returns:
    numpy.arary: data as chosen by arguments
  """
  min_depth, max_depth = critDepths
  min_force, max_force = critForces
  if eTarget:
    modulusRedGoal = self.ReducedModulus(eTarget, self.nuMat) #pylint: disable=unused-variable

  self.restartFile()
  testNameAll=[]
  if self.method==Method.CSM:
    x, y, h, t = None, None, None, None
    while True:
      if self.output['progressBar'] is not None:
        self.output['progressBar'](1-len(self.testList)/len(self.allTestList), 'calibrateStiffness') #pylint: disable=not-callable
      self.analyse()
      if x is None:
        x = 1./np.sqrt(self.Ac) #add 1nm:prevent runtime error
        y = 1./self.slope
        h = self.h[self.valid]
        t = self.t[self.valid]
        testNameAll = np.append( testNameAll, [self.testName] * len(self.slope), axis=0 )
        mask = (t < self.t[self.iLHU[0][1]]) #pylint: disable = superfluous-parens
      elif np.count_nonzero(self.valid)>0:
        x = np.hstack(( x, 1./np.sqrt(self.Ac) ))
        y = np.hstack(( y, 1./self.slope ))
        h = np.hstack(( h, self.h[self.valid] ))
        t = self.t[self.valid]
        testNameAll = np.append( testNameAll, [self.testName] * len(self.slope), axis=0 )
        mask = np.hstack((mask, (t < self.t[self.iLHU[0][1]]))) # the section after loading will be removed
      if not self.testList:
        break
      self.nextTest()
    mask &= (h > min_depth) & (h < max_depth)
    mask &= (x<1./np.sqrt(min_force)) & (x>1./np.sqrt(max_force))
    if len(mask[mask])==0:
      # e="WARNING too restrictive filtering, no data left. Use high penetration: 50% of force and depth"
      # suggestion="adjust the range for calculating frame compliance"
      print("WARNING too restrictive filtering, no data left. Use high penetration: 50% of force and depth")
      mask = np.logical_and(h>np.max(h)*0.5, x<np.max(x)*0.5)
  else:
    pAll, hAll, AcAll, sAll = [], [], [], []
    while True:
      print(self.testName)
      if self.output['progressBar'] is not None:
        self.output['progressBar'](1-len(self.testList)/len(self.allTestList), 'calibrateStiffness')
      self.analyse()
      if isinstance(self.metaUser['pMax_mN'], list):
        pAll = pAll+list(self.metaUser['pMax_mN'])
        hAll = hAll+list(self.metaUser['hMax_um'])
        AcAll = AcAll+list(self.metaUser['A_um2'])
        sAll  = sAll +list(self.metaUser['S_mN/um'])
        testNameAll = np.append( testNameAll, [self.testName] * len(self.metaUser['pMax_mN']), axis=0 )
      else:
        pAll = pAll+[self.metaUser['pMax_mN']]
        hAll = hAll+[self.metaUser['hMax_um']]
        AcAll = AcAll+[self.metaUser['A_um2']]
        sAll  = sAll +[self.metaUser['S_mN/um']]
        testNameAll = np.append( testNameAll, [self.testName] * len(self.metaUser['pMax_mN']), axis=0 )
      if not self.testList:
        break
      self.nextTest()
    pAll = np.array(pAll)
    hAll = np.array(hAll)
    AcAll = np.array(AcAll)
    sAll  = np.array(sAll)
    ## determine compliance by intersection of 1/sqrt(Ac) -- compliance curve
    x = 1./np.sqrt(AcAll)
    y = 1./sAll
    mask = (hAll > min_depth) & (hAll < max_depth) & (pAll > min_force) & (pAll < max_force)
    print("number of data-points:", len(x[mask]))
    if len(mask[mask])==0:
      print("ERROR too much filtering, no data left. Decrease critForce and critDepth")
      return None

  if eTarget:
    param, covM = np.polyfit(x[mask],y[mask],1, cov=True) # pylint: disable=unused-variable
    frameStiff = 1./param[1]
    frameCompliance = param[1]
  else:
    param, covM = np.polyfit(x[mask],y[mask],1, cov=True) # pylint: disable=unused-variable
    frameStiff = 1./param[1]
    frameCompliance = param[1]
  print(f"  frame compliance: {frameCompliance:8.4e} um/mN = {frameCompliance/1000.:8.4e} m/N")
  print(f"  frame stiffness: {frameStiff:6.0f} mN/um = {1000.*frameStiff:6.2e} N/m")
  print(f"  tip.compliance: {self.tip.compliance:8.4e} um/mN = {self.tip.compliance/1000.:8.4e} m/N")
  self.tip.compliance = self.tip.compliance + frameCompliance
  print(f"  tip.compliance: {self.tip.compliance:8.4e} um/mN = {self.tip.compliance/1000.:8.4e} m/N")
  print(f"  self.model['driftRate']: {self.model['driftRate']}")
  if plotStiffness or self.output['ax'][0] is not None:
    if plotStiffness:
      _, ax_ = plt.subplots(2,1,sharex=True, gridspec_kw={'hspace':0, 'height_ratios':[4, 1]})
      ax = ax_[0]
      ax1= ax_[1]
    else:
      ax = self.output['ax'][0]
      ax1= self.output['ax'][1]
    for _, testName in enumerate(self.allTestList):
      mask1 = np.where(testNameAll[~mask]==testName)
      ax.plot(x[~mask][mask1], y[~mask][mask1], 'o', color='#165480', fillstyle='none', markersize=1, label=f"{testName}", picker=True)
      mask2 = np.where(testNameAll[mask]==testName)
      ax.plot(x[mask][mask2], y[mask][mask2],   'C0o', markersize=5, label=f"{testName}", picker=True)
    x_ = np.linspace(0, np.max(x)*1.1, 50)
    if eTarget:
      y_ = np.polyval(param, x_)
      y_fitted = np.polyval(param, x[mask])
    else:
      y_ = np.polyval(param, x_)
      y_fitted = np.polyval(param, x[mask])
    error = (y_fitted - y[mask]) / y[mask] *100
    ax.plot(x_,y_,'w-')
    ax.plot(x_,y_,'C0--')
    ax.set_ylabel(r"Contact Compliance, $C_{\rm cont}$[$\mathrm{\mu m/mN}$]")
    ax.set_ylim([0,np.max(y[mask])*1.5])
    ax.set_xlim([0,np.max(x[mask])*1.5])
    ax1.scatter(x[mask], error, color='grey',s=5)
    ax1.set_ylabel(r"$\frac{{\rm fitted} C_{\rm cont} - {\rm meas.} C_{\rm cont}}{{\rm meas.} C_{\rm cont}}x100$ [%]")
    ax1.set_xlabel(r"$\frac{1}{\sqrt{Ac}}$ [$\mathrm{µm^{-1}}$]")
    if plotStiffness:
      plt.show()
  #end of function
  if returnData:
    return x,y
  return frameCompliance


def calibrateStiffness_iterativeMethod(self, eTarget=False, critDepths=(0.5,5), critForces=(0.0001,1000), plotStiffness=False, returnData=False):
  """
  iteratively Calibrate the frame-stiffness using the known Ac=f(hc) according to Eq.(22) in paper of Ovliver 2004

  Args:
    eTarget (float): the targert elastic modulus for the calibration
    critDepths (tuple[float, float]): (min_depth, max_depth) range of data to use.
    critForces (tuple[float, float]): (min_force, max_force) range of data to use.
    plotStiffness (bool): plot stiffness graph with compliance
    returnData (bool): return data for external plotting
  """
  print('start calibrateStiffness_iterativeMethod')
  print(f"the tip.prefactors: {self.tip.prefactors}")
  frameCompliance = self.calibrateStiffness_OneIteration(eTarget=eTarget, critDepths=critDepths, critForces=critForces, plotStiffness=False, returnData=False)
  iteration_numbers=0
  while np.abs(frameCompliance) > 1e-7 and iteration_numbers<21:
    frameCompliance = self.calibrateStiffness_OneIteration(eTarget=eTarget, critDepths=critDepths, critForces=critForces, plotStiffness=False, returnData=False)
    iteration_numbers+=1
    print('iteration_numbers',iteration_numbers)

def calibrateTAF(self,eTarget, frameCompliance, TipType='Berkovich', # pylint:disable=too-many-arguments
                 half_includedAngel_Cone=30, Radius_Sphere=2, numPolynomial=3, critDepthTip=0.0,
                 critMaxDepthTip=1000.0, plotTip=False, plot_Ac_hc=False,
                 DepthStep4UniformDepth=0.01,**kwargs):
  """
  Calibrate the area-function calibration using the known frame stiffness

  Args:
      eTarget (float): target Young's modulus (not reduced), nu is known
      frameCompliance (float): frame compliance
      TipType (string): the type of the tip, e.g. 'Berkovich', 'Cone', 'Sphere'
      half_includedAngel_Cone (float): the included half-angle of a conical tip
      Radius_Sphere (float): the radius of the Sphere, µm
      numPolynomial (int): number of area function polynomial; if None: return interpolation function
      critDepthTip (float): area function what is the minimum depth of data used
      critMaxDepthTip (float): area function what is the maximum depth of data used
      plotTip (bool): plot tip shape after fitting
      plot_Ac_hc (bool): plot the Ac-hc and the fitted function
      DepthStepUniformDepth (float): depth step size to make the Ac-hc data uniform along hc
      kwargs (dict): additional keyword arguments
        - constantTerm (bool): add constant term into area function
        - returnArea (bool): return contact depth and area

  Returns:
    bool: success
  """
  UniformDepth = False
  if self.method==Method.CSM: UniformDepth = True
  constantTerm = kwargs.get('constantTerm', False)
  ## re-create data-frame of all files
  self.restartFile()
  self.tip.compliance = frameCompliance
  slope, h, p = np.array([], dtype=np.float64), np.array([],dtype=np.float64), np.array([],dtype=np.float64)
  NumberOfTests = 0
  if self.method==Method.CSM:
    self.nextTest(newTest=False)  #rerun to ensure that onlyLoadingSegment used
    while True:
      if self.output['progressBar'] is not None:
        self.output['progressBar'](1-len(self.testList)/len(self.allTestList), 'calibration1')
      self.analyse()
      slope = np.hstack((slope, self.slope))
      h     = np.hstack((h,     self.h[self.valid]))
      p     = np.hstack((p,     self.p[self.valid]))
      NumberOfTests += 1
      if not self.testList:
        break
      self.nextTest()
  else:
    while True:
      if self.output['progressBar'] is not None:
        self.output['progressBar'](1-len(self.testList)/len(self.allTestList), 'calibration2')
      self.analyse()
      slope = np.hstack((slope, self.metaUser['S_mN/um']))
      h     = np.hstack((h,     self.metaUser['hMax_um']))
      p     = np.hstack((p,     self.metaUser['pMax_mN']))
      NumberOfTests += 1
      if len(self.testList)==0:
        break
      self.nextTest()

  #the max. depth has to be greater than the given value
  mask = (h>critDepthTip)&(h<critMaxDepthTip)
  slope = slope[mask]
  h = h[mask]
  p = p[mask]

  ## fit shape function
  #reverse OliverPharrMethod to determine area function
  modulusRedGoal = self.ReducedModulus(eTarget, self.nuMat)
  Ac = np.array( np.power( slope  / (2.0*modulusRedGoal/np.sqrt(np.pi))  ,2))  #Eq.(26) Oliver 2004
  hc = np.array( h - self.model['beta']*p/slope )
  #
  bins_ = int((np.max(hc)-np.min(hc))/DepthStep4UniformDepth)
  Ac_mean, bin_edges, _ = binned_statistic(hc, Ac, statistic="mean", bins=bins_)
  Ac_mean = Ac_mean[:-1]
  bin_edges = bin_edges[:-1]
  hc_bin_center = 0.5 * (bin_edges[:-1] + bin_edges[1:])
  if UniformDepth:
    Ac4fit = Ac_mean
    hc4fit = hc_bin_center
  else:
    Ac4fit = Ac
    hc4fit = hc
  #calculate shape function as interpolation of 30 points (log-spacing)
  #  first calculate the  savgol-average using a adaptive window-size
  if numPolynomial is None:
    # use interpolation function using random points
    data = np.vstack((hc,Ac))
    data = data[:, data[0].argsort()]
    windowSize = int(len(Ac)/20) if int(len(Ac)/20)%2==1 else int(len(Ac)/20)-1
    output = savgol_filter(data,windowSize,3)
    interpolationFunct = interpolate.interp1d(output[0,:],output[1,:])
    hc_ = np.logspace(np.log(0.0001),np.log(np.max(output[0,:])),num=50,base=np.exp(1))
    Ac_ = interpolationFunct(hc_)
    interpolationFunct = interpolate.interp1d(hc_, Ac_)
    self.tip.setInterpolationFunction(interpolationFunct)
    del output, data
  else:
    if constantTerm:
      appendix = 'isoPlusConstant'
    else:
      appendix = 'iso'
    def area_from_params(params, hc_vals):
      # Requires a pure function version for best speed.
      # Fallback: temporarily assign to tip object if needed.
      self.tip.prefactors = [params[x].value for x in params] + [appendix]
      return self.tip.areaFunction(hc_vals)
    def fitFunct(params,hc4fit, Ac4fit):     #error function
      tempArea = area_from_params(params, hc4fit)
      # use inhomogenous weight
      # w = 1/Ac4fit
      # w = 1
      w = 1.0 / np.sqrt(np.maximum(Ac4fit, 1e-30))
      # center = 0.5
      # sigma  = 0.08   # 0.08 µm
      # w = 1.0 + 5.0 * np.exp(-0.5*((hc4fit-center)/sigma)**2)  # 0.5 near region has a higher weight
      # residual = (Ac4fit-tempArea) * w  #normalize by number of points
      # residual =  np.log(np.maximum(Ac4fit,1e-30)) - np.log(np.maximum(tempArea,1e-30))
      self.taf_weight_data = {'hc': np.array(hc4fit, copy=True), 'w': np.array(w, copy=True)}
      residual =  (Ac4fit-tempArea) * w
      return residual
    # Parameters, 'value' = initial condition, 'min' and 'max' = boundaries
    params = lmfit.Parameters()
    if TipType=='Berkovich':
      params.add('m0', value= 24.3, min=10.0, max=40.0)
      for idx in range(1,numPolynomial):
        if idx >3:
          startVal = np.power(100,3)
          params.add('m'+str(idx), value= startVal/100, min=-startVal*np.power(10,idx+1)*(1-self.IfTermsGreaterThanZero), max=startVal*np.power(10,idx+1))
        elif idx>1:
          startVal = np.power(100,idx)
          params.add('m'+str(idx), value= startVal/100, min=-startVal*np.power(10,idx+1)*(1-self.IfTermsGreaterThanZero), max=startVal*np.power(10,idx+1))
        else:
          startVal = np.power(100,idx)
          params.add('m'+str(idx), value= startVal/100, min=-startVal*np.power(10,idx+1)*(1-self.IfTermsGreaterThanZero), max=startVal*np.power(10,idx+1))
    elif TipType in ('Cone', 'Sphere+Cone'):
      m0=np.tan(half_includedAngel_Cone/180*np.pi)**2 * np.pi
      params.add('m0', value= m0, min=0.9*m0, max=1.1*m0)
      for idx in range(1,numPolynomial):
        if idx >3:
          startVal = np.power(100,3)
        else:
          startVal = np.power(100,idx)
        params.add('m'+str(idx), value= startVal/100, min=-startVal*1000*(1-self.IfTermsGreaterThanZero), max=startVal*1000)
    elif TipType =='Sphere':
      params.add('m0', value= -np.pi, min=1.5*-np.pi, max=0.5*-np.pi)
      params.add('m1', value= 2*np.pi*Radius_Sphere*1000, min=0.1*2*np.pi*Radius_Sphere*1000, max=1.9*2*np.pi*Radius_Sphere*1000)
      for idx in range(2,numPolynomial):
        startVal = np.power(10,idx)
        params.add('m'+str(idx), value= startVal/100, min=-startVal*500*(1-self.IfTermsGreaterThanZero), max=startVal*500)
    if constantTerm:
      params.add('c',  value= 20, min=0.5, max=300.0) ##all prefactors are in nm, this has to be too
    # do fit, here with leastsq model; args=(hc, Ac)
    result = lmfit.minimize(fitFunct, params,
                            args=(hc4fit, Ac4fit),
                            method='least_squares',
                            loss='huber',     # 'soft_l1' or 'huber' or 'cauchy'
                            f_scale = 0.05,
                            max_nfev=10000)
    self.tip.prefactors = [result.params[x].value for x in result.params]+[appendix]

  if plotTip:
    rNonPerfect = np.sqrt(Ac/np.pi)
    plt.plot(rNonPerfect, hc,'C0o', label='data')
    self.tip.plotIndenterShape(maxDepth=1.5)
    #Error plot
    plt.plot(hc,(Ac-self.tip.areaFunction(hc))/Ac,'o',markersize=2)
    plt.axhline(0,color='k',linewidth=2)
    plt.xlabel(r"Depth [$\mathrm{\mu m}$]")
    plt.ylabel("Relative area error")
    plt.ylim([-0.1,0.1])
    plt.xlim(left=0)
    plt.yticks([-0.1,-0.05,0,0.05,0.1])
    plt.show()

  if plot_Ac_hc:
    _,ax = plt.subplots() #pylint:disable=unused-variable
    ax.scatter(hc,Ac,color='b',label='data')
    if UniformDepth:
      ax.scatter(hc4fit,Ac4fit,color='orange',label='data uniformed along hc',zorder=2)
    hc_new = np.arange(0,hc.max()*1.05,hc.max()/100)
    Ac_new = self.tip.areaFunction(hc_new)
    ax.plot(hc_new,Ac_new,color='r',label='fitted Tip Area Function')
    ax.legend()
    ax.set_xlabel('Contact Depth hc [µm]')
    ax.set_ylabel('Contact Area Ac [µm$^2$]')
  if kwargs.get('returnArea', False):
    return hc, Ac
  return True

def oneIteration_TAF_frameCompliance(self, eTarget, frameCompliance, TipType, half_includedAngel_Cone, Radius_Sphere, numPolynomial, critDepthTip, critMaxDepthTip, constantTerm, critDepthStiffness, critForceStiffness): #pylint: disable=too-many-arguments
  """
  Calibrate the area-function calibration using the known frame stiffness

  Args:
    eTarget (float): target Young's modulus (not reduced), nu is known
    frameCompliance (float): frame compliance
    TipType (string): the type of the tip, e.g. 'Berkovich', 'Cone', 'Sphere'
    half_includedAngel_Cone (float): the included half-angle of a conical tip
    Radius_Sphere (float): the radius of the Sphere, µm
    numPolynomial (int): number of area function polynomial; if None: return interpolation function
    critDepthTip (float): area function: what is the minimum depth of data used
    critMaxDepthTip (float): area function: what is the maximum depth of data used
    constantTerm (bool): wheater to use a constant term for TAF
    critDepthStiffness (tuple[float, float]): (min_depth, max_depth) range of data to use.
    critForceStiffness (tuple[float, float]): (min_force, max_force) range of data to use.

  Returns:
    float: difference of the frame compliance before and after this iteration
  """

  #using frameCompliance to calculate TAF
  hc, Ac = self.calibrateTAF(eTarget=eTarget, frameCompliance = frameCompliance, TipType=TipType, half_includedAngel_Cone=half_includedAngel_Cone,Radius_Sphere=Radius_Sphere, numPolynomial=numPolynomial, critDepthTip=critDepthTip, critMaxDepthTip=critMaxDepthTip, plotTip=False, constantTerm=constantTerm, plot_Ac_hc=False, returnArea=True) # pylint: disable=unused-variable
  #using TAF to calculate frameCompliance
  self.calibrateStiffness_iterativeMethod(eTarget=eTarget, critDepths=critDepthStiffness, critForces=critForceStiffness, plotStiffness=False, returnData=False)
  return (frameCompliance - self.tip.compliance) # pylint: disable=superfluous-parens

def calibrate_TAF_and_FrameStiffness_iterativeMethod(self, eTarget, TipType='Berkovich', half_includedAngel_Cone=30., Radius_Sphere=2, numPolynomial=3, critDepthStiffness=(0,5), critForceStiffness=(0,1000), critDepthTip=0.0, critMaxDepthTip=1000.0, **kwargs): # pylint:disable=too-many-arguments
  """
  iteratively Calibrate the area-function and frame compliance simutaneously according to Eq.(22) in the paper of Oliver 2004

  Args:
    eTarget (float): target Young's modulus (not reduced), nu is known
    TipType (string): the type of the tip, e.g. 'Berkovich', 'Cone', 'Sphere'
    half_includedAngel_Cone (float): the included half-angle of a conical tip
    Radius_Sphere (float): the radius of the Sphere, µm
    numPolynomial (int): number of area function polynomial; if None: return interpolation function
    critDepthStiffness (tuple[float, float]): (min_depth, max_depth) range of data to use.
    critForceStiffness (tuple[float, float]): (min_force, max_force) range of data to use.
    critDepthTip (float): area function: what is the minimum depth of data used
    critMaxDepthTip (float): area function: what is the maximum depth of data used
    kwargs (dict): additional keyword arguments
        - constantTerm (bool): add constant term into area function

  Returns:
    float: difference of the frame compliance before and after this iteration
  """
  self.restartFile()
  constantTerm = kwargs.get('constantTerm', False)
  #calculate the initial frame compliance assuming the constant hardness and elastic modulus
  self.calibrateStiffness(critDepths=critDepthStiffness, critForces=critForceStiffness, plotStiffness=False, returnData=False)
  #Using the assumed frame compliance to calculate the tip area function
  frameCompliance = self.tip.compliance
  Number_of_ChaningBetweenIncreaseDecrease = 0
  change_Value = np.abs( frameCompliance*(0.08/2**Number_of_ChaningBetweenIncreaseDecrease) )
  change_afterIncrease = self.oneIteration_TAF_frameCompliance(frameCompliance=frameCompliance+change_Value, eTarget=eTarget, TipType=TipType, half_includedAngel_Cone=half_includedAngel_Cone, Radius_Sphere=Radius_Sphere, numPolynomial=numPolynomial, critDepthTip=critDepthTip, critMaxDepthTip=critMaxDepthTip, constantTerm=constantTerm, critDepthStiffness=critDepthStiffness, critForceStiffness=critForceStiffness) # pylint: disable=no-name-in-module
  change_afterDecrease = self.oneIteration_TAF_frameCompliance(frameCompliance=frameCompliance-change_Value, eTarget=eTarget, TipType=TipType, half_includedAngel_Cone=half_includedAngel_Cone, Radius_Sphere=Radius_Sphere, numPolynomial=numPolynomial, critDepthTip=critDepthTip, critMaxDepthTip=critMaxDepthTip, constantTerm=constantTerm, critDepthStiffness=critDepthStiffness, critForceStiffness=critForceStiffness) # pylint: disable=no-name-in-module
  Increase_Status = 0
  Decrease_Status = 0
  frameCompliance_Old = frameCompliance
  if np.abs(change_afterDecrease) < np.abs(change_afterIncrease):
    frameCompliance = frameCompliance - change_Value
    Decrease_Status = 1
    change_afterDecreaseORIncrease = np.abs(change_afterDecrease)
  else:
    frameCompliance = frameCompliance + change_Value
    Increase_Status = 1
    change_afterDecreaseORIncrease = np.abs(change_afterIncrease)

  while change_Value > 1e-7:
    change_Value = np.abs( frameCompliance*(0.08/2**Number_of_ChaningBetweenIncreaseDecrease) )
    if Decrease_Status == 1:
      change_afterDecrease = self.oneIteration_TAF_frameCompliance(frameCompliance=frameCompliance-change_Value, eTarget=eTarget, TipType=TipType, half_includedAngel_Cone=half_includedAngel_Cone, Radius_Sphere=Radius_Sphere, numPolynomial=numPolynomial, critDepthTip=critDepthTip, critMaxDepthTip=critMaxDepthTip, constantTerm=constantTerm, critDepthStiffness=critDepthStiffness, critForceStiffness=critForceStiffness)
      if np.abs(change_afterDecrease) <= change_afterDecreaseORIncrease:
        change_afterDecreaseORIncrease = np.abs(change_afterDecrease)
        frameCompliance_Old = frameCompliance
        frameCompliance = frameCompliance - change_Value
        print(f"!!!!!!! frameCompliance is decreased from {frameCompliance_Old} by {change_Value} to: {frameCompliance}")
        print(f"change_afterDecrease: {change_afterDecrease}, change_afterDecreaseORIncrease: {change_afterDecreaseORIncrease}")
      else:
        Decrease_Status = 0
        Increase_Status = 1
        Number_of_ChaningBetweenIncreaseDecrease += 1
        print(f"Number_of_ChaningBetweenIncreaseDecrease: {Number_of_ChaningBetweenIncreaseDecrease}")
    elif Increase_Status == 1:
      change_afterIncrease = self.oneIteration_TAF_frameCompliance(frameCompliance=frameCompliance+change_Value, eTarget=eTarget, TipType=TipType, half_includedAngel_Cone=half_includedAngel_Cone, Radius_Sphere=Radius_Sphere, numPolynomial=numPolynomial, critDepthTip=critDepthTip, critMaxDepthTip=critMaxDepthTip, constantTerm=constantTerm, critDepthStiffness=critDepthStiffness, critForceStiffness=critForceStiffness)
      if np.abs(change_afterIncrease) <= change_afterDecreaseORIncrease:
        change_afterDecreaseORIncrease = np.abs(change_afterIncrease)
        frameCompliance_Old = frameCompliance
        frameCompliance = frameCompliance + change_Value
        print(f"!!!!!!! frameCompliance is increased from {frameCompliance_Old} by {change_Value} to: {frameCompliance}")
        print(f"change_afterIncrease: {change_afterIncrease}, change_afterDecreaseORIncrease: {change_afterDecreaseORIncrease}")
      else:
        Decrease_Status = 1
        Increase_Status = 0
        Number_of_ChaningBetweenIncreaseDecrease += 1
        print(f"Number_of_ChaningBetweenIncreaseDecrease: {Number_of_ChaningBetweenIncreaseDecrease}")

    # #Using the assumed Tip area function to caluclate the frame compliance
    # self.calibrateStiffness_iterativeMethod(eTarget=eTarget, critDepth=critDepthStiffness, critForce=critForceStiffness, plotStiffness=False, returnData=False)
    # frameCompliance_Old.append(frameCompliance)
    # frameCompliance=self.tip.compliance
    # #Using the assumed frame compliance to calculate the tip area function
    # hc, Ac = self.calibrateTAF(eTarget=eTarget, frameCompliance = frameCompliance, TipType=TipType, half_includedAngel_Cone=half_includedAngel_Cone,Radius_Sphere=Radius_Sphere, numPolynomial=numPolynomial, critDepthTip=critDepthTip, plotTip=False, constantTerm=constantTerm, plot_Ac_hc=False, returnArea=True)
    # Ac_max_Old.append(Ac_max)
    # Ac_max = np.max(Ac)
    # # Ac_infiniteMax = self.tip.areaFunction(hc_infiniteMax)[0]
    # print('Ac_max', Ac_max)
    # if frameCompliance > frameCompliance_Old[-1] and Ac_max > Ac_max_Old[-1]:
    #   # if Increase_Status == 1:
    #   #   if frameCompliance_Old[-1] > frameCompliance_Old[-2] and Ac_infiniteMax_Old[-1] > Ac_infiniteMax_Old[-2]:
    #   #     pass
    #   #   else:
    #   #     Func_IF_self_convergence()
    #   #     continue
    #   Increase_Status = 1
    #   if Decrease_Status == 1:
    #     Decrease_Status = 0
    #     Number_of_ChaningBetweenIncreaseDecrease += 1
    #   Decrease_Value = np.abs( frameCompliance_Old[-1]*(0.08/2**Number_of_ChaningBetweenIncreaseDecrease) )
    #   frameCompliance = frameCompliance_Old[-1] - Decrease_Value
    #   print(f"!!!!!!! frameCompliance is decreased from {frameCompliance_Old} by {Decrease_Value}  to: {frameCompliance}")
    #   #Using the assumed frame compliance to calculate the tip area function
    #   hc, Ac = self.calibrateTAF(eTarget=eTarget, frameCompliance = frameCompliance, TipType=TipType, half_includedAngel_Cone=half_includedAngel_Cone,Radius_Sphere=Radius_Sphere, numPolynomial=numPolynomial, critDepthTip=critDepthTip, plotTip=False, constantTerm=constantTerm, plot_Ac_hc=False, returnArea=True)
    #   Ac_max = np.max(Ac)
    #   print('Ac_max', Ac_max)
    # elif frameCompliance < frameCompliance_Old[-1] and Ac_max < Ac_max_Old[-1]:
    #   # if Decrease_Status == 1:
    #   #   if frameCompliance_Old[-1] < frameCompliance_Old[-2] and Ac_infiniteMax_Old[-1] < Ac_infiniteMax_Old[-2]:
    #   #     pass
    #   #   else:
    #   #     Func_IF_self_convergence()
    #   #     continue
    #   Decrease_Status = 1
    #   if Increase_Status == 1:
    #     Increase_Status = 0
    #     Number_of_ChaningBetweenIncreaseDecrease += 1
    #   Increase_Value = np.abs( frameCompliance_Old[-1]*(0.08/2**Number_of_ChaningBetweenIncreaseDecrease) )
    #   frameCompliance = frameCompliance_Old[-1] + Increase_Value
    #   print(f"!!!!!!! frameCompliance is increased from {frameCompliance_Old} by {Increase_Value} to: {frameCompliance}")
    #   hc, Ac = self.calibrateTAF(eTarget=eTarget, frameCompliance = frameCompliance, TipType=TipType, half_includedAngel_Cone=half_includedAngel_Cone,Radius_Sphere=Radius_Sphere, numPolynomial=numPolynomial, critDepthTip=critDepthTip, plotTip=False, constantTerm=constantTerm, plot_Ac_hc=False, returnArea=True)
    #   Ac_max = np.max(Ac)
    #   print('Ac_max', Ac_max)
    # else:
    #   Func_IF_self_convergence()
  return frameCompliance
