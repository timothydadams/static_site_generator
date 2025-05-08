import unittest

from textNode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("This is an image", TextType.IMAGE, "https://random.url.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://random.link.url.com")
        self.assertNotEqual(node1, node2)

    # text styles (bold, italic, normal) should not have a url // None
    def test_text_only(self):
        node = TextNode("This is some text", TextType.BOLD)
        node2 = TextNode("This is more text", TextType.ITALIC)
        node3 = TextNode("this is normal text", TextType.NORMAL)
        for node in [node,node2,node3]:
            self.assertEqual(node.url, None)


    def test_invalid_nodeType(self):
        #with self.assertRaises(ValueError):
        self.assertRaises(ValueError, TextNode, "Bad data", "span")
        self.assertRaises(ValueError, TextNode, "Bad data", "div")
        self.assertRaises(ValueError, TextNode, "Bad data", "h1")
            #TextNode("Bad data", "span")
            #TextNode("Another bad node", TextNode.SPAN)
        


if __name__ == "__main__":
    unittest.main()