"""
Crea una función que imprima los 30 próximos años bisiestos
    siguientes a uno dado.
- Utiliza el menor número de líneas para resolver el ejercicio.
"""

def print_leap_years(year: int, count: int = 30) -> None:
    """
    Prints the next N leap years starting from a given year.

    Args:
        year (int): The starting year (must be a positive integer).
        count (int, optional): Number of leap years to print. Defaults to 30.

    Raises:
        ValueError: If year or count are not valid positive integers.
    """

    if not isinstance(year, int) or year <= 0:
        raise ValueError("Ha ocurrido un error. Ingrese una fecha valida.")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Ha ocurrido un error. Ingrese un digito correcto.")

    while count > 0:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year)
            count -= 1
        year += 1

if __name__ == "__main__":
    print_leap_years(2025)
