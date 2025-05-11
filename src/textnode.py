from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        if self.text == node.text\
            and self.text_type == node.text_type\
            and self.url == node.url:
            return True
        return False

    def __repr__(self):
        return f'TextNode("{self.text}", {self.text_type.value}, "{self.url}")'

    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, {'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', '', props={'src': text_node.url, 'alt': text_node.text})
    raise Exception('Unknown TextType value')
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for n in old_nodes:
        if n.text_type is not TextType.TEXT:
            nodes.append(old_nodes)
            continue

        blocks = n.text.split(delimiter)
        
        if len(blocks) != 3:
            raise Exception(f'Invalid Markdown: no closing "{delimiter}"')
        
        nodes = [
            TextNode(blocks[0], TextType.TEXT), 
            TextNode(blocks[1], text_type), 
            TextNode(blocks[2], TextType.TEXT), 
        ]
    return nodes