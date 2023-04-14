# Install
highly recommend: install in a new environment (python >= 3.8) created by Anaconda (https://www.anaconda.com/)
In the terminal, keyboard type the following command and press Enter
``` bash
pip install micromechanics-indentationGUI
```
# Uninstall
In the terminal, keyboard type the following command and press Enter
``` bash
pip uninstall micromechanics-indentationGUI
```
# Upgrade
In the terminal, keyboard type the following command and press Enter
``` bash
pip install --upgrade micromechanics-indentationGUI
```
# Usage
In the terminal, keyboard type the following command and press Enter
``` bash
micromechanics-indentationGUI
``` 

# More detailed description to developers

# Prepare and create a new version
Test the code: linting, documentation and then the tests from project main directory
``` bash
pylint micromechanics_indentationGUI/
make -C docs html
# python tests/testVerification.py
```

Then upload/create-pull-request to github, via
``` bash
./commit.py 'my message'
```
