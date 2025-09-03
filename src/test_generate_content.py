import unittest

from generate_content import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_eq(self):
        title = extract_title("# Valid Title")
        self.assertEqual(title, "Valid Title")

    def test_eq_double(self):
        title = extract_title(
            """
# Title One
# Title Two
"""
        )
        self.assertEqual(title, "Title One")

    def test_eq_long(self):
        title = extract_title(
            """
# Title
some random stuff
and more content
even more things
- and
- this
- list
"""
        )
        self.assertEqual(title, "Title")

    def test_title_not_provided(self):
        try:
            extract_title("this md has no title tag")
            self.fail("shoud raise an exception")
        except Exception as e:
            pass

if __name__ == "__main__":
    unittest.main()