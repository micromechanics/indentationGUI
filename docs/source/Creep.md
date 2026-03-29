# Creep

Use the `Creep` tab for creep-rate evaluation.

```{image} img/main_window_tab_Creep.png
:alt: Creep tab in micromechanics-indentationGUI
:width: 100%
```

## Inputs

- one or more creep test files
- calibrated TAF
- frame compliance
- material Young's modulus input, often taken from the `Hardness and Young's Modulus` tab

## Typical steps

1. Load the file or files.
2. Copy or enter TAF, frame compliance, and the material Young's modulus.
3. Run the creep calculation.
4. Inspect the creep-rate plots and related values.

## Outputs to inspect

Check whether:

- the selected tests are appropriate
- the corrected data behave as expected
- the resulting creep-rate values are stable in the range you care about

## Key plots

The most important plots are the creep-rate plots and any related depth or
time-dependent curves used in the calculation. These help you judge whether the
reported creep values come from a stable region.

## Common problems

Typical issues include:

- running the analysis without the correct TAF, frame compliance, or material Young's modulus
- using tests that are not suitable for creep evaluation
- over-interpreting unstable creep-rate regions

## Next step

This workflow depends on earlier setup from:

- [Tip Area Function](TipAreaFunction.md)
- [Frame Compliance](FrameCompliance.md)
- [Hardness and Young's Modulus](HardnessModulus.md) for the material Young's modulus input in typical workflows
