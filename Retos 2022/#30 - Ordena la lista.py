"""
Crea una función que ordene y retorne una matriz de números.
- La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
    adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
    o de mayor a menor.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan
    automáticamente.
"""

from typing import Literal, List

SortOption = Literal["Asc", "Desc"]

def validate_data(arr: List[int], sort: SortOption) -> None:
    """
    Validates input data for the sorting function.

    Args:
        arr (List[int]): The list to validate.
        sort (SortOption): The sorting order ("Asc" or "Desc").

    Raises:
        TypeError: If arr is not a list of integers or if sort is invalid.
    """
    if not isinstance(arr, list) or not all(isinstance(number, int) for number in arr):
        raise TypeError("Solo se admite una lista de numeros enteros.")

    if sort not in ("Asc", "Desc"):
        raise TypeError("El tipo de ordenamiento debe ser 'Asc' o 'Desc'.")

def sort_list(arr: List[int], sort: SortOption = "Asc") -> list[int]:
    """
    Sorts a list of integers using the Quicksort algorithm.

    Args:
        arr (List[int]): The list to sort.
        sort (SortOption): Sorting order. "Asc" for ascending, "Desc" for descending.

    Returns:
        List[int]: The sorted list.

    Raises:
        TypeError: If validation fails.
    """
    validate_data(arr, sort)

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    if sort == "Asc":
        return sort_list(left, sort) + [pivot] + sort_list(right, sort)
    elif sort == "Desc":
        return sort_list(right, sort) + [pivot] + sort_list(left, sort)

lista_desordenada = [5, 2, 8, 1, 9, 4, 7, 3, 6]
lista_ordenada = sort_list(lista_desordenada, "Asc")
print(f"Lista desordenada: {lista_desordenada}")
print(f"Lista ordenada: {lista_ordenada}")