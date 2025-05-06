import unittest

from textNode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("This is an image", "image", "https://random.url.com")
        node2 = TextNode("This is a link", "link", "https://random.link.url.com")
        self.assertNotEqual(node1, node2)

    def test_text_only(self):
        node = TextNode("This is some text", TextType.BOLD)
        node2 = TextNode("This is more text", TextType.ITALIC)
        node3 = TextNode("this is normal text", TextType.NORMAL)
        for node in [node,node2,node3]:
            self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()