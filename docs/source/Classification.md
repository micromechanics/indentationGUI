---
myst:
  html_meta:
    description: Cluster and map indentation results in micromechanics-indentationGUI with the K-means Classification tab.
---

# Classification

Use the `K-means Clustering` tab to cluster and map hardness/modulus data.

```{image} img/main_window_tab_Classification.png
:alt: Classification tab in micromechanics-indentationGUI
:width: 100%
```

## Inputs

- multiple result files
- clustering settings appropriate for your dataset

## Typical steps

1. Load multiple result files.
2. Choose clustering settings.
3. Run classification.
4. Plot the mapping before and after clustering.

## Outputs to inspect

Useful checks include:

- whether the clusters are stable
- whether the mapping matches the expected microstructural regions
- whether the input hardness/modulus data were prepared consistently

## Key plots

The key plots are:

- the mapping before clustering
- the mapping after clustering
- any cluster-colored property plot that shows whether the clusters are
  physically meaningful

## Common problems

Typical issues include:

- mixing inconsistent input datasets
- choosing clustering settings without checking the mapping
- interpreting clusters without comparing them to the original data

## Next step

Classification commonly produces a final analysis view, so the next step is
usually export, reporting, or comparison with microscopy or phase information.

## Related workflows

Classification commonly uses results from:

- [Hardness and Young's Modulus](HardnessModulus.md)
