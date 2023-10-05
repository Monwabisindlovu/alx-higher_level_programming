#!/usr/bin/python3
def text_indentation(text):
    """
    Print a text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    result = ""
    new_line = True

    for char in text:
        if char in punctuation_chars:
            result += char + "\n\n"
            new_line = True
        else:
            if new_line and char == ' ':
                continue
            result += char
            new_line = False

    print(result, end="")

if __name__ == "__main__":
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres"""
    text_indentation(text)

