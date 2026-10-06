import unittest
from hunter.programs import PROGRAMS, payout_candidates, research_queue

class ProgramTests(unittest.TestCase):
    def test_programs_are_public_and_have_rules(self):
        self.assertGreaterEqual(len(PROGRAMS), 2)
        for program in PROGRAMS:
            self.assertTrue(program["program_url"].startswith("https://"))
            self.assertIn("payouts", program)
            self.assertIn("program_url", program)

    def test_layerzero_source_is_registered(self):
        layerzero = next(p for p in PROGRAMS if p["name"] == "LayerZero")
        self.assertEqual(layerzero["source_repo"], "https://github.com/LayerZero-Labs/LayerZero-v2")
        self.assertEqual(layerzero["scope_assets"], 25)
        self.assertTrue(layerzero["poc_required"])

    def test_bep20_candidate_exists(self):
        names = {p["name"] for p in payout_candidates("BEP20")}
        self.assertIn("Symbiosis", names)

    def test_research_queue_prioritizes_bep20_compatible_target(self):
        queue = research_queue("BEP20")
        self.assertEqual(queue[0]["name"], "Symbiosis")
        self.assertEqual(queue[0]["scope_mode"], "local-fork-only")
        self.assertTrue(queue[0]["poc_required"])

if __name__ == "__main__":
    unittest.main()
