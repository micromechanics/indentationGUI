# micromechanics-indentationGUI documentation

`micromechanics-indentationGUI` is a GUI for nanoindentation data analysis.
It brings the common workflows used in this project into one place:

- tip area function calibration
- frame compliance calibration
- hardness and Young's modulus analysis
- creep analysis
- tip-radius calibration
- pop-in analysis
- clustering and mapping
- exporting results to `xlsx` or `hdf5`

This documentation is organized to help both new users and returning users
find the next useful page quickly.

```{toctree}
:maxdepth: 1
:caption: Start Here

GettingStarted
WorkflowGuide
```

```{toctree}
:maxdepth: 1
:caption: Analysis tabs

TipAreaFunction
FrameCompliance
HardnessModulus
Creep
TipRadius
PopIn
Classification
```

```{toctree}
:maxdepth: 1
:caption: Help

FAQ
```

```{toctree}
:maxdepth: 1
:caption: Project links

GitHub repository <https://github.com/micromechanics/indentationGUI>
PyPI package <https://pypi.org/project/micromechanics-indentationGUI/>
```

## Overview

`micromechanics-indentationGUI` is designed for users who need a practical GUI
for indentation workflows, from calibration to final export. The docs below are
organized so you can either start from the beginning or jump directly to a
specific analysis tab.

```{image} img/main_window_tab_TAF.png
:alt: Main window of micromechanics-indentationGUI
:width: 100%
```

<div class="landing-grid">
  <a class="landing-card landing-card-primary" href="GettingStarted.html">
    <div class="landing-card-kicker">Start Here</div>
    <h3>Getting Started</h3>
    <p>Install the GUI, launch it, load files, and learn the basic interactions.</p>
  </a>
  <a class="landing-card landing-card-primary" href="WorkflowGuide.html">
    <div class="landing-card-kicker">Roadmap</div>
    <h3>Workflow Guide</h3>
    <p>See the recommended order of analysis and how the main tabs depend on each other.</p>
  </a>
  <a class="landing-card landing-card-primary" href="FAQ.html">
    <div class="landing-card-kicker">Help</div>
    <h3>FAQ</h3>
    <p>Find the common GUI operations that are easy to forget during daily work.</p>
  </a>
</div>

## Analysis workflows

<div class="landing-grid">
  <a class="landing-card" href="TipAreaFunction.html">
    <h3>Tip Area Function</h3>
    <p>Calibrate the TAF, inspect the fit, and review the weight and property plots.</p>
  </a>
  <a class="landing-card" href="FrameCompliance.html">
    <h3>Frame Compliance</h3>
    <p>Calibrate frame compliance for the workflows that need stiffness correction.</p>
  </a>
  <a class="landing-card" href="HardnessModulus.html">
    <h3>Hardness and Young's Modulus</h3>
    <p>Run the core H/E analysis and inspect the depth-dependent property plots.</p>
  </a>
  <a class="landing-card" href="Creep.html">
    <h3>Creep</h3>
    <p>Evaluate creep rate and inspect time-dependent behavior after calibration.</p>
  </a>
  <a class="landing-card" href="TipRadius.html">
    <h3>Tip Radius</h3>
    <p>Fit Hertzian contact and calibrate the indenter tip radius.</p>
  </a>
  <a class="landing-card" href="PopIn.html">
    <h3>Pop-in</h3>
    <p>Analyse pop-in events and inspect the derived load, modulus, and shear stress.</p>
  </a>
  <a class="landing-card" href="Classification.html">
    <h3>Classification</h3>
    <p>Cluster and map indentation results across multiple datasets.</p>
  </a>
</div>

## Quick start

If you are new to the GUI, start here:

1. Read [Getting Started](GettingStarted.md)
2. Read [Workflow Guide](WorkflowGuide.md)
3. Use [FAQ](FAQ.md) when you need help with test selection or manual operations
