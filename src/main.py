from textNode import TextNode


def main():
    node = TextNode("this is a special test", "link", "https://www.google.com")
    print(node.__repr__())


main()