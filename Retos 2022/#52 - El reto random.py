"""
Crea tu propio enunciado para que forme parte de los retos de 2023.
- Ten en cuenta que su dificultad debe ser asumible por la comunidad y seguir
    un estilosemejante a los que hemos realizado durante el año.
- Si quieres también puedes proponer tu propia solución al reto
    (en el lenguaje que quieras).
"""

# Ejemplo de enunciado:
"""
Crear un programa que genere un número aleatorio entre 1 y 100,
    y le pida al usuario que adivine el número.
El programa debe indicarle al usuario si su número es mayor o 
    menor que el número aleatorio.
"""

# Ejemplo de solución en Python:
import random

def adivina_el_numero() -> None:
    """
    Generates a random number between 1 and 100 and prompts the user to guess it.

    The user is given hints indicating whether their guess is too low or too high.
    The program continues until the correct number is guessed and displays 
    the number of attempts taken.

    Raises:
        ValueError: If the user inputs a non-integer value.
    """
    numero_aleatorio = random.randint(1, 100)
    intentos = 0

    print("He generado un numero aleatorio entre 1 y 100.")
    print("Intenta adivinarlo.")

    while True:
        try:
            adivinanza = int(input("Introduce tu numero: "))
            intentos += 1
            
            if adivinanza < numero_aleatorio:
                print("El numero es mayor.")
            elif adivinanza > numero_aleatorio:
                print("El numero es menor.")
            else:
                print(f"¡Felicidades! Has adivinado el numero {numero_aleatorio} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número valido.")


if __name__ == "__main__":
    adivina_el_numero()
