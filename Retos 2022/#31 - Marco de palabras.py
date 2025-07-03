"""
Crea una función que reciba un texto y muestre cada palabra en una línea,
    formando un marco rectangular de asteriscos.
- ¿Qué te parece el reto? Se vería así:
**********
* ¿Qué   *
* te     *
* parece *
* el     *
* reto?  *
**********
"""

def validate_data(text: str) -> None:
    """
    Validates that the input is a string and that it is not empty.

    Args:
        text (str): The input to validate.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or consists only of whitespace.
    """
    if not isinstance(text, str):
        raise TypeError("Solo se admite datos de tipo texto.")
    if not text.strip():
        raise ValueError("Debe de ingresar un texto.")

def word_frame(text: str) -> None:
    """
    Prints a list of words from the input text inside a framed box made of asterisks.

    The function splits the input text into words and then prints them one by one inside
    a rectangular frame of asterisks. The longest word determines the width of the frame.

    Args:
        text (str): The input text to frame, split by spaces.

    Raises:
        ValueError: If the input text is empty or consists only of whitespace.

    Example:
        >>> word_frame("Hello world")
        **********
        * Hello  *
        * world  *
        **********
    """
    validate_data(text)

    word_list = text.strip().split()

    max_length = max(len(word) for word in word_list)

    border = "*" * (max_length + 4)

    print(f"\n{border}")
    for word in word_list:
        print(f"* {word.ljust(max_length)} *")
    print(border)


if __name__ == "__main__":
    word_frame("¿Que te parece el reto?")
    word_frame("  hola     mundo   ")
    word_frame("X")
    word_frame("¡Hola! ¿Cómo estás?")
    word_frame("hipopotomonstrosesquipedaliofobia corto")
