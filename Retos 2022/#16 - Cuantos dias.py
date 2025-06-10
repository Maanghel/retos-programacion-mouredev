"""
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
    de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
    lanzará una excepción.
"""

from datetime import datetime

def day_difference(date1: str, date2: str) -> int:
    """
    Calculates the absolute difference in days between two date strings
    in the format "dd/MM/yyyy".

    Args:
        date1 (str): A date string in "dd/MM/yyyy" format.
        date2 (str): A date string in "dd/MM/yyyy" format.

    Returns:
        int: Absolute number of days between the two dates.

    Raises:
        ValueError: If either string is not a valid date.
    """
    try:
        dt1 = datetime.strptime(date1, "%d/%m/%Y")
        dt2 = datetime.strptime(date2, "%d/%m/%Y")
    except ValueError as e:
        raise ValueError("Formato de fecha invalido. Se espera 'dd/MM/yyyy'.") from e

    return abs((dt1 - dt2).days)

if __name__ == "__main__":
    print(day_difference("01/06/2025", "06/06/2025"))
    print(day_difference("02/06/2025", "06/06/2025"))
    print(day_difference("03/06/2025", "06/06/2025"))
