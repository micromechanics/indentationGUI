---
myst:
  html_meta:
    description: Calibrate the tip area function in micromechanics-indentationGUI and inspect the TAF, frame stiffness, hardness, modulus, and weight plots.
---

# Tip Area Function

Use the `Tip Area Function` tab when you want to calibrate the tip area
function from a reference dataset, typically fused silica.

```{image} img/main_window_tab_TAF.png
:alt: Tip Area Function tab in micromechanics-indentationGUI
:width: 100%
```

## Inputs

- a reference file
- material parameters
- fitting range and TAF settings

## Typical steps

1. Load the fused silica reference file.
2. Set the material and tip parameters.
3. Choose the fitting range.
4. Run the TAF calibration.
5. Inspect the generated plots.
6. Copy the calibrated TAF into the reference fields if needed.

## Outputs to inspect

Important outputs include:

- frame stiffness plot
- TAF plot
- hardness and modulus plots
- interactive weight `w` plot

## Key plots

The most informative plots in this workflow are:

- the TAF plot, to judge the fitted area function
- the frame stiffness plot, to check stability of the calibration
- the hardness and modulus plots, to see whether the calibrated TAF behaves
  reasonably over depth
- the weight `w` plot, to inspect how the fitting weight is distributed

## Common problems

Typical issues include:

- using the wrong reference dataset
- choosing a fitting range that is too narrow or unstable
- copying an outdated TAF into later tabs
- accepting a fit without checking the weight `w` and hardness/modulus plots

## Next step

After TAF is calibrated, the usual next step is
[Frame Compliance](FrameCompliance.md) or directly
[Hardness and Young's Modulus](HardnessModulus.md), depending on your workflow.
