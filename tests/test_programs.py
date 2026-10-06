import unittest
from hunter.programs import PROGRAMS, payout_candidates

class ProgramTests(unittest.TestCase):
    def test_programs_are_public_and_have_rules(self):
        self.assertGreaterEqual(len(PROGRAMS), 2)
        for program in PROGRAMS:
            self.assertTrue(program["program_url"].startswith("https://"))
            self.assertIn("payouts", program)
    def test_bep20_candidate_exists(self):
        names = {p["name"] for p in payout_candidates("BEP20")}
        self.assertIn("Symbiosis", names)

if __name__ == "__main__":
    unittest.main()
