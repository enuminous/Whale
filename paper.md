# WHALE: Whole-History Aggregated Longitudinal Evaluation

## Abstract

WHALE is an experimental framework for detecting slow systemic drift and long-horizon change that may remain invisible in recent-window monitoring. It combines global trend, cumulative deviation, recency-versus-history disagreement, and regime-memory metrics into a whole-history stability assessment.

## 1. Motivation

A system can look stable today while being far from where it began.

Short-window metrics are poorly suited to detect secular drift and hysteresis.

## 2. Model

Global drift:

`D = slope(x_1...x_T)`

Cumulative deviation:

`C = mean |x_t-baseline|`

Recency/history gap:

`RHD = |mean(recent)-mean(history)|`

Regime memory:

`M = |mean(post)-mean(pre)|`

## 3. Metrics

- global drift
- recent drift
- cumulative deviation
- recency/history gap
- regime memory
- long-run stability

## 4. Baselines

- linear trend analysis
- rolling-window metrics
- change-point detection
- ARIMA/state-space models
- cumulative sum monitoring

## 5. Ablations

- recent window only
- no regime-memory term
- no cumulative deviation
- no multi-scale comparison
- alternate baselines
- shuffled temporal order

## 6. Falsification

If standard longitudinal time-series methods capture the same long-horizon risks under equivalent information access, WHALE's additional structure is not justified.

## 7. Claim boundary

WHALE measures temporal structure across long histories. Drift is not automatically harmful and requires domain interpretation.
