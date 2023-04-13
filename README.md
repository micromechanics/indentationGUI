# Install
``` bash
pip install micromechanics-indentationGUI
```
# Usage
``` bash
python micromechanics-indentationGUI
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
