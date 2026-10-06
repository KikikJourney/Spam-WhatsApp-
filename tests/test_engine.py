import unittest

from simulator.engine import run
from simulator.models import SimulationConfig

class EngineTests(unittest.TestCase):
    def test_zero_messages(self):
        r = run(SimulationConfig(messages=0))
        self.assertEqual(r.processed, 0)
        self.assertEqual(r.dropped, 0)

    def test_duplicates(self):
        r = run(SimulationConfig(messages=10, duplicate_rate=1.0))
        self.assertEqual(r.generated, 10)
        self.assertEqual(r.duplicates, 10)
        self.assertEqual(r.processed, 20)

    def test_retry_storm(self):
        r = run(SimulationConfig(messages=5, failure_rate=1.0, retry_limit=2))
        self.assertEqual(r.failed, 5)
        self.assertEqual(r.retried, 10)
        self.assertEqual(r.dropped, 5)
        self.assertEqual(r.processed, 0)

    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
            run(SimulationConfig(rate=0))

    def test_deterministic_core(self):
        cfg = SimulationConfig(messages=100, failure_rate=0.1, duplicate_rate=0.2)
        a, b = run(cfg), run(cfg)
        self.assertEqual(a.generated, b.generated)
        self.assertEqual(a.processed, b.processed)
        self.assertEqual(a.failed, b.failed)
        self.assertEqual(a.retried, b.retried)
        self.assertEqual(a.duplicates, b.duplicates)
        self.assertEqual(a.dropped, b.dropped)
        self.assertEqual(a.latency_ms, b.latency_ms)

if __name__ == "__main__":
    unittest.main()
