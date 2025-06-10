"""
Escribe una función que reciba un texto y retorne verdadero o
    falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
    de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
    Ejemplo: Ana lleva al oso la avellana.
"""

import unicodedata

def is_palindrome(text: str) -> bool:
    """
    Determines whether a given text is a palindrome.

    A palindrome is a word or phrase that reads the same forward and backward,
    ignoring spaces, punctuation, diacritical marks (accents), and case sensitivity.

    Args:
        text (str): The input text to evaluate.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    text = ''.join(
        char for char in unicodedata.normalize('NFD', text)
        if unicodedata.category(char) != 'Mn'
    )

    cleaned_text = "".join(
        char.lower() for char in text
        if char.isalnum()
        )

    return cleaned_text == cleaned_text[::-1]

print(is_palindrome("Ana, lleva al. oso la avellana!"))
