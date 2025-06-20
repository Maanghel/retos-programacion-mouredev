"""
Crea un programa que calcule quien gana más partidas al piedra,
    papel, tijera.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "R" (piedra), "P" (papel)
    o "S" (tijera).
- Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""

from typing import List, Tuple, Literal

Move = Literal["R", "P", "S"]
Result = Literal["Player 1", "Player 2", "Tie", "Invalid Input"]

def validate_game(game: List[Tuple[Move, Move]]) -> bool:
    """
    Validates that all plays contain only valid moves: 'R', 'P', or 'S'.

    Parameters:
        game (List[Tuple[str, str]]): List of tuples representing the moves.

    Returns:
        bool: True if all moves are valid, False otherwise.
    """
    valid_moves = {"R", "P", "S"}
    return all(p1 in valid_moves and p2 in valid_moves for p1, p2 in game)


def winner(p1: Move, p2: Move) -> int:
    """
    Determines the winner of a single round.

    Returns:
        0 for a tie, 1 if Player 1 wins, 2 if Player 2 wins.
    """
    win_rules = {"R": "S", "P": "R", "S": "P"}

    if p1 == p2:
        return 0
    elif win_rules[p1] == p2:
        return 1
    else:
        return 2


def rock_paper_scissors(game: List[Tuple[Move, Move]]) -> Result:
    """
    Determines the overall winner of a Rock, Paper, Scissors game.

    Parameters:
        game (List[Tuple[str, str]]): List of tuples with moves for Player 1 and Player 2.

    Returns:
        str: "Player 1", "Player 2", "Tie", or "Invalid Input"
    """
    if not validate_game(game):
        return "Invalid Input"

    p1_score = p2_score = 0

    for p1, p2 in game:
        result = winner(p1, p2)
        if result == 1:
            p1_score += 1
        elif result == 2:
            p2_score += 1

    if p1_score > p2_score:
        return "Player 1"
    elif p2_score > p1_score:
        return "Player 2"
    else:
        return "Tie"


if __name__ == "__main__":
    plays: List[Tuple[Move, Move]] = [("R", "S"), ("S", "R"), ("R", "S")]
    result = rock_paper_scissors(plays)
    print(f"Resultado del juego: {result}")
