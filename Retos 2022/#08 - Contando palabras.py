"""
Crea un programa que cuente cuantas veces se repite cada palabra
    y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
    lo resuelvan automáticamente.
"""

def word_counter(text: str) -> dict:
    """
    Counts the number of times each word appears in a given text,
    ignoring case and excluding punctuation.

    This function performs manual processing to:
    - Convert uppercase letters to lowercase without using .lower().
    - Remove punctuation symbols.
    - Split the text into words without using .split().
    - Count word occurrences using basic logic.

    Args:
        text (str): The input string to analyze. It may contain mixed case words
                    and punctuation symbols.

    Returns:
        dict: A dictionary where each key is a word in lowercase, and each value
            is the number of times that word appears in the input text.
    """
    word_dict = {}
    puntuaction_signs = ".,;:!?¿'()"

    lowered_text = ""
    for char in text:
        if 'A' <= char <= 'Z':
            lowered_text += chr(ord(char) + 32)
        else:
            lowered_text += char

    cleaned_text = ""
    for char in lowered_text:
        if char not in puntuaction_signs:
            cleaned_text += char

    words = []
    word = ""
    for char in cleaned_text:
        if char != " ":
            word += char
        elif word:
            words.append(word)
            word = ""
    if word:
        words.append(word)

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


if __name__ == "__main__":
    TEXT = "Hola Hola, Python Hola!, h2la, PyThon, hola  "
    dict_ = word_counter(TEXT)

    for key, value in dict_.items():
        print(f"{key}: {value}")
