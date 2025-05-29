class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return " " + " ".join(
            list(
                map(
                    lambda key,val: f"{key}=\"{val}\"",
                    *zip(*self.props.items())
                )
            )
        )
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

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
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    
    def to_html(self):
        has_props = self.props != None
        if self.tag is None:
            raise ValueError("parent node must have a tag property")
        if self.children is None:
            raise ValueError("parent node must have children")
        return f"<{self.tag}{self.props_to_html() if has_props else ''}>{"".join([child.to_html() for child in self.children])}</{self.tag}>"
        