---
myst:
  html_meta:
    description: Run hardness and Young's modulus analysis in micromechanics-indentationGUI after tip area function and frame compliance calibration.
---

# Hardness and Young's Modulus

Use the `Hardness and Young's Modulus` tab after TAF and frame compliance are
ready.

```{image} img/main_window_tab_HE.png
:alt: Hardness and Young's Modulus tab in micromechanics-indentationGUI
:width: 100%
```

## Inputs

- one or more test files
- calibrated TAF
- frame compliance

## Typical steps

1. Load the test file or files.
2. Copy the calibrated TAF.
3. Copy the frame compliance.
4. Choose the mean-value range.
5. Run the calculation.
6. Inspect the plots and result tables.

## Outputs to inspect

Typical plots include:

- hardness vs contact depth
- hardness vs depth
- modulus vs contact depth
- modulus vs depth
- H-E related plots

Also check:

- the mean-value range used for the reported values
- whether the selected tests are the intended ones
- whether the resulting values are stable across depth

## Key plots

The most useful plots in this workflow are:

- hardness vs contact depth
- hardness vs depth
- modulus vs contact depth
- modulus vs depth
- H-E related plots for comparing property relationships across tests

## Common problems

Typical issues include:

- forgetting to update TAF or frame compliance before running
- using the wrong mean-value range
- including unsuitable tests in the calculation
- reading summary values without checking the plots

## Next step

This tab is often the main analysis result for a project. It can also feed:

- [Classification](Classification.md)
- [Creep](Creep.md), when additional time-dependent analysis is needed
