# Limitations and Falsification

WHALE is an experimental longitudinal evaluation framework.

## Limitations

- Global trends can be distorted by regime changes.
- Long histories may mix incompatible operating conditions.
- Baseline choice matters.
- Missing data can bias cumulative metrics.
- A secular trend may be intended adaptation.
- Hysteresis may be benign or necessary.

## Falsification criteria

WHALE's central hypothesis is weakened if:

1. Standard time-series trend analysis performs equivalently.
2. Multi-scale comparison adds no value.
3. Regime-memory scoring does not predict persistent change.
4. Whole-history metrics do not improve detection over recent windows.
5. Results fail on held-out long-horizon datasets.
6. Long-run scores are unstable to reasonable baseline choices.

## Claim boundary

WHALE measures long-horizon temporal structure. It does not prove that observed drift is harmful or causal without domain-specific evidence.
