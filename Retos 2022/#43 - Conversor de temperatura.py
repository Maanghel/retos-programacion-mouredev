"""
Crea una función que transforme grados Celsius en Fahrenheit
    y viceversa.
- Para que un dato de entrada sea correcto debe poseer un símbolo "°"
    y su unidad ("C" o "F").
- En caso contrario retornará un error.
"""

def grades_converter(grades: str, unit: str) -> float | str:
    """
    Converts a temperature value between Celsius and Fahrenheit.

    Parameters:
        grades (str): A temperature string that includes the degree symbol, e.g., "100°".
        unit (str): The original temperature unit. Must be either "C" or "F" (case-insensitive).

    Returns:
        float: The converted temperature rounded to 2 decimal places.
        str: "Error" if inputs are invalid or conversion fails.
    """
    if not isinstance(grades, str) or not isinstance(unit, str):
        return "Error"
    if "°" not in grades:
        return "Error"

    unit = unit.upper()
    if unit not in ("C", "F"):
        return "Error"

    try:
        temp = float(grades.replace("°", ""))
    except ValueError:
        return "Error"

    if unit == "C":
        return round((temp * 9/5) + 32, 2)
    else:
        return round((temp - 32) * 5/9, 2)


if __name__ == "__main__":
    print(grades_converter("55°", "C"))
