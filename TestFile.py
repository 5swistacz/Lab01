from File import File
import unittest

class TestFile(unittest.TestCase):
    def test_wc_should_return_correct_sum_of_words(self):
        f = File()
        f.set_name("test.log")
        expected_sum = 5
        self.assertEqual(f.word_count_all(), expected_sum)
