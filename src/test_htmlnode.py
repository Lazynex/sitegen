import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode()
        node.props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr_img(self):
        node = HTMLNode()
        node.tag = 'img'
        node.props = {'src': 'src/image.jpg'}
        self.assertEqual(str(node), 'HTMLNode(img, None, None, " src=\"src/image.jpg\"")')

    def test_repr_a(self):
        node = HTMLNode()
        node.tag = 'a'
        node.value = 'Test'
        node.props = {'href': 'test.html'}
        self.assertEqual(str(node), 'HTMLNode(a, Test, None, " href=\"test.html\"")')

    def test_repr_div_children(self):
        node = HTMLNode()
        node.tag = 'div'
        node.value = 'Center'
        node.props = {'class': 'center'}
        node.children = [HTMLNode('div', 'Right', None, {'class': 'right'})]
        self.assertEqual(
            str(node),
            'HTMLNode(div, Center, [HTMLNode(div, Right, None, " class=\"right\"")], " class=\"center\"")'
        )

    def test_not_dict(self):
        node = HTMLNode(props=1)
        self.assertEqual(str(node), 'HTMLNode(None, None, None, "")')


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_no_value(self):
        node = LeafNode("a", None)
        self.assertRaises(ValueError)

    def test_leaf_no_value(self):
        node = LeafNode(None, 'Value')
        self.assertEqual(node.to_html(), 'Value')
    
    def test_leaf_children_instead_of_props(self):
        node = LeafNode("a", "Click me!", [HTMLNode()])
        self.assertEqual(node.to_html(), '<a>Click me!</a>')


class TestParentNode(unittest.TestCase):
    def test_node_and_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )
    
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

if __name__ == "__main__":
    unittest.main()