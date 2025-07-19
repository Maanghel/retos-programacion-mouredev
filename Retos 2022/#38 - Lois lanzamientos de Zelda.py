"""
¡Han anunciado un nuevo "The Legend of Zelda"!
Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
"The Legend of Zelda" de la historia?
Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
que tú selecciones.
- Debes buscar cada uno de los títulos y su día de lanzamiento 
(si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
"""

from enum import Enum
from datetime import date
from dataclasses import dataclass

@dataclass(frozen=True)
class ZeldaInfo:
    """
    A class to store information about a Zelda game including its title and release date.
    
    Attributes:
    title (str): The name of the Zelda game.
    release_date (date): The release date of the game.
    """
    title: str
    release_date: date

class ZeldaGame(Enum):
    """
    Enum that defines all the "The Legend of Zelda" games with their respective release dates.
    
    Each enum member represents a specific Zelda game and stores its title and release date.
    """
    THE_LEGEND_OF_ZELDA = ZeldaInfo("The Legend of Zelda", date(1986, 2, 21))
    ZELDA_II_THE_ADVENTURE_OF_LINK = ZeldaInfo("Zelda II: The Adventure of Link", date(1987, 1, 14))
    A_LINK_TO_THE_PAST = ZeldaInfo("The Legend of Zelda: A Link to the Past", date(1991, 11, 21))
    LINKS_AWAKENING = ZeldaInfo("The Legend of Zelda: Link's Awakening", date(1993, 6, 6))
    OCARINA_OF_TIME = ZeldaInfo("The Legend of Zelda: Ocarina of Time", date(1998, 11, 21))
    MAJORAS_MASK = ZeldaInfo("The Legend of Zelda: Majora's Mask", date(2000, 4, 27))
    ORACLE_OF_SEASONS_AND_ORACLE_OF_AGES = ZeldaInfo("The Legend of Zelda: Oracle of Seasons / Oracle of Ages", date(2001, 2, 14))
    FOUR_SWORDS = ZeldaInfo("The Legend of Zelda: Four Swords", date(2002, 12, 2))
    THE_WIND_WAKER = ZeldaInfo("The Legend of Zelda: The Wind Waker", date(2002, 12, 13))
    FOUR_SWORDS_ADVENTURES = ZeldaInfo("The Legend of Zelda: Four Swords Adventures", date(2004, 6, 18))
    THE_MINISH_CAP = ZeldaInfo("The Legend of Zelda: The Minish Cap", date(2004, 11, 4))
    TWILIGHT_PRINCESS = ZeldaInfo("The Legend of Zelda: Twilight Princess", date(2006, 11, 20))
    PHANTOM_HOURGLASS = ZeldaInfo("The Legend of Zelda: Phantom Hourglass", date(2007, 6, 23))
    SPIRIT_TRACKS = ZeldaInfo("The Legend of Zelda: Spirit Tracks", date(2009, 12, 7))
    SKYWARD_SWORD = ZeldaInfo("The Legend of Zelda: Skyward Sword", date(2011, 11, 20))
    A_LINK_BETWEEN_WORLDS = ZeldaInfo("The Legend of Zelda: A Link Between Worlds", date(2013, 11, 22))
    TRI_FORCE_HEROES = ZeldaInfo("The Legend of Zelda: Tri Force Heroes", date(2015, 10, 22))
    BREATH_OF_THE_WILD = ZeldaInfo("The Legend of Zelda: Breath of the Wild", date(2017, 3, 3))
    TEARS_OF_THE_KINGDOM = ZeldaInfo("The Legend of Zelda: Tears of the Kingdom", date(2023, 5, 12))

class DateDifference():
    """
    A class to calculate the date difference between two selected Zelda games.
    
    The user selects two games from a menu, and the program calculates the 
    difference in years, months, and days between their release dates.
    """

    def __init__(self) -> None:
        """
        Initializes the DateDifference object, calls the menu to get the selected games,
        and calculates the date difference.
        """
        games = self.menu()
        self.first_game = games[0]
        self.second_game = games[1]
        self.calculated_date_difference()

    def menu(self) -> list[ZeldaGame]:
        """
        Displays a menu of all Zelda games, allowing the user to select two games 
        for which the release date difference will be calculated.
        
        Returns:
        list[ZeldaGame]: A list containing the two selected Zelda games.
        """
        print("Seleccione dos juegos de zelda para verificar la diferencia entre sus fechas de lanzamientos:")
        for idx, game in enumerate(ZeldaGame, 1):
            print(f"{idx}. {game.value.title} (Lanzado: {game.value.release_date})")

        games = []
        while True:
            try:
                option1 = int(input("Introduce el número del primer juego: "))
                if option1 < 1 or option1 > len(ZeldaGame):
                    raise ValueError("Opción fuera de rango.")
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor, introduce un número válido.")
        while True:
            try:
                option2 = int(input("Introduce el número del segundo juego: "))
                if option2 < 1 or option2 > len(ZeldaGame):
                    raise ValueError("Opción fuera de rango.")
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor, introduce un número válido.")

        games.append(list(ZeldaGame)[option1 - 1])
        games.append(list(ZeldaGame)[option2 - 1])
        print(f"Seleccionaste:\n1.- {games[0].value.title} (Lanzado: {games[0].value.release_date})\n2.- {games[1].value.title} (Lanzado: {games[1].value.release_date})")

        return games

    def calculated_date_difference(self) -> None:
        """
        Calculates the difference in years, months, and days between the release dates
        of the two selected Zelda games, and displays the result.
        """
        dt1 = self.first_game.value.release_date
        dt2 = self.second_game.value.release_date

        delta = abs(dt1 - dt2)

        years = delta.days // 365
        days = delta.days - (years * 30)

        print(f"\nLa diferencia entre los lanzamientos de '{self.first_game.value.title}' y '{self.second_game.value.title}' es:")
        print(f"{years} años y {days} días.")


if __name__ == "__main__":
    date_difference = DateDifference()
