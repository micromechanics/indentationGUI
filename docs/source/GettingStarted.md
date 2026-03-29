---
myst:
  html_meta:
    description: Install micromechanics-indentationGUI, launch the GUI, load indentation data, generate test lists, and learn the first analysis steps.
---

# Getting Started

Use this page to launch the GUI, load data, and learn the basic test-selection actions.

## 1. Installation

For a normal installation:

1. Create and activate a Python environment with Python `>= 3.10`.
2. Install the GUI from PyPI:

```bash
pip install micromechanics-indentationGUI
```

3. Start the installed GUI:

```bash
micromechanics-indentationGUI
```

To upgrade an existing installation:

```bash
pip install --upgrade micromechanics-indentationGUI
```

If you are working from the repository instead of an installed package, start it from the project root with:

```bash
python -m micromechanics_indentationGUI.main
```

## 2. First steps in the GUI

When the GUI opens, start with these steps:

1. Choose the workflow tab you want to use.
2. Add one or more data files.
3. Check that the file list is correct.
4. Run the tab's first calibration or calculation to generate the test list.
5. Select the tests you want to inspect or calculate.
6. Plot the selected tests to inspect the load-depth curve and check whether the parameters for detecting the contact surface or identifying the load-hold-unload segments are correct.
7. Run the calculation again if you changed the test selection or the analysis parameters.
8. Inspect plots and summary values.

Some tabs use a path table instead of a single path field so that you can work with multiple files in one workflow.

In many tabs, the test list is not available until after the first calibration or calculation has finished.

The main workflows are organized into these tabs:

- `Tip Area Function`
- `Hardness and Young's Modulus`
- `Creep`
- `Tip Radius`
- `Analyse Pop-in Effect`
- `K-means Clustering`

Several workflows also have a frame-compliance sub-tab or related frame
compliance step.

If you are not sure where to begin, start with `Tip Area Function` or go to [Workflow Guide](WorkflowGuide.md) for the recommended order.

## 3. Select tests for plotting

There are three common ways to highlight tests for plotting the load-depth curve.

1. Left click

   ![](img/selectTest2plotLoadDepth_1.gif)

2. Left click + `Ctrl`

   ![](img/selectTest2plotLoadDepth_2.gif)

3. Left click + `Shift`

   ![](img/selectTest2plotLoadDepth_3.gif)

## 4. Select tests for calculation

There are three common ways to choose which tests are used in the calculation.

1. Left click

   ![](img/selectTest_1.gif)

2. Select or unselect all tests

   ![](img/selectTest_2.gif)

3. Type the test number

   ![](img/selectTest_3.gif)

## 5. Manually set the contact surface

If needed, move the mouse onto the data point and right click to set the contact surface manually.

![](img/rightClick2selectContactSurface.gif)

## 6. What to read next

Once you are comfortable with loading files and selecting tests, continue with [Workflow Guide](WorkflowGuide.md).
