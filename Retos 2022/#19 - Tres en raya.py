"""
Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
y retorne lo siguiente:
- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta.
Se podría representar con un vacío "", por ejemplo.
"""

def game_line(matrix: list) -> str:
    """
    Analyzes a 3x3 matrix representing a Tic-Tac-Toe board and determines the game result.

    The matrix should contain only the symbols "X", "O", or an empty string "" 
    (which may represent an empty cell).
    The function returns:
    - "X" if player X has won
    - "O" if player O has won
    - "Empate" if the game ended in a draw
    - "Nulo" if the board is invalid (wrong size, invalid symbols, 
    too many moves by one player, or both players have won)

    Args:
        matrix (list): A 3x3 list of lists representing the board.

    Returns:
        str: The game result ("X", "O", "Empate", or "Nulo").
    """
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        return "Nulo"

    valid_symbols = {"X", "O", ""}
    normalized = [
        [cell.strip().upper() if cell.strip() else "" for cell in row]
        for row in matrix
    ]
    flat = [cell for row in normalized for cell in row]

    if any(cell not in valid_symbols for cell in flat):
        return "Nulo"

    x_count = flat.count("X")
    o_count = flat.count("O")
    if abs(x_count - o_count) > 1:
        return "Nulo"

    winning_combinations = [
        (0, 1, 2),  # fila 0
        (3, 4, 5),  # fila 1
        (6, 7, 8),  # fila 2
        (0, 3, 6),  # columna 0
        (1, 4, 7),  # columna 1
        (2, 5, 8),  # columna 2
        (0, 4, 8),  # diagonal \
        (2, 4, 6),  # diagonal /
    ]

    x_wins = o_wins = 0

    for a, b, c in winning_combinations:
        line = [flat[a], flat[b], flat[c]]
        if line == ["X"] * 3:
            x_wins += 1
        elif line == ["O"] * 3:
            o_wins += 1

    if x_wins > 0 and o_wins > 0:
        return "Nulo"
    if x_wins > 0:
        return "X"
    if o_wins > 0:
        return "O"
    if "" in flat:
        return "Nulo"
    return "Empate"


if __name__ == "__main__":
    matrix1 = [
        ["X", "X", "X"],
        ["O", "O", " "],
        [" ", " ", "O"]
    ]

    matrix2 = [
        ["X", "O", "O"],
        ["X", "O", "O"],
        ["X", "X", "O"]
    ]

    print(game_line(matrix1))
    print(game_line(matrix2))
