"""
Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes
    de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes
    de los dos array.
- No se pueden utilizar operaciones del lenguaje que
    lo resuelvan directamente.
"""

from typing import Any, List

def is_list(arr: List[Any]) -> bool:
    """
    Checks whether the given object is a list.

    Args:
        arr (Any): The object to check.

    Returns:
        bool: True if the object is a list, False otherwise.
    """
    return isinstance(arr, list)

def common_or_not(arr1: List[Any], arr2: List[Any], boolean: bool) -> List[Any]:
    """
    Returns a list of either common or non-common elements between two input lists,
    based on the given boolean flag.

    Args:
        arr1 (List[Any]): The first input list.
        arr2 (List[Any]): The second input list.
        boolean (bool): If True, returns elements common to both lists.
                        If False, returns elements not shared between the lists.

    Returns:
        List[Any]: A list containing either the common or non-common elements.

    Raises:
        TypeError: If either arr1 or arr2 is not a list.
    """

    for arr in [arr1, arr2]:
        if not is_list(arr):
            raise TypeError("Tipo de dato incorrecto. Solo se aceptan listas.")

    result = []

    if boolean:
        for element in arr1:
            if element in arr2 and element not in result:
                result.append(element)
    else:
        for element in arr1:
            if element not in arr2 and element not in result:
                result.append(element)
        for element in arr2:
            if element not in arr1 and element not in result:
                result.append(element)

    return result


if __name__ == "__main__":
    print(common_or_not([1, 2, 3, 4, 5], [4, 5, 6, 7, 8], True))
    print(common_or_not([1, 2, 3], [3, 4, 5], False))
