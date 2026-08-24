from benchmark import drift_then_flat
from whale import WhaleEvaluator, WhaleConfig

if __name__ == "__main__":
    xs = drift_then_flat()
    full = WhaleEvaluator(WhaleConfig(recent_window=20,drift_scale=40,gap_scale=2,deviation_scale=2))
    print("full:", full.evaluate(xs, baseline=0.5))

    recent_only = xs[-20:]
    print("recent-only:", full.evaluate(recent_only, baseline=recent_only[0]))
