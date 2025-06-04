import re
from enum import Enum

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
    return list(map(
        lambda x : x.strip(), blocks
    ))

