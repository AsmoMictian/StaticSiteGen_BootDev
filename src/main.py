from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.LinksType, "https://mywebsitehere.com")
    print(node)

if __name__ == "__main__":
    main()