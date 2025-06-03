import re
from textNode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimeter)
        if len(sections) % 2 == 0:
            raise Exception("invalid markdown, section was not properly closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append( TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append( TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append( node )
            continue
        initial_text = node.text
        images = extract_markdown_images(initial_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for description, url in images:
            sections = initial_text.split(f"![{description}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append( TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(description, TextType.IMAGE, url))
            initial_text = sections[1]
        if initial_text != "":
            new_nodes.append( TextNode(initial_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = [] 
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append( node )
            continue
        initial_text = node.text
        links = extract_markdown_links(initial_text)
        if len(links) == 0:
            new_nodes.append( node )
            continue
        for display_text, url in links:
            sections = initial_text.split(f"[{display_text}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append( TextNode(sections[0], TextType.TEXT))
            new_nodes.append( TextNode(display_text, TextType.LINK, url))
            initial_text = sections[1]
        if initial_text != "":
            new_nodes.append( TextNode(initial_text, TextType.TEXT))
    return new_nodes


def text_to_nodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

