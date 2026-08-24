# WHALE Theory

## 1. Problem

Short-window monitoring can miss:
- slow degradation,
- cumulative bias,
- ratcheting state change,
- repeated small corrections,
- regime memory,
- long-term instability,
- secular trend hidden by local noise.

WHALE treats the complete longitudinal record as an object of analysis.

## 2. Time series

Let observations be:

`x_1, x_2, ..., x_T`

Short-window health may be high while whole-history trend is poor.

## 3. Cumulative deviation

Relative to baseline `mu_0`:

`C_T = (1/T) * sum_t |x_t - mu_0|`

or a signed version where direction matters.

## 4. Long-horizon drift

Fit a global trend:

`x_t ≈ a + b*t`

The drift rate is:

`D = b`

This should be compared with rolling local trends.

## 5. Recency/history disagreement

Let recent mean be `mu_recent` and historical mean be `mu_hist`.

`RHD = |mu_recent - mu_hist|`

Large disagreement can indicate regime transition or slow structural drift.

## 6. Regime memory

If post-shock dynamics remain shifted after the shock is removed, define:

`M = |post_recovery_baseline - pre_shock_baseline|`

Persistent nonzero `M` indicates hysteresis or memory.

## 7. Trajectory curvature

A long-horizon nonlinear trajectory can be approximated by second-order fit:

`x_t ≈ a + b*t + c*t^2`

Curvature term `c` measures acceleration of change.

## 8. Irreversibility

If corrective interventions repeatedly fail to return state toward the historical baseline:

`I = 1 - recovery_fraction`

## 9. Whole-history coherence

WHALE can compare local segments against the global trajectory.

A system may be locally smooth but globally incoherent if segment trends point in incompatible directions.

## 10. EFMW interpretation

The EFMW-inspired element is recursive aggregation across temporal scales:
- local window,
- intermediate regime,
- full history.

The important distinction is:

**stable now** versus **stable across history**.

## 11. Falsifiable prediction

WHALE should add value when:
- drift is slow,
- memory effects exist,
- short windows appear normal,
- cumulative state matters.

If conventional trend analysis and change-point models fully capture the same signal, WHALE's extra framing is not justified.
