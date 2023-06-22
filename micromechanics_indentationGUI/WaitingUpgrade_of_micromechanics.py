""" Module temporarily used to replace the corresponding Module in micromechanics waited to be upgraded """

#pylint: disable=line-too-long, unsubscriptable-object, invalid-unary-operand-type

import math, traceback
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import curve_fit
from micromechanics import indentation
from micromechanics.indentation.definitions import Method, Vendor
from .CorrectThermalDrift import correctThermalDrift
from .Tools4hdf5 import convertXLSXtoHDF5

class IndentationXXX(indentation.Indentation):
  """
  based on the Main class of micromechanics.indentation
  """
  from .calibration_iterativeMethod import calibrateStiffness_iterativeMethod, calibrateStiffness_OneIteration, calibrateTAF, oneIteration_TAF_frameCompliance, calibrate_TAF_and_FrameStiffness_iterativeMethod

  def parameters_for_GUI(self): # !!!!!!
    """
    intinally define parameters for GUI
    """
    self.IfTermsGreaterThanZero = 0  #pylint: disable=attribute-defined-outside-init

  def nextTest(self, newTest=True, plotSurface=False):
    """
    Wrapper for all next test for all vendors

    Args:
      newTest (bool): go to next test; false=redo this one
      plotSurface (bool): plot surface area

    Returns:
      bool: success of going to next sheet
    """
    if newTest:
      if self.vendor == Vendor.Agilent:
        success = self.nextAgilentTest(newTest)
      elif self.vendor == Vendor.Micromaterials:
        success = self.nextMicromaterialsTest()
      elif self.vendor == Vendor.FischerScope:
        success = self.nextFischerScopeTest()
      elif self.vendor > Vendor.Hdf5:
        success = self.nextHDF5Test()
      else:
        print("No multiple tests in file")
        success = False
    else:
      success = True
    #SURFACE FIND
    if self.testName in self.surface['surfaceIdx']:
      surface = self.surface['surfaceIdx'][self.testName]
      self.h -= self.h[surface]  #only change surface, not force
    else:
      found = False
      if 'load' in self.surface:
        thresValues = self.p
        thresValue  = self.surface['load']
        found = True
      elif 'stiffness' in self.surface:
        thresValues = self.slope
        thresValue  = self.surface['stiffness']
        found = True
      elif 'phase angle' in self.surface:
        thresValues = self.phase
        thresValue  = self.surface['phase angle']
        found = True
      elif 'abs(dp/dh)' in self.surface:
        thresValues = np.abs(np.gradient(self.p,self.h))
        thresValue  = self.surface['abs(dp/dh)']
        found = True
      elif 'dp/dt' in self.surface:
        thresValues = np.gradient(self.p,self.t)
        thresValue  = self.surface['dp/dt']
        found = True

      if found:
        #interpolate nan with neighboring values
        nans = np.isnan(thresValues)
        def tempX(z):
          """
          Temporary function

          Args:
            z (numpy.array): input

          Returns:
            numpy.array: output
          """
          return z.nonzero()[0]
        thresValues[nans]= np.interp(tempX(nans), tempX(~nans), thresValues[~nans])

        #filter this data
        if 'median filter' in self.surface:
          thresValues = signal.medfilt(thresValues, self.surface['median filter'])
        elif 'gauss filter' in self.surface:
          thresValues = gaussian_filter1d(thresValues, self.surface['gauss filter'])
        elif 'butterfilter' in self.surface:
          valueB, valueA = signal.butter(*self.surface['butterfilter'])
          thresValues = signal.filtfilt(valueB, valueA, thresValues)
        if 'phase angle' in self.surface:
          surface  = np.where(thresValues<thresValue)[0][0]
        else:
          surface  = np.where(thresValues>thresValue)[0][0]
        if plotSurface or 'plot' in self.surface:
          _, ax1 = plt.subplots()
          ax1.plot(self.h,thresValues, 'C0o-')
          ax1.plot(self.h[surface], thresValues[surface], 'C9o', markersize=14)
          ax1.axhline(0,linestyle='dashed')
          ax1.set_ylim(bottom=0, top=np.percentile(thresValues,80))
          ax1.set_xlabel(r'depth [$\mu m$]')
          ax1.set_ylabel(r'threshold value [different units]', color='C0')
          ax1.grid()
          plt.show()
        self.h -= self.h[surface]  #only change surface, not force
        self.p -= self.p[surface]  #!!!!!:Different from micromechanics: change load
        self.identifyLoadHoldUnload() #!!!!!:Different from micromechanics: moved from nextAgilentTest
    #correct thermal drift !!!!!
    if self.model['driftRate']:
      correctThermalDrift(indentation=self,reFindSurface=True)
      self.model['driftRate'] = True
    return success


  def loadAgilent(self, fileName):
    """
    replacing loadAgilent in micromechanics.indentation

    Initialize G200 excel file for processing

    Args:
      fileName (str): file name

    Returns:
      bool: success
    """
    self.testList = []          # pylint: disable=attribute-defined-outside-init
    self.fileName = fileName    #one file can have multiple tests # pylint: disable=attribute-defined-outside-init
    slash='\\'
    if '/' in fileName:
      slash ='/'
    index_path_end = [i for i,c in enumerate(fileName) if c==slash][-1]
    thePath = fileName[:index_path_end]
    index_file_end = [i for i,c in enumerate(fileName) if c=='.'][-1]
    theFile = fileName[index_path_end+1:index_file_end]
    # try to open hdf5-file, if not convert .xlsx to .h5
    try:
      # read converted .hf5
      self.datafile = pd.HDFStore(f"{thePath}{slash}{theFile}.h5", mode='r') # pylint: disable=attribute-defined-outside-init
      if self.output['progressBar'] is not None:
        self.output['progressBar'](100,'convert')  # pylint: disable=not-callable
    except:
      if '.xlsx' in fileName:
        convertXLSXtoHDF5(XLSX_File=fileName,progressbar=self.output['progressBar'])
        # read converted .hf5
        self.datafile = pd.HDFStore(f"{thePath}{slash}{theFile}.h5", mode='r') # pylint: disable=attribute-defined-outside-init
      else:
        print(f"**ERROE: {fileName} is not an XLSX File")
    self.indicies = {} # pylint: disable=attribute-defined-outside-init
    for sheetName in ['Required Inputs', 'Pre-Test Inputs']:
      try:
        workbook = self.datafile.get(sheetName)
        self.metaVendor.update( dict(workbook.iloc[-1]) )
        break
      except:
        pass #do nothing;
    if 'Poissons Ratio' in self.metaVendor and self.metaVendor['Poissons Ratio']!=self.nuMat and \
        self.output['verbose']>0:
      print("*WARNING*: Poisson Ratio different than in file.",self.nuMat,self.metaVendor['Poissons Ratio'])
    tagged = []
    code = {"Load On Sample":"p", "Force On Surface":"p", "LOAD":"p", "Load":"p"\
          ,"_Load":"pRaw", "Raw Load":"pRaw","Force":"pRaw"\
          ,"Displacement Into Surface":"h", "DEPTH":"h", "Depth":"h"\
          ,"_Displacement":"hRaw", "Raw Displacement":"hRaw","Displacement":"hRaw"\
          ,"Time On Sample":"t", "Time in Contact":"t", "TIME":"t", "Time":"tTotal"\
          ,"Contact Area":"Ac", "Contact Depth":"hc"\
          ,"Harmonic Displacement":"hHarmonic", "Harmonic Load":"pHarmonic","Phase Angle":"phaseAngle"\
          ,"Load vs Disp Slope":"pVsHSlope","d(Force)/d(Disp)":"pVsHSlope", "_Column": "Column"\
          ,"_Frame": "Frame"\
          ,"Support Spring Stiffness":"slopeSupport", "Frame Stiffness": "frameStiffness"\
          ,"Harmonic Stiffness":"slopeInvalid"\
          ,"Harmonic Contact Stiffness":"slope", "STIFFNESS":"slope","Stiffness":"slope" \
          ,"Stiffness Squared Over Load":"k2p","Dyn. Stiff.^2/Load":"k2p"\
          ,"Hardness":"hardness", "H_IT Channel":"hardness","HARDNESS":"hardness"\
          ,"Modulus": "modulus", "E_IT Channel": "modulus","MODULUS":"modulus","Reduced Modulus":"modulusRed"\
          ,"Scratch Distance": "s", "XNanoPosition": "x", "YNanoPosition": "y"\
          ,"X Position": "xCoarse", "Y Position": "yCoarse","X Axis Position":"xCoarse"\
          ,"Y Axis Position":"yCoarse"\
          ,"TotalLateralForce": "L", "X Force": "pX", "_XForce": "pX", "Y Force": "pY", "_YForce": "pY"\
          ,"_XDeflection": "Ux", "_YDeflection": "Uy" }
    self.fullData = ['h','p','t','pVsHSlope','hRaw','pRaw','tTotal','slopeSupport'] # pylint: disable=attribute-defined-outside-init
    if self.output['verbose']>1:
      print("Open Agilent file: "+fileName)
    for _, dfName in enumerate(self.datafile.keys()):
      dfName = dfName[1:]
      df    = self.datafile.get(dfName)
      if "Test " in dfName and not "Tagged" in dfName and not "Test Inputs" in dfName:
        self.testList.append(dfName)
        #print "  I should process sheet |",sheet.name,"|"
        if len(self.indicies)==0:               #find index of colums for load, etc
          for cell in df.columns:
            if cell in code:
              self.indicies[code[cell]] = cell
              if self.output['verbose']>2:
                print(f"     {cell:<30} : {code[cell]:<20} ")
            else:
              if self.output['verbose']>2:
                print(f" *** {cell:<30} NOT USED")
            if "Harmonic" in cell or "Dyn. Frequency" in cell:
              self.method = Method.CSM # pylint: disable=attribute-defined-outside-init
          #reset to ensure default values are set
          if "p" not in self.indicies: self.indicies['p']=self.indicies['pRaw']
          if "h" not in self.indicies: self.indicies['h']=self.indicies['hRaw']
          if "t" not in self.indicies: self.indicies['t']=self.indicies['tTotal']
          #if self.output['verbose']: print("   Found column names: ",sorted(self.indicies))
      if "Tagged" in dfName: tagged.append(dfName)
    if len(tagged)>0 and self.output['verbose']>1: print("Tagged ",tagged)
    if "t" not in self.indicies or "p" not in self.indicies or \
      "h" not in self.indicies:
      print("*WARNING*: INDENTATION: Some index is missing (t,p,h) should be there")
    self.metaUser['measurementType'] = 'MTS, Agilent Indentation XLS'
    #rearrange the testList
    TestNumber_collect=[]
    for _, theTest in enumerate(self.testList):
      TestNumber_collect.append(int(theTest[5:]))
    TestNumber_collect.sort()
    self.testList = [] # pylint: disable=attribute-defined-outside-init
    for theTest in TestNumber_collect:
      self.testList.append(f"Test {theTest}")
    #define allTestList
    self.allTestList =  list(self.testList) # pylint: disable=attribute-defined-outside-init
    self.nextTest()
    return True


  def nextAgilentTest(self, newTest=True):
    """
    Go to next sheet in worksheet and prepare indentation data

    Data:

    - _Raw: without frame stiffness correction,
    - _Frame:  with frame stiffness correction (remove postscript finally)
    - only affects/applies directly depth (h) and stiffness (s)
    - modulus, hardness and k2p always only use the one with frame correction

    Args:
      newTest (bool): take next sheet (default)

    Returns:
      bool: success of going to next sheet
    """
    if self.vendor!=Vendor.Agilent: return False #cannot be used
    if len(self.testList)==0: return False   #no sheet left
    if newTest:
      self.testName = self.testList.pop(0) # pylint: disable=attribute-defined-outside-init

    #read data and identify valid data points
    df     = self.datafile.get(self.testName)
    h       = np.array(df[self.indicies['h'    ]][1:-1], dtype=np.float64)
    validFull = np.isfinite(h)
    if 'slope' in self.indicies:
      slope   = np.array(df[self.indicies['slope']][1:-1], dtype=np.float64)
      self.valid =  np.isfinite(slope) # pylint: disable=attribute-defined-outside-init
      self.valid[self.valid] = slope[self.valid] > 0.0  #only valid points if stiffness is positiv
    else:
      self.valid = validFull # pylint: disable=attribute-defined-outside-init
    for index in self.indicies:  #pylint: disable=consider-using-dict-items
      data = np.array(df[self.indicies[index]][1:-1], dtype=np.float64)
      mask = np.isfinite(data)
      mask[mask] = data[mask]<1e99
      self.valid = np.logical_and(self.valid, mask)  #adopt/reduce mask continously # pylint: disable=attribute-defined-outside-init

    #Run through all items again and crop to only valid data
    for index in self.indicies:  #pylint: disable=consider-using-dict-items
      data = np.array(df[self.indicies[index]][1:-1], dtype=np.float64)
      if not index in self.fullData:
        data = data[self.valid]
      else:
        data = data[validFull]
      setattr(self, index, data)

    self.valid = self.valid[validFull]  # pylint: disable=attribute-defined-outside-init
    #  now all fields (incl. p) are full and defined

    #self.identifyLoadHoldUnload()   #!!!!!Different from micromechanics::Moved to nextTest() after found surface
    #TODO_P2 Why is there this code?
    # if self.onlyLoadingSegment and self.method==Method.CSM:
    #   # print("Length test",len(self.valid), len(self.h[self.valid]), len(self.p[self.valid])  )
    #   iMin, iMax = 2, self.iLHU[0][1]
    #   self.valid[iMax:] = False
    #   self.valid[:iMin] = False
    #   self.slope = self.slope[iMin:np.sum(self.valid)+iMin]

    #correct data and evaluate missing
    self.h /= 1.e3 #from nm in um
    if "Ac" in self.indicies         : self.Ac /= 1.e6  #from nm in um
    if "slope" in self.indicies       : self.slope /= 1.e3 #from N/m in mN/um
    if "slopeSupport" in self.indicies: self.slopeSupport /= 1.e3 #from N/m in mN/um
    if 'hc' in self.indicies         : self.hc /= 1.e3  #from nm in um
    if 'hRaw' in self.indicies        : self.hRaw /= 1.e3  #from nm in um
    if not "k2p" in self.indicies and 'slope' in self.indicies: #pylint: disable=unneeded-not
      self.k2p = self.slope * self.slope / self.p[self.valid] # pylint: disable=attribute-defined-outside-init
    return True


  @staticmethod
  def inverse_unloadingPowerFunc(p,B,hf,m):
    """
    !!!!!!
    internal function describing the unloading regime

    - function: h = (p/B)**(1/m) + hf
    - B:  scaling factor (no physical meaning)
    - m:  exponent       (no physical meaning)
    - hf: final depth = depth where force becomes 0
    """
    value = (p/B)**(1./m) + hf
    return value


  def stiffnessFromUnloading(self, p, h, plot=False):
    """
    Calculate single unloading stiffness from Unloading; see G200 manual, p7-6

    Args:
        p (np.array): vector of forces
        h (np.array): vector of depth
        plot (bool): plot results

    Returns:
        list: stiffness, validMask, mask, optimalVariables, powerlawFit-success |br|
          validMask is [values of p,h where stiffness is determined]
    """
    if self.method== Method.CSM:
      print("*ERROR* Should not land here: CSM method")
      return None, None, None, None, None
    if self.output['verbose']>2:
      print("Number of unloading segments:"+str(len(self.iLHU))+"  Method:"+str(self.method))
    stiffness, mask, opt, powerlawFit = [], None, None, []
    validMask = np.zeros_like(p, dtype=bool)
    if plot:
      if self.output['ax'] is not None:
        ax  = self.output['ax'][0]
        ax2 = self.output['ax'][1]
      elif plot:
        ax_ = plt.subplots(2,1,sharex=True, gridspec_kw={'hspace':0})
        ax  = ax_[0]
        ax2 = ax_[1]
      ax.plot(h,p, '-ok', markersize=3, linewidth=1, label='data') #!!!!!!
    for cycleNum, cycle in enumerate(self.iLHU):
      loadStart, loadEnd, unloadStart, unloadEnd = cycle
      if loadStart>loadEnd or loadEnd>unloadStart or unloadStart>unloadEnd:
        print('*ERROR* stiffnessFromUnloading: indicies not in order:',cycle)
      maskSegment = np.zeros_like(h, dtype=bool)
      maskSegment[unloadStart:unloadEnd+1] = True
      maskForce   = np.logical_and(p<p[loadEnd]*self.model['unloadPMax'], p>p[loadEnd]*self.model['unloadPMin'])
      mask        = np.logical_and(maskSegment,maskForce)
      # mask_evaluateSAtMax = np.logical_and(maskSegment, p>p[loadEnd]*self.model['unloadPMin']) #!!!!!!
      if len(mask[mask])==0:
        print('*ERROR* mask of unloading is empty. Cannot fit\n')
        return None, None, None, None, None
      if plot:
        if cycleNum==0:
          ax.plot(h[mask],p[mask],'ob', label='this cycle') #!!!!!!
        else:
          ax.plot(h[mask],p[mask],'ob') #!!!!!!
      #initial values of fitting
      hf0    = h[mask][-1]/1.1
      m0     = 1.5
      B0     = max(abs(p[mask][0] / np.power(h[mask][0]-hf0,m0)), 0.001)  #prevent neg. or zero
      bounds = [[0,0,0.8],[np.inf, max(np.min(h[mask]),hf0), 10]]
      if self.output['verbose']>2:
        print("Initial fitting values B,hf,m", B0,hf0,m0)
        print("Bounds", bounds)
      # Old linear assumptions
      # B0  = (P[mask][-1]-P[mask][0])/(h[mask][-1]-h[mask][0])
      # hf0 = h[mask][0] - P[mask][0]/B0
      # m0  = 1.5 #to get of axis
      try:
        opt, _ = curve_fit(self.unloadingPowerFunc, h[mask],p[mask],      # pylint: disable=unbalanced-tuple-unpacking
                          p0=[B0,hf0,m0], bounds=bounds,
                           maxfev=1000 )#set ftol to 1e-4 if accept more and fail less
        if self.output['verbose']>2:
          print("Optimal values B,hf,m", opt)
        B,hf,m = opt
        if np.isnan(B):
          raise ValueError("NAN after fitting")
        powerlawFit.append(True)
        calculatedP = self.unloadingPowerFunc(h[mask],B=B,hf=hf,m=m)
        error = (calculatedP-p[mask])/p[mask]*100
        if plot:
          ax2.scatter(h[mask],error,color='gray',s=5)
      except:
        #if fitting fails: often the initial bounds and initial values do not match
        print(traceback.format_exc())
        if self.output['verbose']>0:
          print("stiffnessFrommasking: #",cycleNum," Fitting failed. use linear")
        B  = (p[mask][-1]-p[mask][0])/(h[mask][-1]-h[mask][0])
        hf = h[mask][0] -p[mask][0]/B
        m  = 1.
        opt= (B,hf,m)
        powerlawFit.append(False)
        calculatedP = self.unloadingPowerFunc(h[mask],B=B,hf=hf,m=m)
        error = (calculatedP-p[mask])/p[mask]*100
        if plot:
          ax2.plot(h[mask],error,color='red')
      if self.model['evaluateSAtMax']:
        hmax = self.inverse_unloadingPowerFunc(p=p[loadEnd], B=B, hf=hf, m=m) #!!!!!!
        x_ = np.linspace(0.5*hmax, hmax, 100) #!!!!!!
        stiffnessPlot = B*m*math.pow( h[unloadStart]-hf, m-1)
        # stiffnessValue= p[unloadStart]-stiffnessPlot*h[unloadStart]
        p_unloadStart = self.unloadingPowerFunc(x_[-1],B=B,hf=hf,m=m) #!!!!!!
        stiffnessValue= p_unloadStart-stiffnessPlot*x_[-1] #!!!!!!
        validMask[unloadStart]=True
      else:
        x_ = np.linspace(0.5*h[mask].max(), h[mask].max(), 100)
        stiffnessPlot = B*m*math.pow( (h[mask][0]-hf), m-1)
        stiffnessValue= p[mask][0]-stiffnessPlot*h[mask][0]
        validMask[ np.where(mask)[0][0] ]=True
      stiffness.append(stiffnessPlot)
      if plot:
        if cycleNum==0:
          ax.plot(x_,   self.unloadingPowerFunc(x_,B,hf,m),'m-', label='final fit')
          ax.plot(x_,   self.unloadingPowerFunc(x_,B0,hf0,m0),'g-', label='initial fit')   #!!!!!!
          ax.plot(x_,   stiffnessPlot*x_+stiffnessValue, 'r--', lw=3, label='linear at max')
          ax.axhline(0, linestyle='-.', color='tab:orange', label='zero Load or Depth') #!!!!!!
          ax.axvline(0, linestyle='-.', color='tab:orange') #!!!!!!
        else:
          ax.plot(x_,   self.unloadingPowerFunc(x_,B,hf,m),'m-')
          ax.plot(x_,   self.unloadingPowerFunc(x_,B0,hf0,m0),'g-')   #!!!!!!
          ax.plot(x_,   stiffnessPlot*x_+stiffnessValue, 'r--', lw=3)
    if plot:
      ax.legend()
      ax.set_xlim(left=0-h.max()*0.05)
      ax.set_ylim(bottom=0-p.max()*0.05)
      ax.set_ylabel(r'force [$\mathrm{mN}$]')
      ax2.set_ylabel(r"$\frac{P_{cal}-P_{mea}}{P_{mea}}x100$ [%]")
      ax2.set_xlabel(r'depth [$\mathrm{\mu m}$]')
    if plot and not self.output['ax'][0]:
      plt.show()
    return stiffness, validMask, mask, opt, powerlawFit


  def calibrateStiffness(self,critDepth=0.5,critForce=0.0001,plotStiffness=True, returnData=False):
    """
    Calibrate by first frame-stiffness from K^2/P of individual measurement

    Args:
      critDepth (float): frame stiffness: what is the minimum depth of data used
      critForce (float): frame stiffness: what is the minimum force used for fitting
      plotStiffness (bool): plot stiffness graph with compliance
      returnData (bool): return data for external plotting

    Returns:
      numpy.arary: data as chosen by arguments
    """
    print("Start compliance fitting")
    ## output representative values
    if self.method==Method.CSM:
      x, y, h, t = None, None, None, None
      while True:
        if self.output['progressBar'] is not None:
          self.output['progressBar'](1-len(self.testList)/len(self.allTestList), 'calibrateStiffness') #pylint: disable=not-callable
        self.analyse()
        if x is None:
          x = 1./np.sqrt(self.p[self.valid]-np.min(self.p[self.valid])+0.001) #add 1nm:prevent runtime error
          y = 1./self.slope
          h = self.h[self.valid]
          t = self.t[self.valid]
          mask = (t < self.t[self.iLHU[0][1]]) #pylint: disable = superfluous-parens
        elif np.count_nonzero(self.valid)>0:
          x = np.hstack((x,    1./np.sqrt(self.p[self.valid]-np.min(self.p[self.valid])+0.001) ))
          y = np.hstack((y,    1./self.slope))
          h = np.hstack((h, self.h[self.valid]))
          t = self.t[self.valid]
          mask = np.hstack((mask, (t < self.t[self.iLHU[0][1]]))) # the section after loading will be removed
        if not self.testList:
          break
        self.nextTest()
      mask = np.logical_and(mask, h>critDepth)
      mask = np.logical_and(mask, x<1./np.sqrt(critForce))
      if len(mask[mask])==0:
        print("WARNING too restrictive filtering, no data left. Use high penetration: 50% of force and depth")
        mask = np.logical_and(h>np.max(h)*0.5, x<np.max(x)*0.5)
    else:
      ## create data-frame of all files
      pAll, hAll, sAll = [], [], []
      while True:
        if self.output['progressBar'] is not None:
          self.output['progressBar'](1-len(self.testList)/len(self.allTestList), 'calibrateStiffness') # pylint: disable=not-callable
        self.analyse()
        if isinstance(self.metaUser['pMax_mN'], list):
          pAll = pAll+list(self.metaUser['pMax_mN'])
          hAll = hAll+list(self.metaUser['hMax_um'])
          sAll = sAll+list(self.metaUser['S_mN/um'])
        else:
          pAll = pAll+[self.metaUser['pMax_mN']]
          hAll = hAll+[self.metaUser['hMax_um']]
          sAll = sAll+[self.metaUser['S_mN/um']]
        if not self.testList:
          break
        self.nextTest()
      pAll = np.array(pAll)
      hAll = np.array(hAll)
      sAll = np.array(sAll)
      ## determine compliance by intersection of 1/sqrt(p) -- compliance curve
      x = 1./np.sqrt(pAll)
      y = 1./sAll
      mask = hAll > critDepth
      mask = np.logical_and(mask, pAll>critForce)
      print("number of data-points:", len(x[mask]))
    if len(mask[mask])==0:
      print("ERROR too much filtering, no data left. Decrease critForce and critDepth")
      return None

    param, covM = np.polyfit(x[mask],y[mask],1, cov=True)
    print("fit f(x)=",round(param[0],5),"*x+",round(param[1],5))
    frameStiff = 1./param[1]
    frameCompliance = param[1]
    print(f"  frame compliance: {frameCompliance:8.4e} um/mN = {frameCompliance/1000.:8.4e} m/N")
    stderrPercent = np.abs( np.sqrt(np.diag(covM)[1]) / param[1] * 100. )
    print("  compliance and stiffness standard error in %: "+str(round(stderrPercent,2)) )
    print(f"  frame stiffness: {frameStiff:6.0f} mN/um = {1000.*frameStiff:6.2e} N/m")
    self.tip.compliance = frameCompliance

    if plotStiffness or self.output['ax'][0] is not None: # !!!!!!
      if plotStiffness:
        _, ax_ = plt.subplots(2,1,sharex=True, gridspec_kw={'hspace':0, 'height_ratios':[4, 1]}) #!!!!!!
        ax = ax_[0] #!!!!!!
        ax = ax_[1] #!!!!!!
      else:
        ax = self.output['ax'][0]  #!!!!!!
        ax1= self.output['ax'][1]  #!!!!!!

      ax.plot(x[~mask], y[~mask], 'o', color='#165480', fillstyle='none', markersize=1, label='excluded')
      ax.plot(x[mask], y[mask],   'C0o', markersize=5, label='for fit')
      y_fitted = np.polyval(param, x[mask]) # !!!!!!
      error = (y_fitted - y[mask]) / y[mask] *100 # !!!!!!
      x_ = np.linspace(0, np.max(x)*1.1, 50)
      y_ = np.polyval(param, x_)
      ax.plot(x_,y_,'w-')
      ax.plot(x_,y_,'C0--')
      ax.plot([0,np.min(x)/2],[frameCompliance,frameCompliance],'k')
      ax.text(np.min(x)/2,frameCompliance,'frame compliance')
      ax.set_ylabel(r"total compliance, $C_{\rm total}$ [$\mathrm{\mu m/mN}$]")
      ax.legend(loc=4)
      ax.set_ylim([0,np.max(y[mask])*1.5])
      ax.set_xlim([0,np.max(x[mask])*1.5])
      ax1.scatter(x[mask], error, color='grey',s=5) # !!!!!!
      ax1.set_ylabel(r"$\frac{{\rm fitted} C_{\rm total} - {\rm meas.} C_{\rm total}}{{\rm meas.} C_{\rm total}}x100$ [%]") # !!!!!!
      ax1.set_xlabel(r"$\frac{1}{\sqrt{P}}$ [$\mathrm{mN^{-1/2}}$]") # !!!!!!

      if plotStiffness:
        plt.show()
    #end of function # !!!!!!
    if returnData:
      return x,y
    return frameCompliance
