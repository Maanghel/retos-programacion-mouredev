"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime(number: int) -> bool:
    """
    Check if a number is prime.

    A prime number is greater than 1 and divisible only by 1 and itself.

    Parameters:
    - number (int): The number to check.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for x in range(2, int(number**0.5) + 1):
        if number % x == 0:
            return False
    return True

for i in range(1, 101):
    if is_prime(i):
        print(i)
