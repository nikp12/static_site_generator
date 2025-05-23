import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
#     def test_eq(self):
#       node = TextNode("This is a text node", TextType.BOLD)
#       node2 = TextNode("This is a text node", TextType.BOLD)
#     self.assertEqual(node, node2) 

    def test_tag(self):       
        node = HTMLNode("**",)
        print(node.props_to_html)

    def test_value(self):
        node = HTMLNode(value="**")
        print(node.props_to_html)

    def test_children(self):
        node = HTMLNode(children="**")
        print(node.props_to_html)

    def test_props(self):
        node = HTMLNode(props="**")
        print(node.props_to_html)

if __name__ == "__main__":
    unittest.main()