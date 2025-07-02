"""
Crea un programa que determine si dos vectores son ortogonales.
- Los dos array deben tener la misma longitud.
- Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def validate_data(arr1: list[int], arr2: list[int]) -> None:
    """
    Validates that both vectors are lists of exactly two numeric values.

    Parameters:
        arr1 (list[int]): First vector.
        arr2 (list[int]): Second vector.

    Raises:
        TypeError: If either input is not a list or if elements are not numeric.
        ValueError: If either vector does not have exactly two elements.
    """
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Ambos vectores deben ser listas.")

    if len(arr1) != 2 or len(arr2) != 2:
        raise ValueError("Los vectores deben tener exactamente 2 elementos.")

    if not all(isinstance(x, (int, float)) for x in arr1 + arr2):
        raise TypeError("Todos los elementos deben ser numéricos.")

def are_orthogonal_vectors(arr1: list[int], arr2: list[int] ) -> bool|None:
    """
    Determines whether two 2D vectors are orthogonal.

    Two vectors are orthogonal if their dot product is zero.

    Parameters:
        arr1 (list[int]): First vector.
        arr2 (list[int]): Second vector.

    Returns:
        bool | None: True if vectors are orthogonal, False if not, 
                    None if an exception is raised during validation.
    """
    try:
        validate_data(arr1, arr2)

        result = (arr1[0] * arr2[0]) + (arr1[1] * arr2[1])

        return result == 0
    except TypeError as e:
        print(f"Ha ocurrido un error. {e}")
    except ValueError as e:
        print(f"Ha ocurrido un error. {e}")

if __name__ == "__main__":
    print(are_orthogonal_vectors([1, 2], [2, -3]))
    print(are_orthogonal_vectors([1, 0], [0, 1]))
    print(are_orthogonal_vectors([2, 3], [-3, 2]))
