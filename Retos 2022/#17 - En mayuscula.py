"""
Crea una función que reciba un String de cualquier tipo y se encargue de
    poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que
    lo resuelvan directamente.
"""

def upper(text: str) -> str:
    """
    Converts the first letter of each word in a text to uppercase, without using
    built-in language functions that perform this operation directly.

    The function iterates over each word in the text, and if the first character
    is a lowercase English letter, it replaces it with its uppercase equivalent
    using a mapping dictionary. If the word starts with a symbol, number, or 
    already has the first letter in uppercase, it remains unchanged.

    Args:
        text (str): The input string to be processed.

    Returns:
        str: A new string with the first letter of each word converted to uppercase,
            preserving the rest of the original content.
    """
    uppercase_map = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D',
        'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
        'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
        'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P',
        'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
        'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
        'y': 'Y', 'z': 'Z'
    }

    word_list = text.split()
    new_text = []

    for word in word_list:
        if word and word[0] in uppercase_map:
            list_word = list(word)
            list_word[0] = uppercase_map.get(list_word[0], list_word[0])
            new_text.append("".join(list_word))
        else:
            new_text.append(word)

    return " ".join(new_text)

if __name__ == "__main__":
    capitalize_text = upper("hola a todos, seguimos aprendiendo python!")
    print(capitalize_text)
