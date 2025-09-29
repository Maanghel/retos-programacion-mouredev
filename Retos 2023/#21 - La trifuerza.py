"""
¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 

Crea un programa que dibuje una Trifuerza de "Zelda"
formada por asteriscos.
- Debes indicarle el número de filas de los triángulos con un entero positivo (n).
- Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.

Ejemplo: Trifuerza 2

   *
  ***
 *   *
*** ***
"""

def draw_threforce(n: int) -> None:
    if not isinstance(n, int):
        raise TypeError("Solo se admiten enteros positivos.")
    if n < 0:
        raise ValueError("El número de filas debe ser un entero positivo.")

    for i in range(n):
        print(" " * (2 * n - i - 1 ) + "*" * (2 * i + 1))
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1) + " " * (n - i + (n - i - 1)) + "*" * (2 * i + 1))


if __name__ == "__main__":
    draw_threforce(5)
