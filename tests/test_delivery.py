import unittest

from simulator.delivery import run_delivery_proof, proof_summary


class DeliveryProofTests(unittest.TestCase):
    def test_minimum_proof(self):
        proof = run_delivery_proof(1)
        self.assertEqual(proof.delivered, 1)
        self.assertEqual(proof.failed, 0)

    def test_default_small_proof(self):
        proof = run_delivery_proof()
        self.assertEqual(proof.requested, 3)
        self.assertEqual(proof.delivered, 3)

    def test_10000_synthetic_deliveries(self):
        proof = run_delivery_proof(10_000)
        self.assertEqual(proof.requested, 10_000)
        self.assertEqual(proof.accepted, 10_000)
        self.assertEqual(proof.sent, 10_000)
        self.assertEqual(proof.delivered, 10_000)
        self.assertEqual(proof.failed, 0)

    def test_invalid_count(self):
        with self.assertRaises(ValueError):
            run_delivery_proof(0)

    def test_transport_is_disabled(self):
        summary = proof_summary(run_delivery_proof(3))
        self.assertFalse(summary["network_transport"])


if __name__ == "__main__":
    unittest.main()
