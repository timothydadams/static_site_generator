import unittest

from htmlNode import HTMLNode

tmp_props = {
    "class":"test",
    "style":"font-weight:bold;"
}

link_props = {
    "href":"https://www.my-random-image.com/url/v1/img.png",
    "target":"_blank"
}

class TestHTMLNode(unittest.TestCase):
    def test_initialization(self):
        node = HTMLNode("p","this is paragraph text content",props=tmp_props)
        self.assertEqual(node.props['class'], tmp_props['class'])
        self.assertEqual(node.children, None)
        self.assertEqual(node.tag, "p")

    def test_props_converstion(self):
        node = HTMLNode("a","My Image",props=link_props)
        props_html_string = node.props_to_html()
        self.assertEqual(props_html_string, " href=\"https://www.my-random-image.com/url/v1/img.png\" target=\"_blank\"")

    def test_children(self):
        node = HTMLNode("div",children=[HTMLNode("p","nested p"), HTMLNode("p", "another nested p")], props=tmp_props)
        children = node.children
        self.assertEqual(len(children), 2)
        self.assertEqual(node.props["class"], "test")
        for child in children:
            self.assertEqual(child.tag, "p")
   


if __name__ == "__main__":
    unittest.main()