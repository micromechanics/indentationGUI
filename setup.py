#!/usr/bin/env python
from setuptools import setup
import commit

if __name__ == '__main__':
    setup(name='micromechanics-indentationGUI',
          version=commit.get_version()[1:],
          entry_points={
                          'console_scripts': 
                                            [
                                              'micromechanics-indentationGUI=micromechanics-indentationGUI',
                                            ]
                        }
          )
