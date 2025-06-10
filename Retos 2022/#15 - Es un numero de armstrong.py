"""
Escribe una función que calcule si un número dado es un número de Armstrong
    (o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información
    al respecto.
"""

def is_armstrong_number(number: int) -> bool:
    """
    Determines whether a given number is an Armstrong (narcissistic) number.

    Args:
        number (int): A non-negative integer.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    if number < 0:
        return False
    digits = str(number)
    num_digits = len(digits)
    count = sum(int(digit) ** num_digits for digit in digits)

    return count == number

if __name__ == "__main__":
    print(is_armstrong_number(153))
    print(is_armstrong_number(8))
    print(is_armstrong_number(18))
    print(is_armstrong_number(-153))
