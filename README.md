# WHALE — EFMW Zoo #41

**Whole-History Aggregated Longitudinal Evaluation**

WHALE is an experimental EFMW-inspired framework for evaluating slow systemic drift and long-horizon change that may remain invisible in short windows.

## Core question

> What becomes visible only when the entire history is considered?

WHALE is designed for cumulative effects, regime memory, long-term degradation, and differences between local stability and global trajectory.

## Primary outputs

- long-horizon drift
- cumulative deviation
- regime-memory score
- trajectory curvature
- recency/history disagreement
- irreversible-change indicator
- whole-history coherence
- long-run stability score

## Repository contents

- `theory.md`
- `architecture.md`
- `longitudinal_model.md`
- `limitations.md`
- `whale.py`
- `benchmark.py`
- `ablations.py`
- `test_whale.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_whale.py
```

## Zoo position

COBRA #40 evaluates divergence between declared objectives and observed behavior.

**WHALE #41 stretches the temporal axis: it asks whether a system that looks stable locally has been drifting over the full historical record.**
