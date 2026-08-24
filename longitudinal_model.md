# Longitudinal Model

## Observation schema

```json
{
  "time": 420,
  "value": 0.73,
  "regime": "post_update",
  "intervention": null
}
```

## Multi-scale windows

WHALE compares:
- local window
- medium window
- whole-history window

## Drift

For points `(t_i, x_i)`, ordinary least squares estimates:

`b = cov(t,x) / var(t)`

## Cumulative deviation

`C = mean |x_t - baseline|`

## Regime memory

Compare the mean state before and after a bounded perturbation and recovery period.

## History compression

Summaries may be used for scale, but they must preserve:
- trend
- regime boundaries
- interventions
- uncertainty
- representative extremes

## Long-run alert

A candidate alert may require:
- global drift above threshold
- recent window locally stable
- cumulative deviation increasing

This is the characteristic WHALE habitat.
