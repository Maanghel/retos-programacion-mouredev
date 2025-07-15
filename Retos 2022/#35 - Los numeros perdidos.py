"""
Dado un array de enteros ordenado y sin repetidos,
crea una función que calcule y retorne todos los que faltan entre
    el mayor y el menor.
- Lanza un error si el array de entrada no es correcto.
"""

def validate_array(array: list[int]) -> None:
    """
    Validates that the input list is a non-empty, sorted list of unique integers with at least two elements.

    Args:
        array (List[int]): The input list of integers.

    Raises:
        TypeError: If input is not a list of integers.
        ValueError: If list is not sorted, has duplicates, or has fewer than 2 elements.
    """
    if not isinstance(array, list) or not all(isinstance(num, int) for num in array):
        raise TypeError("Ha ocurrido un error. Solo se acepta una lista con enteros.")

    if any(array[i] > array[i + 1] for i in range(len(array) - 1)):
        raise ValueError("Ha ocurrido un error. Los enteros deben de estar ordenados de menor a mayor.")

    if len(set(array)) != len(array):
        raise ValueError("Ha ocurrido un error. No debe haber duplicados en la lista de enteros.")

    if len(array) <= 1:
        raise ValueError("Ha ocurrido un error. La lista debe contener minimo 2 enteros.")

def missing_integers(array: list[int]) -> list[int]:
    """
    Returns a list of missing integers between the smallest and largest values in a sorted input list.

    Args:
        array (List[int]): Sorted list of unique integers.

    Returns:
        List[int]: Missing integers between array[0] and array[-1], exclusive.
    """
    validate_array(array)

    missing_numbers = [num for num in range(array[0] + 1, array[-1]) if num not in array]

    return missing_numbers


if __name__ == "__main__":
    print(missing_integers([1, 2, 5]))
