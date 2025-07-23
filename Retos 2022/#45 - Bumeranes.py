"""
Crea una función que retorne el número total de bumeranes de
    un array de números enteros e imprima cada uno de ellos.
- Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
    seguidos, en el que el primero y el último son iguales, y el segundo
    es diferente. Por ejemplo [2, 1, 2].
- En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2]
    y [4, 2, 4]).
"""

from typing import List

def validate_data(numbers: List[int]) -> None:
    """
    Validates that the input is a list of integers.

    Args:
        numbers (List[int]): The list to validate.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError("Solo se acepta una lista con enteros como valor.")
    if not all(isinstance(number, int) for number in numbers):
        raise ValueError("La lista solo puede incluir valores enteros.")

def find_boomerangs(numbers: List[int]) -> List[List[int]]:
    """
    Finds all boomerangs in a list of integers. A boomerang is a sequence of three
    consecutive numbers where the first and third are equal and the second is different.

    Args:
        numbers (List[int]): A list of integers to analyze.

    Returns:
        List[List[int]]: A list of all boomerang sequences found.
    """
    validate_data(numbers)
    total_bum = []
    for i in range(1, len(numbers) - 1):
        if numbers[i - 1] == numbers[i + 1] and numbers[i] != numbers[i - 1]:
            total_bum.append([numbers[i - 1], numbers[i], numbers[i + 1]])

    return total_bum


if __name__ == "__main__":
    try:
        numbers_list = [2, 1, 2, 3, 3, 4, 2, 4]
        for b in find_boomerangs(numbers_list):
            print(b)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
