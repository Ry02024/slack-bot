import unittest
from modules.auto_reply.reply_handler import test_module

class TestAutoReply(unittest.TestCase):
    def test_reply(self):
        self.assertIn("利用規約", test_module())

if __name__ == "__main__":
    unittest.main()
