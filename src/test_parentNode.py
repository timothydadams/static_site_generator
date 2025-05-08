import unittest

from htmlNode import ParentNode, LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child", {'class':'special'})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span class=\"special\">child</span></div>")

    def test_multiple_children(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(), 
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild", {"fake_attr":"test"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b fake_attr=\"test\">grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()