#!/usr/bin/python3
    """Pnts text with two new lines each of thess charaters:. , ? :"""


    def text_indentation(text):
        """A function that prints two new lines after the char ...
        :param text:
        :type text:; string
        :raise TypeError: if text is not a string
        """
        if not isinstance(text, str):
           raise TypeError("text must be a string")
        
        i = 0
        while i < len(text) and text[i] == ' ':
            i += 1
        while i < len(text):
            print(text[i], end="")
            if text[i] == "\n" or text[i] in ".?:":
                if text[i] in ".?;":
                    print("\n")
                i += 1
                while i < len(text) and text[i] == ' ':
                    i += 1
                continue
            i += 1

