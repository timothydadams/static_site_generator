import unittest

from textNode import TextNode, TextType, text_node_to_html_node

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
        node3 = TextNode("this is normal text", TextType.TEXT)
        for node in [node,node2,node3]:
            self.assertEqual(node.url, None)


    def test_invalid_nodeType(self):
        self.assertRaises(ValueError, TextNode, "Bad data", "span")
        self.assertRaises(ValueError, TextNode, "Bad data", "div")
        self.assertRaises(ValueError, TextNode, "Bad data", "h1")

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://random-url.com/imgs/1.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
            "src":"https://random-url.com/imgs/1.png",
            "alt": "This is an image"
        })

    def test_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")




if __name__ == "__main__":
    unittest.main()