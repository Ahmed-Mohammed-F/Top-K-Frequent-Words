import unittest
from main import top_k_words, word_counts

class TopKTests(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(word_counts("Hello, hello! World."), {"hello": 2, "world": 1})
    def test_top_two(self):
        self.assertEqual(top_k_words("cat dog cat bird dog dog", 2), [(3, "dog"), (2, "cat")])
    def test_tie(self):
        self.assertEqual(top_k_words("ant bee", 1), [(1, "bee")])
    def test_zero(self):
        self.assertEqual(top_k_words("hello", 0), [])
    def test_empty(self):
        self.assertEqual(top_k_words("", 3), [])

if __name__ == '__main__':
    unittest.main()
