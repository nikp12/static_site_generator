import unittest

from htmlnode import *
class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_children_props(self):
        leaf_props = {"href":"www.google.com"}
        parent_props = {"href":"www.bing.com"}
        child_node = LeafNode("a", "child", leaf_props)
        parent_node = ParentNode("a", [child_node], parent_props)
        self.assertEqual(
            parent_node.to_html(),
            "<a href=\"www.bing.com\"><a href=\"www.google.com\">child</a></a>"
        )

    def test_to_html_with_grandchildren_props(self):
        leaf_props = {"href":"www.google.com"}
        parent_props = {"href":"www.bing.com"}
        grandchild_node = LeafNode("a", "child", leaf_props)
        child_node = ParentNode("a", [grandchild_node], parent_props)
        parent_node = ParentNode("a", [child_node], parent_props)
        self.assertEqual(
            parent_node.to_html(),
            "<a href=\"www.bing.com\"><a href=\"www.bing.com\"><a href=\"www.google.com\">child</a></a></a>"
        )
    
if __name__ == "__main__":
    unittest.main()