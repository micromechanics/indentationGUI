""" Module temporarily used to replace the corresponding Module in micromechanics waited to be upgraded """

#pylint: disable=line-too-long, unsubscriptable-object, invalid-unary-operand-type, access-member-before-definition, attribute-defined-outside-init

import math, traceback, io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.ndimage import gaussian_filter1d
from scipy import ndimage
from scipy.optimize import curve_fit
from micromechanics import indentation
from micromechanics.indentation.definitions import Method, Vendor
from .CorrectThermalDrift import correctThermalDrift
from .Tools4hdf5 import convertXLSXtoHDF5
from .load_depth import pick

class IndentationXXX(indentation.Indentation):
  """
  based on the Main class of micromechanics.indentation

  Functions modified based on functions of micromechanics.indentation:
    -analyse
    -nextTest
    -identifyLoadHoldUnload
    -loadAgilent
    -nextAgilentTest
    -nextMicromaterialsTest
    -stiffnessFromUnloading
    -calibrateStiffness

  new Funtions:
    -parameters_for_GUI

  """
  from .calibration_iterativeMethod import calibrateStiffness_iterativeMethod, calibrateStiffness_OneIteration, calibrateTAF, oneIteration_TAF_frameCompliance, calibrate_TAF_and_FrameStiffness_iterativeMethod

  def parameters_for_GUI(self): # !!!!!!
    """
    intinally define parameters for GUI
    """
    self.IfTermsGreaterThanZero = 0  #pylint: disable=attribute-defined-outside-init

  def analyse(self):
    """
    update slopes/stiffness, Young's modulus and hardness after displacement correction by:

    - compliance change

    ONLY DO ONCE AFTER LOADING FILE: if this causes issues introduce flag analysed
      which is toggled during loading and analysing
    """
    self.h -= self.tip.compliance*self.p
    if self.method == Method.CSM:
      if len(self.slope) == len(self.valid):                            #!!!!!!
        self.slope = 1./(1./self.slope[self.valid]-self.tip.compliance) #!!!!!!
      else:                                                             #!!!!!!
        self.slope = 1./(1./self.slope-self.tip.compliance)             #!!!!!!
    else:
      self.slope, self.valid, _, _ , _= self.stiffnessFromUnloading(self.p, self.h)
      self.slope = np.array(self.slope)
    try:
      self.k2p = self.slope*self.slope/self.p[self.valid]
    except:
      print('**WARNING SKIP ANALYSE')
      print(traceback.format_exc())
      return
    #Calculate Young's modulus
    self.calcYoungsModulus()
    self.calcHardness()
    self.saveToUserMeta()
    return

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
        nans = np.isnan(thresValues) #pylint:disable=used-before-assignment
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
          surface  = np.where(thresValues<thresValue)[0][0]  #pylint:disable=used-before-assignment
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
        self.valid = np.logical_and(self.valid, self.h>=0) #!!!!!
        self.identifyLoadHoldUnload() #!!!!!:Different from micromechanics: moved from nextAgilentTest
    #correct thermal drift !!!!!
    if self.model['driftRate']:
      correctThermalDrift(indentation=self,reFindSurface=True)
      self.model['driftRate'] = True
    return success

  def identifyLoadHoldUnload(self,plot=False):
    """
    internal method: identify ALL load - hold - unload segments in data

    Args:
        plot (bool): verify by plotting

    Returns:
        bool: success of identifying the load-hold-unload
    """
    if self.method==Method.CSM:
      success = self.identifyLoadHoldUnloadCSM()
      return success
    #use force-rate to identify load-hold-unload
    if self.model['relForceRateNoiseFilter']=='median':
      p = signal.medfilt(self.p, 5)
    else:
      p = gaussian_filter1d(self.p, 5)
    rate = np.gradient(p, self.t)
    rate /= np.max(rate)
    loadMask  = np.logical_and(rate >  self.model['relForceRateNoise'], p>self.model['forceNoise'])
    unloadMask= np.logical_and(rate < -self.model['relForceRateNoise'], p>self.model['forceNoise'])
    if plot:     # verify visually
      plt.plot(rate)
      plt.axhline(0, c='k')
      plt.axhline( self.model['relForceRateNoise'], c='k', linestyle='dashed')
      plt.axhline(-self.model['relForceRateNoise'], c='k', linestyle='dashed')
      if plot:
        plt.ylim([-8*self.model['relForceRateNoise'], 8*self.model['relForceRateNoise']])
      plt.xlabel('time incr. []')
      plt.ylabel(r'rate [$\mathrm{mN/sec}$]')
      plt.title('Identify load, hold, unload: loading and unloading segments - prior to cleaning')
      plt.show()
    #try to clean small fluctuations
    if len(loadMask)>100 and len(unloadMask)>100:
      size = self.model['maxSizeFluctuations']
      loadMaskTry = ndimage.binary_closing(loadMask, structure=np.ones((size,)) )
      unloadMaskTry = ndimage.binary_closing(unloadMask, structure=np.ones((size,)))
      loadMaskTry = ndimage.binary_opening(loadMaskTry, structure=np.ones((size,)))
      unloadMaskTry = ndimage.binary_opening(unloadMaskTry, structure=np.ones((size,)))
    if np.any(loadMaskTry) and np.any(unloadMaskTry):
      loadMask = loadMaskTry
      unloadMask = unloadMaskTry
    # verify visually
    if plot or self.output['plotLoadHoldUnload']:
      if self.output['ax'] is None:
        fig, ax = plt.subplots(2,1, sharex=True, gridspec_kw={'hspace':0})
      ax[0].plot(rate)
      ax[0].axhline(0, c='k')
      x_ = np.arange(len(rate))[loadMask]
      y_ = np.zeros_like(rate)[loadMask]
      ax[0].plot(x_, y_, 'C1.', label='load mask')
      x_ = np.arange(len(rate))[unloadMask]
      y_ = np.zeros_like(rate)[unloadMask]
      ax[0].plot(x_, y_, 'C2.', label='unload mask')
      ax[0].axhline( self.model['relForceRateNoise'], c='k', linestyle='dashed')
      ax[0].axhline(-self.model['relForceRateNoise'], c='k', linestyle='dashed')
      ax[0].set_ylim([-8*self.model['relForceRateNoise'], 8*self.model['relForceRateNoise']])
      ax[0].legend()
      ax[0].set_ylabel(r'rate [$\mathrm{mN/sec}$]')
    #find index where masks are changing from true-false
    loadMask  = np.r_[False,loadMask,False] #pad with false on both sides
    unloadMask= np.r_[False,unloadMask,False]
    loadIdx   = np.flatnonzero(loadMask[1:]   != loadMask[:-1])
    unloadIdx = np.flatnonzero(unloadMask[1:] != unloadMask[:-1])
    if len(unloadIdx) == len(loadIdx)+2 and np.all(unloadIdx[-4:]>loadIdx[-1]):
      #for drift: partial unload-hold-full unload
      unloadIdx = unloadIdx[:-2]
    while len(unloadIdx) < len(loadIdx) and loadIdx[2]<unloadIdx[0]:
      #clean loading front
      loadIdx = loadIdx[2:]

    if plot or self.output['plotLoadHoldUnload']:     # verify visually
      ax[1].plot(self.p,'o')
      ax[1].plot(p, 's')
      ax[1].plot(loadIdx[::2],  self.p[loadIdx[::2]],  'o',label='load',markersize=12)
      ax[1].plot(loadIdx[1::2], self.p[loadIdx[1::2]], 'o',label='hold',markersize=10)
      ax[1].plot(unloadIdx[::2],self.p[unloadIdx[::2]],'o',label='unload',markersize=8)
      try:
        ax[1].plot(unloadIdx[1::2],self.p[unloadIdx[1::2]],'o',label='unload-end',markersize=6)
      except IndexError:
        pass
      ax[1].legend(loc=0)
      ax[1].set_xlabel(r'time incr. []')
      ax[1].set_ylabel(r'force [$\mathrm{mN}$]')
      fig.tight_layout()
      if self.output['ax'] is None:
        plt.show()
    #store them in a list [[loadStart1, loadEnd1, unloadStart1, unloadEnd1], [loadStart2, loadEnd2, unloadStart2, unloadEnd2],.. ]
    self.iLHU = [] #pylint:disable=attribute-defined-outside-init
    if len(loadIdx) != len(unloadIdx):
      print("**ERROR: Load-Hold-Unload identification did not work",loadIdx, unloadIdx  )
    else:
      self.output['successTest'].append(self.testName)
    try:
      for i,_ in enumerate(loadIdx[::2]):
        if loadIdx[::2][i] < loadIdx[1::2][i] <= unloadIdx[::2][i] < unloadIdx[1::2][i]:
          newEntry = [loadIdx[::2][i],loadIdx[1::2][i],unloadIdx[::2][i],unloadIdx[1::2][i]]
          if np.min(newEntry)>0 and np.max(newEntry)<=len(self.h): #!!!!!!
            self.iLHU.append(newEntry)
          else:
            print("**ERROR: iLHU values out of bounds", newEntry,' with length',len(self.h))
            if len(self.iLHU)>0:
              self.iLHU.append([])
        else:
          print("**ERROR: some segment not found", loadIdx[::2][i], loadIdx[1::2][i], unloadIdx[::2][i], unloadIdx[1::2][i])
          if len(self.iLHU)>0:
            self.iLHU.append([])
    except:
      print("**ERROR: load-unload-segment not found")
      self.iLHU = [] #pylint:disable=attribute-defined-outside-init
    if len(self.iLHU)>1:
      self.method=Method.MULTI #pylint:disable=attribute-defined-outside-init
    #drift segments: only add if it makes sense
    try:
      iDriftS = unloadIdx[1::2][-1]+1
      iDriftE = len(self.p)-1
      if iDriftS+1>iDriftE:
        iDriftS=iDriftE-1
      self.iDrift = [iDriftS,iDriftE] #pylint:disable=attribute-defined-outside-init
    except:
      self.iDrift = [-1,-1] #pylint:disable=attribute-defined-outside-init
    return True

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
    #read sheet of 'Results' #!!!!!!
    self.code_Results = {"X_Position": "X_Position", "Y_Position": "Y_Position"} #!!!!!! #pylint:disable=attribute-defined-outside-init
    self.workbook_Results = None #!!!!!!#pylint:disable=attribute-defined-outside-init
    self.X_Position=None #!!!!!!#pylint:disable=attribute-defined-outside-init
    self.Y_Position=None #!!!!!!#pylint:disable=attribute-defined-outside-init
    for sheetName in ['Results']: #!!!!!!
      try: #!!!!!!
        self.workbook_Results = self.datafile.get(sheetName) #!!!!!!#pylint:disable=attribute-defined-outside-init
        for cell in self.workbook_Results.columns: #!!!!!!
          if cell in self.code_Results: #!!!!!!
            self.indicies[self.code_Results[cell]] = cell #!!!!!!
        break #!!!!!!
      except: #!!!!!!
        pass #do nothing; #!!!!!!
    self.length_indicies_after_readingResults=len(self.indicies) #!!!!!!#pylint:disable=attribute-defined-outside-init
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
        if len(self.indicies)==self.length_indicies_after_readingResults:               #find index of colums for load, etc #!!!!!!
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
      if index not in self.code_Results: #!!!!!!
        data = np.array(df[self.indicies[index]][1:-1], dtype=np.float64) #!!!!!!
        mask = np.isfinite(data) #!!!!!!
        mask[mask] = data[mask]<1e99 #!!!!!!
        self.valid = np.logical_and(self.valid, mask)  #adopt/reduce mask continously # pylint: disable=attribute-defined-outside-init #!!!!!!
    #Run through all items again and crop to only valid data
    for index in self.indicies:  #pylint: disable=consider-using-dict-items
      if index in self.code_Results: #!!!!!!
        testNumber = int(self.testName[5:]) #!!!!!!
        data = self.workbook_Results[self.indicies[index]][testNumber] #!!!!!!
        setattr(self, index, data) #!!!!!!
      elif index not in self.code_Results: #!!!!!!
        data = np.array(df[self.indicies[index]][1:-1], dtype=np.float64) #!!!!!!
        if not index in self.fullData: #!!!!!!
          data = data[self.valid] #!!!!!!
        else: #!!!!!!
          data = data[validFull] #!!!!!!
        setattr(self, index, data) #!!!!!!

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


  def nextMicromaterialsTest(self, newTest=True):
    """
    Go to next file in zip or hdf5-file

    Returns:
        bool: success of going to next sheet
    """
    if self.vendor!=Vendor.Micromaterials: #cannot be used
      return False
    if len(self.testList)==0: #no sheet left
      return False
    if newTest: #!!!!!!
      self.testName = self.testList.pop(0) # pylint: disable=attribute-defined-outside-init
    myFile = self.datafile.open(self.testName) #pylint: disable=assignment-from-no-return
    txt = io.TextIOWrapper(myFile, encoding="utf-8")
    success = self.loadMicromaterials(txt)
    return success


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


  def stiffnessFromUnloading(self, p, h, plot=False, win=False): #!!!!!!
    """
    Calculate single unloading stiffness from Unloading; see G200 manual, p7-6

    Args:
        p (np.array): vector of forces
        h (np.array): vector of depth
        plot (bool): plot results
        win (Class): main_window #!!!!!!
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
      if win: #!!!!!!
        try: #!!!!!!
          loadStart, loadEnd, unloadStart, unloadEnd = cycle #!!!!!!
        except Exception as e: #!!!!!! # pylint:disable=broad-except
          suggestion = 'Try setting the "max. Size of fluctuation" to a vlaue greater than 10.' #!!!!!!
          win.show_error(str(e), suggestion) #!!!!!!
      else: #!!!!!!
        loadStart, loadEnd, unloadStart, unloadEnd = cycle #!!!!!!
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
    testNameAll=[]
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
          testNameAll = np.append( testNameAll, [self.testName] * len(self.slope), axis=0 )
          mask = (t < self.t[self.iLHU[0][1]]) #pylint: disable = superfluous-parens
        elif np.count_nonzero(self.valid)>0:
          x = np.hstack((x,    1./np.sqrt(self.p[self.valid]-np.min(self.p[self.valid])+0.001) ))
          y = np.hstack((y,    1./self.slope))
          h = np.hstack((h, self.h[self.valid]))
          t = self.t[self.valid]
          testNameAll = np.append( testNameAll, [self.testName] * len(self.slope), axis=0 )
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
          testNameAll = np.append( testNameAll, [self.testName] * len(self.metaUser['pMax_mN']), axis=0 )
        else:
          pAll = pAll+[self.metaUser['pMax_mN']]
          hAll = hAll+[self.metaUser['hMax_um']]
          sAll = sAll+[self.metaUser['S_mN/um']]
          testNameAll = np.append( testNameAll, [self.testName] * len(self.metaUser['pMax_mN']), axis=0 )
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
      for _, testName in enumerate(self.allTestList):
        mask1 = np.where(testNameAll[~mask]==testName)
        ax.plot(x[~mask][mask1], y[~mask][mask1], 'o', color='#165480', fillstyle='none', markersize=1, label=f"{testName}", picker=True)
        mask2 = np.where(testNameAll[mask]==testName)
        ax.plot(x[mask][mask2], y[mask][mask2],   'C0o', markersize=5, label=f"{testName}", picker=True)
      y_fitted = np.polyval(param, x[mask]) # !!!!!!
      error = (y_fitted - y[mask]) / y[mask] *100 # !!!!!!
      x_ = np.linspace(0, np.max(x)*1.1, 50)
      y_ = np.polyval(param, x_)
      ax.plot(x_,y_,'w-')
      ax.plot(x_,y_,'C0--')
      ax.plot([0,np.min(x)/2],[frameCompliance,frameCompliance],'k')
      ax.text(np.min(x)/2,frameCompliance,'frame compliance')
      ax.set_ylabel(r"total compliance, $C_{\rm total}$ [$\mathrm{\mu m/mN}$]")
      #ax.legend(loc=4)
      #pick the label of datapoints
      ax.figure.canvas.mpl_connect("pick_event", pick)
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


  def popIn(self, correctH=True, plot=True, removeInitialNM=2.):
    """
    Search for pop-in by jump in depth rate

    Certainty:

    - deltaSlope: higher is better (difference in elastic - plastic slope). Great indicator
    - prefactor: higher is better (prefactor of elastic curve). Great indicator
    - secondRate: lower is better (height of second largest jump). Nice indicator 0.25*deltaRate
    - covElast: lower is better. bad indicator
    - deltaH: higher is better (delta depth in jump). bad indicator
    - deltaRate: higher is better (depth rate during jump). bad indicator

    Future: iterate over largest, to identify best

    Args:
      correctH (bool): correct depth such that curves aligned
      plot (bool): plot pop-in curve
      removeInitialNM (float): remove initial nm from data as they have large scatter

    Returns:
      list: pop-in force, dictionary of certainty
    """
    maxPlasticFit = 150
    minElasticFit = 0.01

    mask = (self.h[self.valid]-np.min(self.h[self.valid]))  >removeInitialNM/1.e3
    h = self.h[self.valid][mask]
    p = self.p[self.valid][mask]
    h = h[:np.argmax(p)] #!!!!!!
    p = p[:np.argmax(p)] #!!!!!!
    depthRate = h[1:]-h[:-1]
    x_        = np.arange(len(depthRate))
    fits      = np.polyfit(x_,depthRate,2)  #substract 2nd order fit b/c depthRate increases over time
    depthRate-= np.polyval(fits,x_)
    iJump     = np.argmax(depthRate)
    iMax      = min(np.argmax(p), iJump+maxPlasticFit)      #max for fit: 150 data-points or max. of curve
    iMin      = np.min(np.where(p>minElasticFit))
    print(iJump, iMax)
    fitPlast  = np.polyfit(h[iJump+1:iMax],p[iJump+1:iMax],2) #does not have to be parabola, just close fit
    slopePlast= np.polyder(np.poly1d(fitPlast))(h[iJump+1] )
    def funct(depth, prefactor, h0):
      diff           = depth-h0
      if isinstance(diff, np.float64):
        diff = max(diff,0.0)
      else:
        diff[diff<0.0] = 0.0
      return prefactor* (diff)**(3./2.)
    fitElast, pcov = curve_fit(funct, h[iMin:iJump], p[iMin:iJump], p0=[100.,0.])    # pylint: disable=unbalanced-tuple-unpacking
    slopeElast= (funct(h[iJump],*fitElast) - funct(h[iJump]*0.9,*fitElast)) / (h[iJump]*0.1)
    fPopIn    = p[iJump]
    certainty = {"deltaRate":depthRate[iJump], "prefactor":fitElast[0], "h0":fitElast[1], \
                  "deltaSlope": slopeElast-slopePlast, 'deltaH':h[iJump+1]-h[iJump],\
                  "covElast":pcov[0,0] }
    listDepthRate = depthRate.tolist()
    iJump2 = np.argmax(listDepthRate)
    while (iJump2-iJump)<3:
      del listDepthRate[iJump2]
      iJump2 = np.argmax(listDepthRate)
    certainty["secondRate"] = np.max(listDepthRate)
    if plot:
      _, ax1 = plt.subplots()
      ax2 = ax1.twinx()
      ax1.plot(self.h,self.p)
      h_ = np.linspace(self.h[iJump+1],self.h[iMax])
      ax1.plot(h_, np.polyval(fitPlast,h_))
      ax1.plot(self.h[iMin:iJump], funct(self.h[iMin:iJump],*fitElast))
      ax2.plot(h[:-1],depthRate,'r')
      ax1.axvline(h[iJump], color='k', linestyle='dashed')
      ax1.axhline(fPopIn, color='k', linestyle='dashed')
      ax1.set_xlim(right=4.*self.h[iJump])
      ax1.set_ylim(top=4.*self.p[iJump], bottom=0)
      plt.show()
    if correctH:
      self.h -= certainty["h0"]
    return fPopIn, certainty
