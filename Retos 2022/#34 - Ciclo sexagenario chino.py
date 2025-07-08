"""
Crea un función, que dado un año, indique el elemento 
    y animal correspondiente en el ciclo sexagenario del zodíaco chino.
- Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
- El ciclo sexagenario se corresponde con la combinación de los elementos
    madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
    conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
    (en este orden).
Cada elemento se repite dos años seguidos.
El último ciclo sexagenario comenzó en 1984 (Madera Rata).
"""

def validate_data(year: int, cycle_start: int) -> None:
    """
    Validates that the input year and cycle_start are positive integers.

    Args:
        year (int): The target year.
        cycle_start (int): The base year of the 60-year cycle.

    Raises:
        ValueError: If any of the inputs are not valid positive integers.
    """
    if not isinstance(year, int) or year <= 0:
        raise ValueError("El año ingresado debe ser un entero positivo.")
    if not isinstance(cycle_start, int) or cycle_start <= 0:
        raise ValueError("El ciclo debe iniciar con un entero positivo.")

def chinese_sexagenary(year: int, cycle_start: int = 1984) -> dict[str, str]:
    """
    Returns the Chinese zodiac element and animal corresponding to the given year,
    based on the 60-year sexagenary cycle starting from 1984 (Wood Rat).

    Args:
        year (int): The year to analyze.
        cycle_start (int, optional): The base year of the cycle. Default is 1984.

    Returns:
        dict[str, str]: A dictionary containing the 'animal' and 'element'.
    """
    animals = [
        "Rata", "Buey", "Tigre", "Conejo", "Dragon", "Serpiente", "Caballo", "Oveja", "Mono", "Gallo", "Perro", "Cerdo"
        ]

    elements = [
        "Madera", "Madera", "Fuego", "Fuego", "Tierra", "Tierra", "Metal", "Metal", "Agua", "Agua"
        ]

    validate_data(year, cycle_start)

    cycle_offset  = (year - cycle_start) % 60

    return {"animal": animals[cycle_offset  % 12],"elemento": elements[cycle_offset  % 10]}

if __name__ == "__main__":
    print(chinese_sexagenary(1984))
