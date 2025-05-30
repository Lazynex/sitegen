class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        if isinstance(self.props, dict):
            for key, value in self.props.items():
                html += f' {key}="{value}"'
        return html
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, "{self.props_to_html()}")'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError('value cannot be empty!')
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError('tag cannot be empty!')
        if not self.children:
            raise ValueError('children cannot be empty!')
        html = ''
        for c in self.children:
            html += c.to_html()
        return f'<{self.tag}{self.props_to_html()}>{html}</{self.tag}>'