import unittest
from modules.recruitment.job_fetcher import test_module

class TestRecruitment(unittest.TestCase):
    def test_jobs(self):
        self.assertIn("求人", test_module())

if __name__ == "__main__":
    unittest.main()
