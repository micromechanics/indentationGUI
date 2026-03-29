---
myst:
  html_meta:
    description: Calibrate frame compliance in micromechanics-indentationGUI for workflows that require stiffness correction before later analysis.
---

# Frame Compliance

Several workflows in the GUI require frame compliance correction. This step is
shared across multiple tabs.

```{image} img/main_window_tab_FrameCompliance.png
:alt: Frame Compliance view in micromechanics-indentationGUI
:width: 100%
```

## Where it appears

Frame compliance is used in:

- `tabHE_FrameStiffness`
- `tabCreep_FrameStiffness`
- `tabTipRadius_FrameStiffness`
- `tabPopIn_FrameStiffness`

## Inputs

- frame-stiffness reference file or files
- selected tests
- fitting range for the stiffness evaluation

## Typical steps

1. Load the frame-stiffness reference file or files.
2. Select the tests to use.
3. Adjust fitting ranges if necessary.
4. Calculate frame compliance.
5. Copy the result into the target analysis tab.

## Outputs to inspect

Important checks include:

- whether the selected tests form a stable stiffness trend
- whether the fitted range is physically reasonable
- whether the copied frame compliance value matches the target tab

## Key plots

The most important plot here is the frame stiffness fit itself. Use it to
check:

- whether the selected tests follow a consistent trend
- whether the fitting region is appropriate
- whether outliers are influencing the result

## Common problems

If frame compliance is not calibrated correctly, downstream results can shift
in a systematic way.

Typical issues include:

- selecting unsuitable tests
- using a poor fitting range
- forgetting to copy the result into the target analysis tab
- mixing results from different datasets

## Next step

After frame compliance is ready, continue to the relevant target page:

- [Hardness and Young's Modulus](HardnessModulus.md)
- [Creep](Creep.md)
- [Tip Radius](TipRadius.md)
- [Pop-in](PopIn.md)
