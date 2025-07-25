"""
Crea un función que reciba un texto y retorne la vocal que
    más veces se repita.
- Ten cuidado con algunos casos especiales.
- Si no hay vocales podrá devolver vacío.
"""

VOWELS = ("a","e","i","o","u")

def validate_data(text: str) -> None:
    """
    Validates that the input is a string.

    Args:
        text (str): Input text to be validated.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Solo se acepta un texto como dato.")

def most_frequent_vowel(text: str) -> tuple|None:
    """
    Finds the vowel(s) that appear most frequently in the input text.

    Args:
        text (str): The text to analyze.

    Returns:
        tuple | None: A tuple with two elements:
            - A list of the most frequent vowel(s) in the text.
            - The number of times they appear.
        Returns None if no vowels are present or if the input is empty.
    """
    validate_data(text)
    if not text:
        return None

    text_vowels = {}
    for char in text.lower():
        if char in VOWELS:
            if char in text_vowels:
                text_vowels[char] += 1
            else:
                text_vowels[char] = 1

    if not text_vowels:
        return None

    max_freq = max(text_vowels.values())
    more_freq_vowels = [vowel for vowel, freq in text_vowels.items() if freq == max_freq]

    return (more_freq_vowels, max_freq)


if __name__ == "__main__":
    samples = [
        "Hola Python",          # o aparece dos veces
        "BCDFG",                # No vowels
        "",                     # Empty string
        "AeiouAEIOUaeiou",      # All vowels, same frequency
        "aaaeeeiiiooo",         # a, e, i, o with same freq, u missing
        1,                      # TypeError
    ]

    for s in samples:
        try:
            result = most_frequent_vowel(s)
            print(f"Input: {s}\nResult: {result}\n")
        except TypeError as e:
            print(f"Error: {e}")
