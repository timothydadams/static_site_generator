from enum import Enum
from htmlNode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

def check_by_name(attr_name):
    try:
        TextType[attr_name]
        return True
    except KeyError:
        return False
    
def check_by_value(attr_value):
    return attr_value in TextType._value2member_map_

def is_enum_member(var):
    return isinstance(var, TextType)

class TextNode:
    def __init__(self, text, text_type, url=None):
        if is_enum_member(text_type) == False:
            raise ValueError(f"invalid text type: {text_type}.  Must be one of {[t.value for t in TextType]}")
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
    
    def __eq__(self, other):
        compare_dict = other.__dict__
        for k,v in self.__dict__.items():
            if compare_dict[k] != v:
                return False
        return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    
def text_node_to_html_node(text_node):
        if not is_enum_member(text_node.text_type):
            raise Exception("not a vaild text node")
        
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {
                "src": text_node.url,
                "alt": text_node.text
            })