# Purpose is to unit test the class poem

from poem import Poem
import unittest


class TestPoemClass(unittest.TestCase):
    def setUp(self):
        self.poem = Poem()
        self.POEM_LENGTH = 11

    def test_load_data(self):
        poem_as_list = self.poem._Poem__load_poem()
        self.assertEqual(len(poem_as_list), self.POEM_LENGTH)

    def test_get_poem(self):
        poem_as_list = self.poem.get_poem()
        self.assertEqual(len(poem_as_list), self.POEM_LENGTH)

    def test_str_(self):
        human_readable_str = self.poem.__str__()
        self.assertIsNotNone(human_readable_str)

    def test_len_(self):
        self.assertEqual(len(self.poem), self.POEM_LENGTH)


if __name__ == '__main__':
    unittest.main()
