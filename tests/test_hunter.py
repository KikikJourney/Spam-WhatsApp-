import unittest
from hunter.checks import check_cors, check_security_headers
from hunter.models import Target
from hunter.scope import validate_target

class HunterTests(unittest.TestCase):
    def setUp(self):
        self.target = Target(name="test", base_url="https://example.test")
    def test_scope_rejects_invalid_url(self):
        with self.assertRaises(ValueError): validate_target("javascript:alert(1)")
    def test_scope_rejects_credentials(self):
        with self.assertRaises(ValueError): validate_target("https://user:pass@example.test")
    def test_missing_headers(self):
        self.assertEqual(len(check_security_headers(self.target, {})), 4)
    def test_cors_wildcard(self):
        self.assertEqual(check_cors(self.target, {"Access-Control-Allow-Origin": "*"})[0].check_id, "cors/wildcard")

if __name__ == "__main__": unittest.main()
