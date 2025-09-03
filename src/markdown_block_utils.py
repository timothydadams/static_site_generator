import re
from enum import Enum
from htmlNode import ParentNode
from markdown_inline_utils import text_to_nodes
from textNode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

def check_for_ordered_list(line):
    if line[1].startswith(f"{line[0] + 1}. "):
        return True
    return False

def block_to_block_type(block):
    heading_prefixes = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    lines = block.splitlines()

    if block.startswith(tuple(heading_prefixes)):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(map(lambda x: x.startswith(">"), lines )):
        return BlockType.QUOTE
    elif all(map(lambda x: x.startswith("- "), lines )):
        return BlockType.UL
    elif all(map(check_for_ordered_list, enumerate(lines) )):
        return BlockType.OL
    else:
        return BlockType.PARAGRAPH

def normalize_endings(text):
    return text.replace("\r\n", "\n").replace("\r", "\n")

def markdown_to_blocks(markdown):
    normalized_markdown = normalize_endings(markdown)
    blocks = re.split(r"[\n]{2,}", normalized_markdown)
    return list(
        filter(
            lambda x: x != "", map(
                lambda x : x.strip(), blocks
            )
        )
    )

def block_to_html_node(block):
    type = block_to_block_type(block)
    if type == BlockType.PARAGRAPH:
        return paragraph_to_html(block)
    if type == BlockType.HEADING:
        return heading_to_html(block)
    if type == BlockType.CODE:
        return code_to_html(block)
    if type == BlockType.OL:
        return ol_to_html(block)
    if type == BlockType.UL:
        return ul_to_html(block)
    if type == BlockType.QUOTE:
        return quote_to_html(block)
    raise ValueError("invalid block type")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def text_to_children(text):
    text_nodes = text_to_nodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_html(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def ul_to_html(block):
    list_items = block.split("\n")
    html_items = []
    for item in list_items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def ol_to_html(block):
    list_items = block.split("\n")
    html_items = []
    for item in list_items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def quote_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid block quote")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)