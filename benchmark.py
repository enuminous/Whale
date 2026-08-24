import random
from whale import WhaleEvaluator, WhaleConfig

def stable(seed=41, n=120):
    rng = random.Random(seed)
    return [0.5 + rng.gauss(0,0.02) for _ in range(n)]

def slow_drift(seed=41, n=120):
    rng = random.Random(seed)
    xs = []
    for t in range(n):
        xs.append(0.5 + 0.0025*t + rng.gauss(0,0.02))
    return xs

def drift_then_flat(seed=41, n=120):
    rng = random.Random(seed)
    xs = []
    for t in range(n):
        if t < 90:
            base = 0.5 + 0.003*t
        else:
            base = 0.5 + 0.003*90
        xs.append(base + rng.gauss(0,0.01))
    return xs

if __name__ == "__main__":
    ev = WhaleEvaluator(WhaleConfig(recent_window=20,drift_scale=40,gap_scale=2,deviation_scale=2))
    for name,fn in [("stable",stable),("slow_drift",slow_drift),("drift_then_flat",drift_then_flat)]:
        xs = fn()
        print(name, ev.evaluate(xs, baseline=0.5))
