from htmlNode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        has_props = self.props != None
        if self.value==None:
            raise ValueError("leaf nodes must have a value")
        if self.tag==None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html() if has_props else ''}>{self.value}</{self.tag}>"