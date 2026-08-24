# WHALE Architecture

## Pipeline

1. Longitudinal Data Ingestor
2. Baseline/Regime Annotator
3. Multi-Scale Window Engine
4. Global Trend Estimator
5. Cumulative Deviation Analyzer
6. Regime Memory/Hysteresis Analyzer
7. Curvature Detector
8. Recency-vs-History Comparator
9. Long-Run Stability Scorer
10. Audit Reporter

## Inputs

- ordered historical measurements
- baseline period
- optional regime labels
- intervention events
- recovery intervals

## Outputs

```json
{
  "global_drift": 0.0031,
  "recent_drift": 0.0002,
  "cumulative_deviation": 0.19,
  "recency_history_gap": 0.24,
  "regime_memory": 0.17,
  "trajectory_curvature": 0.00004,
  "long_run_stability": 0.61
}
```

## Design principle

WHALE should flag cases where local windows look reassuring but the whole trajectory has moved materially away from the historical baseline.

## Integration

ELEPHANT can preserve the full longitudinal event history.

MANTIS can identify abrupt transitions inside WHALE's slower record.

WOLF can identify distributed precursors before long-run drift becomes obvious.

PHOENIX can compare post-recovery states against pre-hazard history.
