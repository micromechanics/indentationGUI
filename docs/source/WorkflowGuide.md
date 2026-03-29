# Workflow Guide

This page is the roadmap for the whole GUI. It shows the usual analysis order
and links to the dedicated page for each workflow.

## Analysis tabs

- [Tip Area Function](TipAreaFunction.md)
- [Frame Compliance](FrameCompliance.md)
- [Hardness and Young's Modulus](HardnessModulus.md)
- [Creep](Creep.md)
- [Tip Radius](TipRadius.md)
- [Pop-in](PopIn.md)
- [Classification](Classification.md)

## Recommended order

For most datasets, the recommended order is:

```text
Load file(s)
   |
   v
Tip Area Function
   |
Frame compliance
   |
Hardness / Young's modulus
   |
   +--> Creep
   +--> Tip Radius
   |      |
   |      +--> Pop-in
   \--> Classification

[Export / save available after results]
```

Not every project needs every branch. Many users stop after TAF, frame
compliance, and hardness/modulus analysis, then save or export the results.

## Why this order

- Start with [Tip Area Function](TipAreaFunction.md) when you need a calibrated
  area function for later workflows.
- Use [Frame Compliance](FrameCompliance.md) next whenever the target workflow
  needs frame compliance correction.
- Use [Hardness and Young's Modulus](HardnessModulus.md) after TAF and frame
  compliance are ready, because it is the main downstream analysis step for
  many datasets.
- Use [Creep](Creep.md) after [Hardness and Young's Modulus](HardnessModulus.md)
  in the usual workflow, because creep analysis needs a material Young's
  modulus input.
- Use [Pop-in](PopIn.md) after [TipRadius](TipRadius.md), because pop-in
  analysis needs a calibrated tip radius.
- Continue to [TipRadius](TipRadius.md) or [Classification](Classification.md)
  only if your project needs those later analyses.

## Export results

After checking the results and plots, the GUI supports:

- exporting results to `xlsx`
- exporting results to `hdf5`

## Save sessions

If you want to continue the work later, the GUI supports:

- saving sessions
- reloading saved sessions
