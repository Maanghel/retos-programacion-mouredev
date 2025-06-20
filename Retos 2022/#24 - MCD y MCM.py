"""
Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
    que calcule el mínimo común múltiplo (mcm) de dos números enteros.
- No se pueden utilizar operaciones del lenguaje que
    lo resuelvan directamente.
"""

def mcd(num1: int, num2: int) -> int:
    """
    Manually calculates the Greatest Common Divisor (GCD) of two integers
    using the Euclidean algorithm.

    Parameters:
        num1 (int): First integer.
        num2 (int): Second integer.

    Returns:
        int: The greatest common divisor.

    Raises:
        ValueError: If inputs are not integers.
    """
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Ambos valores deben ser enteros.")

    if num1 < 0:
        num1 = -num1
    if num2 < 0:
        num2 = -num2

    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder

    return num1


def mcm(num1: int, num2: int) -> int:
    """
    Manually calculates the Least Common Multiple (LCM) of two integers
    using the formula: LCM(a, b) = (|a * b|) // GCD(a, b).

    Parameters:
        num1 (int): First integer.
        num2 (int): Second integer.

    Returns:
        int: The least common multiple.

    Raises:
        ValueError: If inputs are not integers.
    """
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Ambos valores deben ser enteros.")

    if num1 == 0 or num2 == 0:
        return 0

    product = num1 * num2
    if product < 0:
        product = -product

    gcd = mcd(num1, num2)

    return product // gcd


if __name__ == "__main__":
    print("MCD(12, 18):", mcd(12, 18))
    print("MCM(3, 5):", mcm(3, 5))
