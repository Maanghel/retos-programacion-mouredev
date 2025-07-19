"""
¡La Tierra Media está en guerra! En ella lucharán razas leales
    a Sauron contra otras bondadosas que no quieren que el mal reine
    sobre sus tierras.
Cada raza tiene asociado un "valor" entre 1 y 5:
- Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
    Númenóreanos (4), Elfos (5)
- Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
    Huargos (3), Trolls (5)
Crea un programa que calcule el resultado de la batalla entre
    los 2 tipos de ejércitos:
- El resultado puede ser que gane el bien, el mal, o exista un empate.
    Dependiendo de la suma del valor del ejército y el número de integrantes.
- Cada ejército puede estar compuesto por un número de integrantes variable
    de cada raza.
- Tienes total libertad para modelar los datos del ejercicio.
    Ej: 1 Peloso pierde contra 1 Orco
        2 Pelosos empatan contra 1 Orco
        3 Pelosos ganan a 1 Orco
"""

from enum import Enum
from typing import Dict, Literal

class ArmyType(Enum):
    """
    Enum representing the different races involved in the Middle-Earth battle.
    Divided into good (GOD_RACES) and evil (EVIL_RACES) factions.
    """
    PELOSOS = "Pelosos"
    SURBUENOS = "Sureños buenos"
    ENANOS = "Enanos"
    NUMENOREANOS = "Numenoreanos"
    ELFOS = "Elfos"
    SURMALOS = "Sureños malos"
    ORCOS = "Orcos"
    GOBLINS = "Goblins"
    HUARGOS = "Huargos"
    TROLLS = "Trolls"

GOD_RACES = {
    ArmyType.PELOSOS: 1,
    ArmyType.SURBUENOS: 2,
    ArmyType.ENANOS: 3,
    ArmyType.NUMENOREANOS: 4,
    ArmyType.ELFOS: 5
}

EVIL_RACES = {
    ArmyType.SURMALOS: 2,
    ArmyType.ORCOS: 2,
    ArmyType.GOBLINS: 2,
    ArmyType.HUARGOS: 3,
    ArmyType.TROLLS: 5
}

RESULT_OPTION = Literal["Buenos", "Malos", "Empate"]

def validate_data(god_army: Dict[ArmyType, int], evil_army: Dict[ArmyType, int]) -> None:
    """
    Validates the armies' composition and integrity.

    Args:
        god_army (Dict[ArmyType, int]): Dictionary mapping good races to their unit counts.
        evil_army (Dict[ArmyType, int]): Dictionary mapping evil races to their unit counts.

    Raises:
        TypeError: If either input is not a dictionary.
        ValueError: If an army is empty, contains invalid races, or units are not positive integers.
    """
    if not isinstance(god_army, dict) or not isinstance(evil_army, dict):
        raise TypeError("Ha ocurrido un error. Solo se admite un diccionario de datos.")

    if not god_army or not evil_army:
        raise ValueError("Ha ocurrido un error. Los ejercitos deben tener al menos una raza en sus lineas.")

    if not all(race in GOD_RACES for race in god_army.keys()):
        raise ValueError("Ha ocurrido un error. El ejercito bueno solo acepta razas buenas.")
    if not all(race in EVIL_RACES for race in evil_army.keys()):
        raise ValueError("Ha ocurrido un error. El ejercito malo solo acepta razas malas.")

    if not all(isinstance(count, int) and count > 0 for count in god_army.values()):
        raise ValueError("Ha ocurrido un error. Las cantidades deben ser enteros positivos.")
    if not all(isinstance(count, int) and count > 0 for count in evil_army.values()):
        raise ValueError("Ha ocurrido un error. Las cantidades deben ser enteros positivos.")

def battle(god_army: Dict[ArmyType, int], evil_army: Dict[ArmyType, int]) -> RESULT_OPTION:
    """
    Calculates the battle outcome between the good and evil armies.

    The outcome is determined by summing the product of each race's value
    and its number of units. The higher total wins.

    Args:
        god_army (Dict[ArmyType, int]): The good army composition.
        evil_army (Dict[ArmyType, int]): The evil army composition.

    Returns:
        Literal["Buenos", "Malos", "Empate"]: Result of the battle.
    """
    validate_data(god_army, evil_army)

    god_score = sum(GOD_RACES[race] * count for race, count in god_army.items())
    evil_score = sum(EVIL_RACES[race] * count for race, count in evil_army.items())

    if god_score > evil_score:
        return "Buenos"
    elif evil_score > god_score:
        return "Malos"
    else:
        return "Empate"


if __name__ == "__main__":
    good = {
        ArmyType.PELOSOS: 3,
        ArmyType.ELFOS: 1
    }

    evil = {
        ArmyType.ORCOS: 2,
        ArmyType.TROLLS: 1
    }

    print("Ganador:", battle(good, evil))  # Output: "Malos"
