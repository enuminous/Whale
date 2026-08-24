import unittest
from whale import WhaleEvaluator

class TestWhale(unittest.TestCase):
    def test_constant_series_zero_drift(self):
        ev = WhaleEvaluator()
        out = ev.evaluate([1.0]*20, baseline=1.0)
        self.assertAlmostEqual(out["global_drift"],0.0)

    def test_drift_detected(self):
        ev = WhaleEvaluator()
        out = ev.evaluate([i*0.1 for i in range(20)], baseline=0.0)
        self.assertGreater(out["global_drift"],0.0)

    def test_regime_memory(self):
        ev = WhaleEvaluator()
        m = ev.regime_memory([0.0,0.0],[1.0,1.0])
        self.assertAlmostEqual(m,1.0)

if __name__ == "__main__":
    unittest.main()
