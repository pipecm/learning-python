import unittest
import cap


class TestCap(unittest.TestCase):
    def test_cap_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_cap_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty python')

    def test_title(self):
        text = 'monty python'
        result = cap.title_text(text)
        self.assertEqual(result, 'Monty Python')

    def test_upper(self):
        text = 'python'
        result = cap.uppercase_text(text)
        self.assertEqual(result, 'PYTHON')


if __name__ == "__main__":
    unittest.main()
