"""
Crea un programa que calcule el daño de un ataque durante
    una batalla Pokémon.
- La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
- Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
- Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
    (buscar su efectividad)
- El programa recibe los siguientes parámetros:
- Tipo del Pokémon atacante.
- Tipo del Pokémon defensor.
- Ataque: Entre 1 y 100.
- Defensa: Entre 1 y 100.
"""
from typing import Literal

PokemonType = Literal["Agua", "Fuego", "Planta", "Electrico"]
pokemon_types  = ["Agua", "Fuego", "Planta", "Electrico"]

effectiveness_chart = {
    "Agua": {"Fuego": 2, "Planta": 0.5, "Electrico": 1, "Agua": 0.5},
    "Fuego": {"Planta": 2, "Agua": 0.5, "Electrico": 1, "Fuego": 0.5},
    "Planta": {"Agua": 2, "Fuego": 0.5, "Electrico": 1, "Planta": 0.5},
    "Electrico": {"Agua": 2, "Planta": 0.5, "Fuego": 1, "Electrico": 0.5},
}

def validate_data(attacker: str, defender: str, attack: int, defense: int) -> None:
    """
    Validates Pokémon types and stats.

    Args:
        attacker (str): Attacker type.
        defender (str): Defender type.
        attack (int): Attack value (1 - 100).
        defense (int): Defense value (1 - 100).

    Raises:
        ValueError: If types or stats are invalid.
    """
    if attacker not in pokemon_types or defender not in pokemon_types:
        raise ValueError("Tipos válidos: 'Agua', 'Fuego', 'Planta', 'Electrico'.")
    if not isinstance(attack, int) or not isinstance(defense, int):
        raise ValueError("El ataque y la defensa deben ser enteros.")
    if not 1 <= attack <= 100 or not 1 <= defense <= 100:
        raise ValueError("Los valores de ataque y defensa deben estar entre 1 y 100.")

def calculate_damage(attacker: PokemonType, defender: PokemonType, attack: int, defense: int) -> float:
    """
    Calculates Pokémon damage based on types and stats.

    Args:
        attacker (PokemonType): Type of the attacking Pokémon.
        defender (PokemonType): Type of the defending Pokémon.
        attack (int): Attack stat (1 - 100).
        defense (int): Defense stat (1 - 100).

    Returns:
        float: Total damage rounded to 2 decimals.
    """
    validate_data(attacker, defender, attack, defense)
    effectiveness = effectiveness_chart[attacker][defender]
    damage = 50 * (attack / defense) * effectiveness
    return round(damage, 2)


if __name__ == "__main__":
    print(f"Total de daño: {calculate_damage('Agua', 'Electrico', 50, 23)}")
