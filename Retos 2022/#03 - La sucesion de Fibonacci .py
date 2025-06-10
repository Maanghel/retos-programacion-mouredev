"""
Escribe un programa que imprima los 50 primeros números de la sucesión
    de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci(count: int = 50) -> None:
    """
    Print the first `count` numbers of the Fibonacci sequence, starting from 0.

    The Fibonacci sequence is composed of numbers where each number is the sum
    of the two preceding ones. The sequence starts like this:
    0, 1, 1, 2, 3, 5, 8, 13...

    Parameters:
    - count (int): Number of Fibonacci numbers to print (default is 50).

    Returns:
    None
    """
    num1, num2 = 0, 1
    for _ in range(count):
        print(num1)
        num1, num2 = num2, num1 + num2


if __name__ == "__main__":
    fibonacci()
