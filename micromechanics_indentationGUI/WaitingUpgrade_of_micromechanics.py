""" Module temporarily used to replace the corresponding Module in micromechanics waited to be upgraded """
import pandas as pd
import numpy as np
from micromechanics import indentation
from micromechanics.indentation.definitions import Method
from .Tools4hdf5 import convertXLSXtoHDF5

class IndentationXXX(indentation.Indentation):
  """
  based on the Main class of micromechanics.indentation
  """
  def loadAgilent(self, fileName):
    """
    replacing loadAgilent in micromechanics.indentation

    Initialize G200 excel file for processing

    Args:
      fileName (str): file name

    Returns:
      bool: success
    """
    self.testList = []
    self.fileName = fileName    #one file can have multiple tests
    slash='\\'
    if '/' in fileName:
      slash ='/'
    index_path_end = [i for i,c in enumerate(fileName) if c==slash][-1]
    thePath = fileName[:index_path_end]
    index_file_end = [i for i,c in enumerate(fileName) if c=='.'][-1]
    theFile = fileName[index_path_end+1:index_file_end]
    # try to open hdf5-file, if not convert .xlsx to .h5
    try:
      self.datafile = pd.HDFStore(f"{thePath}{slash}{theFile}.h5", mode='r')
      if self.output['progressBar'] is not None:
        self.output['progressBar'](100,'convert')  # pylint: disable=not-callable
    except:
      if '.xlsx' in fileName:
        convertXLSXtoHDF5(XLSX_File=fileName,progressbar=self.output['progressBar'])
      else:
        print(f"**ERROE: {fileName} is not an XLSX File")
    # read converted .hf5
    self.datafile = pd.HDFStore(f"{thePath}{slash}{theFile}.h5", mode='r')
    self.indicies = {}
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
    self.fullData = ['h','p','t','pVsHSlope','hRaw','pRaw','tTotal','slopeSupport']
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
              self.method = Method.CSM
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
    self.allTestList =  list(self.testList)
    self.nextTest()
    return True
