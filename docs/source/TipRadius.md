---
myst:
  html_meta:
    description: Calibrate indenter tip radius in micromechanics-indentationGUI with Hertzian fitting and inspect the resulting fit quality.
---

# Tip Radius

Use the `Tip Radius` tab to calibrate the indenter tip radius by Hertzian
fitting.

```{image} img/main_window_tab_TipRadius.png
:alt: Tip Radius tab in micromechanics-indentationGUI
:width: 100%
```

## Inputs

- Hertzian calibration file
- frame compliance, if needed for your dataset

## Typical steps

1. Load the Hertzian calibration file.
2. Run frame compliance calibration if needed.
3. Perform the tip-radius calculation.
4. Inspect the fit and the calibrated tip radius.

## Outputs to inspect

Look at:

- the Hertzian fit quality
- the fitted region
- whether the calibrated tip radius is physically reasonable

## Key plots

The key plot is the Hertzian fitting plot. It tells you:

- whether the chosen fitting window is appropriate
- whether the model follows the experimental data
- whether the final tip radius is supported by the fit

## Common problems

Typical issues include:

- using a dataset that is not appropriate for Hertzian fitting
- fitting the wrong region
- accepting a radius value without checking fit quality

## Next step

The calibrated tip radius is often used later in:

- [Pop-in](PopIn.md)
