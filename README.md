# Install
highly recommend: installing in a new environment (python >= 3.8) created by Anaconda (https://www.anaconda.com/)

In the terminal, keyboard type the following command and press Enter
``` bash
pip install micromechanics-indentationGUI
```
# Upgrade
In the terminal, keyboard type the following command and press Enter
``` bash
pip install --upgrade micromechanics-indentationGUI
```
# Usage
Users need to know:
- For fast reading using HDF5 files:
  - Using the given original file (e.g. the XLSX file for G200X), the HDF5 file will be automatically generated at the first calibration/calculation (or when an HDF5 file with the same name as the XLSX file does not exist).
  - The automatically generated HDF5 file has the same as the original file (e.g. the XLSX file for G200X) but the file extension of ".h5" and locates in the same folder as the original file.
  - The original file extension (e.g. '.xlsx' for G200X) should be given in the path instead of the file extension of the HDF5 file (".h5").

Running by keyboard typing the following command and pressing Enter in the terminal
``` bash
micromechanics-indentationGUI
``` 
# Uninstall
In the terminal, keyboard type the following command and press Enter
``` bash
pip uninstall micromechanics-indentationGUI
```

# More detailed descriptions for developers

# Prepare and create a new version
Test the code: linting, documentation and then the tests from the project's main directory
``` bash
pylint micromechanics_indentationGUI/
make -C docs html
# python tests/testVerification.py
```

Then upload/create-pull-request to GitHub, via
``` bash
./commit.py 'my message'
```
