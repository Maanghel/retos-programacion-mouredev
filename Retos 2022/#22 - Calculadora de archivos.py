"""
Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
    resultado e imprímelo.
- El .txt se corresponde con las entradas de una calculadora.
- Cada línea tendrá un número o una operación representada por un
    símbolo (alternando ambos).
- Soporta números enteros y decimales.
- Soporta las operaciones suma "+", resta "-", multiplicación "*"
    y división "/".
- El resultado se muestra al finalizar la lectura de la última
    línea (si el .txt es correcto).
- Si el formato del .txt no es correcto, se indicará que no se han
    podido resolver las operaciones.
"""

class CalculatorParsingError(Exception):
    """
    Custom exception used to indicate invalid formatting in the calculator input file.
    Triggered when the file content does not follow the expected pattern
    of alternating numbers and operators.
    """

def calculate(directory: str) -> None:
    """
    Reads a text file simulating a calculator's input and prints the computed result.

    Expected Format:
    - The file must alternate between numeric values (integers or decimals) 
        and arithmetic operators: "+", "-", "*", "/".
    - The first and last lines must be numbers.
    - Whitespace and blank lines are ignored.

    Behavior:
    - Performs calculations based on the valid input.
    - If the format is incorrect (e.g., non-numeric input, unknown operator, 
        or incorrect order), raises a CalculatorParsingError.
    - Handles division by zero explicitly.
    - Handles missing file errors gracefully.

    Parameters:
        directory (str): Path to the input text file.

    Returns:
        None
    """
    VALID_OPERATORS = {"+", "-", "*", "/"}

    try:
        with open(directory, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]

            operation = []
            for i, value in enumerate(lines):
                if i % 2 == 0:
                    try:
                        number = float(value)
                        operation.append(number)
                    except ValueError as e:
                        raise CalculatorParsingError(f"Numero invalido encontrado: {value}") from e
                elif value in VALID_OPERATORS:
                    operation.append(value)
                else:
                    raise CalculatorParsingError(f"Operador invalido encontrado: {value}")

            if len(operation) % 2 == 0:
                raise CalculatorParsingError("La lista no termina con un numero.")

            result = operation[0]
            for i in range(1, len(operation) - 1, 2):
                operator = operation[i]
                next_number = operation[i + 1]

                if operator == "+":
                    result += next_number
                elif operator == "-":
                    result -= next_number
                elif operator == "*":
                    result *= next_number
                elif operator == "/":
                    if next_number == 0:
                        print("Error. División entre cero.")
                        return None
                    result /= next_number

            print(f"Resultado final: {result}")

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except CalculatorParsingError as e:
        print(f"Error de formato: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")


if __name__ == "__main__":
    calculate("Retos 2022/Challenge21.txt")