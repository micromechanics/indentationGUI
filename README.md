<h2 align = "center">
micromechanics-indentationGUI
</h2>
<p align="center">
  <img
  src="https://raw.githubusercontent.com/micromechanics/indentationGUI/main/micromechanics_indentationGUI/logo.png" 
  width="314"
  title="micromechanics-indentationGUI" >
</p>

# Install
- Create a new environment (python >= 3.8) using **anaconda-navigator** (https://www.anaconda.com/). In Anaconda's documentation (https://docs.anaconda.com/free/navigator/) you will learn:
  - how to **install** anaconda-navigator in the section of "*Anaconda Navigator* => *Installation*" (reading takes ~5 min), 
  - how to **create and activate** a new environment in the section of "*Anaconda Navigator* => *Tutorials* => *How to create a Python 3.5 environment from Anaconda2 or Anaconda3*" (reading takes ~5 min).

- In the terminal of the environment created by Anaconda Navigator, keyboard type the following command and press Enter
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
- For fast reading using **HDF5** files:
  - Using the given original file (e.g. the XLSX file for G200X), the HDF5 file will be automatically generated at the first calibration/calculation (or when an HDF5 file with the same name as the XLSX file does not exist).
  - The automatically generated HDF5 file has the same file name as the original file (e.g. the XLSX file for G200X) except the file extension of ".h5" and locates in the same folder as the original file.
  - The original file extension (e.g. '.xlsx' for G200X) should be given in the path instead of the file extension of the HDF5 file (".h5").
  - **[Important]** If you changed the content of the original file, please delete the correspoding HDF5 file.

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
- Delete RecentFiles.txt in /indentationGUI/micromechanics_indentationGUI

- Delete *.hf in /indentationGUI/micromechanics_indentationGUI/Examples

- Set "# pylint: skip-file" for all files named "***_ui.py"

- Test the code: linting, documentation and then the tests from the project's main directory
``` bash
pylint micromechanics_indentationGUI/
make -C docs html
# python tests/testVerification.py
```

Then upload/create-pull-request to GitHub, via
``` bash
./commit.py 'my message'
```
