"""
Crea un programa que invierta el orden de una cadena de texto
    sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse_text(text: str) -> str:
    """
    Reverses the given text.

    This function takes a string as input and returns a new string
    with the characters in reverse order.

    Parameters:
    - text : str
        The input string to be reversed.

    Returns:
    - str: The reversed string.
    """
    reverse = ""
    for char in text:
        reverse = char + reverse
    return reverse


if __name__ == "__main__":
    print(reverse_text("Hola mundo"))
