# pylint: skip-file
""" Module for tools for hdf5 """
import pickle

class data4save:
  """ Module for saving all things in a file """
  def __init__(self, fileName=False):
    self.tabTAF = {
                    'Materials Name': None,
                    'Materials Youngs Modulus': None,
                    'Materials Poissons ratio': None,
                    'Materials Path': None,
                    'Tips Name': None,
                    'Tips Youngs Modulus': None,
                    'Tips Poissons ratio': None,
                    'Number of Terms used for TAF': None,
                    'Number of Terms used for TAF': None,
                  }

def SAVE(self):
  data = data4save()
  data.tabTAF['Materials Name'] = self.ui.lineEdit_MaterialName_tabTAF.text()
  self.i_tabTAF.output['progressBar'] = None
  data.tabTAF['i_tabTAF'] = self.i_tabTAF

  # open a file, where you ant to store the data
  file = open('important', 'wb')
  # dump information to that file
  pickle.dump(data, file)
  # close the file
  file.close()

  # open a file, where you stored the pickled data
  file = open('important', 'rb')
  # dump information to that file
  data = pickle.load(file)
  print(data.tabTAF)
  # close the file
  file.close()
