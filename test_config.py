import unittest

from src.app import mask_secret
from src.config import Config


class ConfigTests(unittest.TestCase):
    def test_mask_secret_redacts_value(self):
        self.assertEqual(mask_secret("supersecret"), "su*******et")
        self.assertEqual(mask_secret("abc"), "****")
        self.assertEqual(mask_secret(None), "not configured")

    def test_validate_reports_missing_values(self):
        config = Config()
        missing = config.validate()
        self.assertIn("DATABASE_URL", missing)
        self.assertIn("API_KEY", missing)


if __name__ == "__main__":
    unittest.main()
