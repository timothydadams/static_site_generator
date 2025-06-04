import unittest
from markdown_block_utils import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockType(unittest.TestCase):
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UL)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OL)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_blocks_to_block_type(self):
        blocks = [
                "# This is **bolded** paragraph",
                "## This is another paragraph",
                "- This is a list\n- with items",
                ">Just another day in the\n>office",
                "1. line one\n2. line two\n3. line three\n4. line four",
                "3. wrong ordered\n5. test",
                "```i am code```",
        ]
        block_types = list(map(block_to_block_type, blocks))
        self.assertEqual(
            block_types,
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.UL,
                BlockType.QUOTE,
                BlockType.OL,
                BlockType.PARAGRAPH,
                BlockType.CODE
            ],
        )


if __name__ == "__main__":
    unittest.main()