import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_b(self):
        leaf = LeafNode("b", "this is a test")
        self.assertEqual(leaf.to_html(), "<b> this is a test </b>")

    def test_leaf_to_html_a(self):
        link_props = {"href": "https://www.google.com", "target": "_blank"}
        leaf = LeafNode("a", "Click here", props=link_props)
        self.assertEqual(leaf.to_html(), '<a href="https://www.google.com" target="_blank"> Click here </a>')
    
    def test_leaf_to_html_html(self):
        leaf = LeafNode("html", "Test")
        self.assertEqual(leaf.to_html(), '<html> Test </html>')

    def test_leaf_to_html_none(self):
        leaf = LeafNode(None, "Hello, world!")
        self.assertEqual(leaf.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()