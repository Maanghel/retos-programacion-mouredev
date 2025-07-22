"""
Este es un reto especial por Halloween.
Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
    o Trato" y un listado (array) de personas con las siguientes propiedades:
- Nombre de la niña o niño
- Edad
- Altura en centímetros

Si las personas han pedido truco, el programa retornará sustos (aleatorios)
    siguiendo estos criterios:
- Un susto por cada 2 letras del nombre por persona
- Dos sustos por cada edad que sea un número par
- Tres sustos por cada 100 cm de altura entre todas las personas
- Sustos: 🎃 👻 💀 🕷 🕸 🦇

Si las personas han pedido trato, el programa retornará dulces (aleatorios)
    siguiendo estos criterios:
- Un dulce por cada letra de nombre
- Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
- Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
- Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
- En caso contrario retornará un error.
"""

from dataclasses import dataclass
from typing import List, Literal
import random

OPTION = Literal["truco", "trato"]

@dataclass(frozen=True)
class People:
    """
    Represents a person participating in the Trick or Treat game.

    Attributes:
        name (str): The person's name.
        age (int): The person's age in years.
        height (int): The person's height in centimeters.
    """
    name: str
    age: int
    height: int

class TrickOrTreat:
    """
    Main class for handling Trick or Treat logic.

    This class allows calculating either scares or candies based on a list
    of people and the selected option ("truco" or "trato").

    Methods:
        trick(people_list): Returns a string of random scares based on the rules.
        treat(people_list): Returns a string of random candies based on the rules.
        play(option, people_list): Static method to execute the game logic.
    """
    def __init__(self) -> None:
        """Initializes the emoji sets for scares and candies."""
        self.scares = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
        self.candys = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]

    def __validate_people(self, people_list: List[People]) -> None:
        """
        Validates the integrity of the list of people.
        Raises:
            ValueError: If any person has an invalid age or height.
        """
        for person in people_list:
            if person.age < 0 or person.height <= 0:
                raise ValueError(f"Datos inválidos en: {person}")

    def trick(self, people_list: List[People]) -> str:
        """
        Returns random scare emojis based on:
        - One scare for every 2 letters in name
        - Two scares for each even age
        - Three scares for every 100 cm (total height of all people)

        Args:
            people_list: List of People instances.

        Returns:
            A string of scare emojis.
        """
        self.__validate_people(people_list)
        total_scares = 0
        for person in people_list:
            total_scares += len(person.name) // 2
            total_scares += 2 if person.age % 2 == 0 else 0
        total_height = sum(person.height for person in people_list)
        total_scares += (total_height // 100) * 3
        return "".join(random.choice(self.scares) for _ in range(total_scares))

    def treat(self, people_list: List[People]) -> str:
        """
        Returns random candy emojis based on:
        - One candy per letter in name
        - One candy for every 3 years (up to 10 years per person)
        - Two candies per 50 cm (up to 150 cm per person)

        Args:
            people_list: List of People instances.

        Returns:
            A string of candy emojis.
        """
        self.__validate_people(people_list)
        total_candys = 0
        for person in people_list:
            total_candys += len(person.name)
            total_candys += min(person.age, 10) // 3
            total_candys += (min(person.height, 150) // 50) * 2
        return "".join(random.choice(self.candys) for _ in range(total_candys))

    @staticmethod
    def play(option: OPTION, people_list: List[People]) -> str:
        """
        Main entry point. Depending on the option ("truco" or "trato"),
        delegates the logic to the appropriate method.

        Args:
            option: A string indicating the action ("truco" or "trato").
            people_list: List of People instances.

        Returns:
            A string of emojis or "Error" if the option is invalid.
        """
        if option not in ["truco", "trato"]:
            return "Error"
        game = TrickOrTreat()
        return game.trick(people_list) if option == "truco" else game.treat(people_list)


if __name__ == "__main__":
    people_list = [
            People("Manuel", 29, 181), 
            People("Juan", 25, 175),
            People("Ana", 36, 156)
            ]
    print(TrickOrTreat.play("trato", people_list))
