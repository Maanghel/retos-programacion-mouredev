"""
Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
- Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
- EXTRA: ¿Eres capaz de dibujar más figuras?
"""

from typing import Literal

Figure = Literal["Triangle", "Square", "Diamond"]

def validate_data(side: int, figure: Figure) -> bool:
    """
    Validates that the side is a positive integer and the figure is a valid option.
    
    Parameters:
        side (int): Size of the side of the figure.
        figure (str): Name of the figure to draw.

    Returns:
        bool: True if inputs are valid.

    Raises:
        ValueError: If side is not a positive integer.
        TypeError: If figure is not a recognized option.
    """
    valid_figures = ["Triangle", "Square", "Diamond"]

    if not isinstance(side, int) or side <= 0:
        raise ValueError("El lado debe ser un numero entero positivo.")

    if figure.capitalize() not in valid_figures:
        raise TypeError("La figura debe ser 'Triangle', 'Square' or 'Diamond'.")

    return True


def draw_triangle(size: int) -> None:
    for i in range(1, size + 1):
        print("* " * i)


def draw_square(size: int) -> None:
    for _ in range(size):
        print("* " * size)


def draw_diamond(size: int) -> None:
    if size % 2 == 0:
        raise ValueError("Para dibujar un diamante. El lado debe ser un numero impar.")

    mid = size // 2

    for i in range(mid + 1):
        print(" " * (mid - i) + "* " * (i + 1))
    for i in range(mid - 1, -1, -1):
        print(" " * (mid - i) + "* " * (i + 1))


def draw_figure(side: int, figure: Figure) -> None:
    """
    Draws the specified figure using asterisks.
    
    Parameters:
        side (int): Size of the side or height.
        figure (str): Type of figure to draw ("Triangle", "Square", "Diamond").
    """
    validate_data(side, figure)

    print(f"\nDibujando un {figure} de {side} de largo:\n")

    if figure == "Triangle":
        draw_triangle(side)
    elif figure == "Square":
        draw_square(side)
    elif figure == "Diamond":
        draw_diamond(side)


if __name__ == "__main__":
    draw_figure(5, "Triangle")
    draw_figure(4, "Square")
    draw_figure(7, "Diamond")
