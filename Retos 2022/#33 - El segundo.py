"""
Dado un listado de números, encuentra el SEGUNDO más grande
"""

def validate_data(numbers: list[int]) -> None:
    """
    Validates that the input is a list of integers.

    Args:
        numbers (list[int]): The list to validate.

    Raises:
        TypeError: If the input is not a list of integers.
    """
    if not isinstance(numbers, list) or not all(isinstance(number, int) for number in numbers):
        raise TypeError("Los datos ingresados deben ser una lista de enteros.")

def second_greater(numbers: list[int]) -> int:
    """
    Returns the second largest unique number from the input list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The second highest unique value in the list.

    Raises:
        ValueError: If the list has fewer than two unique values.
    """
    validate_data(numbers)

    if len(numbers) < 2:
        raise ValueError("La lista debe contener al menos dos valores únicos.")

    sorted_num = sorted(set(numbers), reverse=True)

    return sorted_num[1]

if __name__ == "__main__":
    number_list = [2, 4, 2, 1, 5, 7, 6]
    print(f"El segundo numero mas grande de la lista es {second_greater(number_list)}.")
