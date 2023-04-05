# More detailed description to developers

# Prepare and create a new version
Test the code: linting, documentation and then the tests from project main directory
``` bash
pylint micromechanics-indentationGUI/
make -C docs html
# python tests/testVerification.py
```

Then upload/create-pull-request to github, via
``` bash
./commit.py 'my message'
```
