"""
Dado un array de números enteros positivos, donde cada uno
    representa unidades de bloques apilados, debemos calcular cuantas unidades
    de agua quedarán atrapadas entre ellos.
- Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].

 *         ⏹
 *         ⏹
 *   ⏹💧💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹⏹⏹

Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
    de agua. Suponemos que existe un suelo impermeable en la parte inferior
    que retiene el agua.
"""

from typing import List

def validate_data(heights: List[int]) -> None:
    """
    Validates that the input is a list of integers.

    Args:
        heights (List[int]): The list to validate.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    if not isinstance(heights, list):
        raise TypeError("Solo se acepta una lista con enteros como valor.")
    if not heights or len(heights) < 3:
        raise ValueError("La lista debe contener un minimo de 3 enteros.")
    if not all(isinstance(height, int) for height in heights):
        raise ValueError("La lista solo puede incluir valores enteros.")

def trapped_water(heights: List[int]) -> int:
    """
    Calculates the total amount of water that can be trapped between blocks.

    Args:
        heights (List[int]): List of positive integers representing block heights.

    Returns:
        int: Total units of trapped water.
    """
    validate_data(heights)

    n = len(heights)
    max_left = [0] * n
    max_right = [0] * n
    water_trapped = 0

    max_left[0] = heights[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], heights[i])

    max_right[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], heights[i])

    for i in range(n):
        water_level = min(max_left[i], max_right[i])
        if water_level > heights[i]:
            water_trapped += water_level - heights[i]

    return water_trapped


if __name__ == "__main__":
    try:
        heights = [4, 0, 3, 6, 1, 3]
        print(trapped_water(heights))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
