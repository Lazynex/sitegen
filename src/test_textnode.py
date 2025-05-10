import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, 'url')
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)
        
    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_is_not_eq(self):
        node = TextNode("This is not a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()