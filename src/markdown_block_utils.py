import re

def normalize_endings(text):
    return text.replace("\r\n", "\n").replace("\r", "\n")

def markdown_to_blocks(markdown):
    normalized_markdown = normalize_endings(markdown)
    blocks = re.split(r"[\n]{2,}", normalized_markdown)
    return list(map(
        lambda x : x.strip(), blocks
    ))