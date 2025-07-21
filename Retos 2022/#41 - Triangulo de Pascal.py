"""
Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
    indicándole únicamente el tamaño del lado.
- Aquí puedes ver rápidamente cómo se calcula el triángulo:
    https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
"""

def triangulo_pascal_iterativo(num_rows: int) -> list[list[int]]:
    """
    Generates Pascal's Triangle of a given size using iteration.

    Args:
        n_side (int): The number of rows in the triangle.

    Returns:
        list[list[int]]: A list of rows, each row being a list of integers.
    """
    if num_rows <= 0:
        raise ValueError("Solo se aceptan enteros positivos para las filas.")
    if not isinstance(num_rows, int):
        raise ValueError("Solo se acepta un entero para las filas.")
    triangle = []
    for i in range(num_rows):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)

    return triangle

def pretty_print(triangle: list[list[int]]) -> None:
    """
    Prints Pascal's Triangle in a nicely formatted, centered way.

    Args:
        triangle (list[list[int]]): The triangle to print.
    """
    max_width = len("   ".join(map(str, triangle[-1])))
    for row in triangle:
        line = " ".join(f"{num:^3}" for num in row)
        print(line.center(max_width))


if __name__ == "__main__":
    pascal_triangle = triangulo_pascal_iterativo(10)
    pretty_print(pascal_triangle)
