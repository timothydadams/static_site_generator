import unittest

from htmlNode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_initialization(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node.children, None)
        self.assertEqual(node.tag, "p")

    def test_fail_if_no_value_provided_error(self):
        self.assertRaises(TypeError, LeafNode, "p")

    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")


if __name__ == "__main__":
    unittest.main()