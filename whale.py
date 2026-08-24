from dataclasses import dataclass
from typing import List, Optional
from statistics import mean

@dataclass
class WhaleConfig:
    recent_window: int = 20
    drift_scale: float = 10.0
    gap_scale: float = 1.0
    deviation_scale: float = 1.0

class WhaleEvaluator:
    def __init__(self, config: Optional[WhaleConfig] = None):
        self.config = config or WhaleConfig()

    @staticmethod
    def linear_slope(xs: List[float]) -> float:
        n = len(xs)
        if n < 2:
            return 0.0
        ts = list(range(n))
        mt = mean(ts)
        mx = mean(xs)
        num = sum((t-mt)*(x-mx) for t,x in zip(ts,xs))
        den = sum((t-mt)**2 for t in ts)
        return num/den if den > 0 else 0.0

    @staticmethod
    def cumulative_deviation(xs: List[float], baseline: float) -> float:
        if not xs:
            return 0.0
        return mean(abs(x-baseline) for x in xs)

    @staticmethod
    def recency_history_gap(xs: List[float], recent_window: int) -> float:
        if not xs:
            return 0.0
        recent = xs[-min(recent_window,len(xs)):]
        return abs(mean(recent)-mean(xs))

    @staticmethod
    def regime_memory(pre: List[float], post: List[float]) -> float:
        if not pre or not post:
            return 0.0
        return abs(mean(post)-mean(pre))

    def evaluate(self, xs: List[float], baseline: Optional[float] = None, pre=None, post=None):
        if not xs:
            return {
                "global_drift":0.0,
                "recent_drift":0.0,
                "cumulative_deviation":0.0,
                "recency_history_gap":0.0,
                "regime_memory":0.0,
                "long_run_stability":1.0
            }

        baseline = xs[0] if baseline is None else baseline
        rw = min(self.config.recent_window, len(xs))
        global_drift = self.linear_slope(xs)
        recent_drift = self.linear_slope(xs[-rw:])
        cumulative = self.cumulative_deviation(xs, baseline)
        gap = self.recency_history_gap(xs, rw)
        memory = self.regime_memory(pre or [], post or [])

        penalty = (
            min(1.0, abs(global_drift)*self.config.drift_scale)*0.30 +
            min(1.0, cumulative*self.config.deviation_scale)*0.25 +
            min(1.0, gap*self.config.gap_scale)*0.25 +
            min(1.0, memory*self.config.gap_scale)*0.20
        )
        stability = max(0.0, 1.0-penalty)

        return {
            "global_drift": global_drift,
            "recent_drift": recent_drift,
            "cumulative_deviation": cumulative,
            "recency_history_gap": gap,
            "regime_memory": memory,
            "long_run_stability": stability
        }
