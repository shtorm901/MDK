import unittest
from null import search


class TestPul(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search(100020), 4)


if __name__ == "__main__":
    unittest.main()