import unittest

from htmlnode import HTMLNode


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
        self.assertEqual(str(node), 'HTMLNode(div, Center, [HTMLNode(div, Right, None, " class=\"right\"")], " class=\"center\"")')

    def test_not_dict(self):
        node = HTMLNode(props=1)
        self.assertEqual(str(node), 'HTMLNode(None, None, None, "")')
if __name__ == "__main__":
    unittest.main()