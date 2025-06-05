"""
Crea un programa se encargue de transformar un número
    decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def decimal_to_binarie(num: int) -> None:
    """
    Converts a decimal number to its binary representation.

    Parameters:
    num (int): The decimal number to be converted.

    Returns:
    None: The function directly prints the binary representation.
    """
    binarie = []
    while num >= 1:
        residue = num % 2
        binarie.append(residue)
        num = num // 2

    for i in range(len(binarie) - 1, -1, -1):
        print(binarie[i], end= "")

decimal_to_binarie(25)
