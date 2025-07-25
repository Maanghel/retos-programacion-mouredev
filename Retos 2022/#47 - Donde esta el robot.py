"""
Calcula dónde estará un robot (sus coordenadas finales) que se
    encuentra en una cuadrícula representada por los ejes "x" e "y".
- El robot comienza en la coordenada (0, 0).
- Para idicarle que se mueva, le enviamos un array formado por enteros
    (positivos o negativos) que indican la secuencia de pasos a dar.
- Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene,
    luego 5, se detiene, y finalmente 2.
El resultado en este caso sería (x: -5, y: 12)
- Si el número de pasos es negativo, se desplazaría en sentido contrario al
    que está mirando.
- Los primeros pasos los hace en el eje "y". Interpretamos que está mirando
    hacia la parte positiva del eje "y".
- El robot tiene un fallo en su programación: cada vez que finaliza una
    secuencia de pasos gira 90 grados en el sentido contrario a las agujas
    del reloj.
"""

from typing import List
from enum import Enum, auto

class Direction(Enum):
    """
    Enum that represents the four cardinal directions.
    Uses auto() to assign unique values automatically.
    """
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

class Robot:
    """
    Simulates a robot moving on a 2D grid starting from (0, 0).
    After each move, the robot turns 90 degrees counter-clockwise.
    """
    DIRECTIONS = [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]

    def __init__(self) -> None:
        """
        Initializes the robot's starting position and direction.
        """
        self.actual_position = [0, 0]
        self.actual_direction = Direction.NORTH

    def walk(self, moves: List[int]) -> None:
        """
        Executes a list of movement instructions and turns the robot after each.
        
        Args:
            moves (List[int]): A list of integers representing movement steps.
                                Positive for forward, negative for backward.
        """
        self._validate_data(moves)
        for distance in moves:
            self._move(distance)
            self._turn_left()

    def print_position(self) -> None:
        """
        Prints the current position of the robot in (x, y) format.
        """
        print(f"Posición final del robot: (x: {self.actual_position[0]}, y: {self.actual_position[1]})")

    def _move(self, distance: int) -> None:
        """
        Moves the robot in the current direction by the specified distance.
        
        Args:
            distance (int): The number of steps to move.
        """
        match self.actual_direction:
            case Direction.NORTH:
                self.actual_position[1] += distance
            case Direction.SOUTH:
                self.actual_position[1] -= distance
            case Direction.EAST:
                self.actual_position[0] += distance
            case Direction.WEST:
                self.actual_position[0] -= distance

    def _validate_data(self, move: List[int]) -> None:
        """
        Validates that the move list contains only integers.
        
        Args:
            move (List[int]): The list of movements.
        
        Raises:
            TypeError: If the input is not a list.
            ValueError: If any element is not an integer.
        """
        if not isinstance(move, list):
            raise TypeError("Solo se acepta una lista de enteros.")
        if not all(isinstance(distance, int) for distance in move):
            raise ValueError("Solo se aceptan enteros negativos y positivos.")

    def _turn_left(self) -> None:
        """
        Rotates the robot 90 degrees counter-clockwise.
        """
        index = self.DIRECTIONS.index(self.actual_direction)
        self.actual_direction = self.DIRECTIONS[(index + 1) % 4]


if __name__ == "__main__":
    my_robot = Robot()
    move_list = [10, 5, -2]
    my_robot.walk(move_list)
    my_robot.print_position()
