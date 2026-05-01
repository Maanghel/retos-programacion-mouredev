"""
Crea un programa que sea capaz de generar e imprimir todas las
    permutaciones disponibles formadas por las letras de una palabra.

- Las palabras generadas no tienen por qué existir.
- Deben usarse todas las letras en cada permutación.
- Ejemplo: sol, slo, ols, osl, los, lso
"""

def generate_permutations(word: str) -> None:
    """ Function to generate and print all permutations of a given word.

    Args:
        word (str): The input word for which to generate permutations.

    Raises:
        ValueError: If the input word is empty or exceeds 10 characters.
        TypeError: If the input word contains non-alphabetic characters.
    """
    if not word:
        raise ValueError("Error. El valor de entrada no puede estar vacio.")
    if not word.isalpha():
        raise TypeError("Error. Solo se aceptan letras del abecedario.")
    if len(word) > 10:
        raise ValueError("Error. La palabra es demasiado larga (max 10 letras).")

    word = word.lower()

    def backtrack(char_left: list, actual: list):
        if not char_left:
            print("".join(actual))
            return

        char_left = sorted(char_left)
        for i, char in enumerate(char_left):
            if i > 0 and char == char_left[i-1]:
                continue

            backtrack(char_left[:i] + char_left[i+1:], actual + [char])

    backtrack(list(word), [])

if __name__ == '__main__':
    word = 'HOLA'
    print('Mi funcion:')
    try:
        generate_permutations(word)
    except (ValueError, TypeError) as e:
        print(e)
