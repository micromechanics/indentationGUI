""" Module temporarily used to replace the corresponding Module in micromechanics waited to be upgraded """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.ndimage import gaussian_filter1d
from micromechanics import indentation
from micromechanics.indentation.definitions import Method, Vendor
from .CorrectThermalDrift import correctThermalDrift
from .Tools4hdf5 import convertXLSXtoHDF5

class IndentationXXX(indentation.Indentation):
  """
  based on the Main class of micromechanics.indentation
  """
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
      self.testName = self.testList.pop(0)

    #read data and identify valid data points
    df     = self.datafile.get(self.testName)
    h       = np.array(df[self.indicies['h'    ]][1:-1], dtype=np.float64)
    validFull = np.isfinite(h)
    if 'slope' in self.indicies:
      slope   = np.array(df[self.indicies['slope']][1:-1], dtype=np.float64)
      self.valid =  np.isfinite(slope)
      self.valid[self.valid] = slope[self.valid] > 0.0  #only valid points if stiffness is positiv
    else:
      self.valid = validFull
    for index in self.indicies:  #pylint: disable=consider-using-dict-items
      data = np.array(df[self.indicies[index]][1:-1], dtype=np.float64)
      mask = np.isfinite(data)
      mask[mask] = data[mask]<1e99
      self.valid = np.logical_and(self.valid, mask)                       #adopt/reduce mask continously

    #Run through all items again and crop to only valid data
    for index in self.indicies:  #pylint: disable=consider-using-dict-items
      data = np.array(df[self.indicies[index]][1:-1], dtype=np.float64)
      if not index in self.fullData:
        data = data[self.valid]
      else:
        data = data[validFull]
      setattr(self, index, data)

    self.valid = self.valid[validFull]
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
      self.k2p = self.slope * self.slope / self.p[self.valid]
    return True
