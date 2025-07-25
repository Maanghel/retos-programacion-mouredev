"""
Escribe una función que calcule y retorne el factorial de un número dado
    de forma recursiva.
"""

def recursion_factorial(num: int) -> int:
    """
    Recursively computes the factorial of a given non-negative integer.

    Args:
        num (int): A non-negative integer.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If the input is a negative integer.
    """
    if num < 0:
        raise ValueError("El factorial no esta definido para numeros negativos.")
    if num in (0, 1):
        return 1
    return num * recursion_factorial(num - 1)


if __name__ == "__main__":
    print(recursion_factorial(6))
    print(recursion_factorial(0))
    # print(recursion_factorial(1))
