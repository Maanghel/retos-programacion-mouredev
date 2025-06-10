"""
Escribe una función que reciba dos palabras (String) y retorne
    verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word1: str, word2: str) -> bool:
    """
    Determine whether two words are anagrams of each other.

    An anagram is a word formed by rearranging all the letters of another word.
    This function returns False if the words are exactly the same or have different lengths.

    Parameters:
    - word1 (str): The first word to compare.
    - word2 (str): The second word to compare.

    Returns:
    - bool: True if the words are anagrams, False otherwise.
    """
    word1 = word1.lower()
    word2 = word2.lower()

    if word1 == word2:
        return False

    return sorted(word1) == sorted(word2)


if __name__ == "__main__":
    text1 = "cara"
    text2 = "arc"
    print(is_anagram(text1, text2))
