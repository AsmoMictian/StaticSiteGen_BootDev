from enum import Enum

class TextType(Enum):
    NormalType = "normal"
    BoldType = "bold"
    ItalicType = "italic"
    CodeType = "code"
    LinksType = "links"
    ImagesType = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        #Confirm other is a TextNode
        #If it is, continue. Otherwise, return False
        if not isinstance(other, TextNode):
            return False
        
        #After confirming type, do an explicit comparison
        #If everything matches, return True. Else, return False.
        return (
        self.text == other.text and
        self.text_type == other.text_type and
        self.url == other.url
    )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"