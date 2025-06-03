"""
Escribe una función que reciba dos palabras (String) y retorne
    verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word1: str, word2: str) -> bool:
    word1 = word1.lower()
    word2 = word2.lower()

    if word1 == word2:
        return False

    return sorted(word1) == sorted(word2)

text1 = "cara"
text2 = "arc"
print(is_anagram(text1, text2))
