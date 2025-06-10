"""
Crea un programa que sea capaz de transformar texto natural a código
    morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar
    la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras
    o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en
    https://es.wikipedia.org/wiki/Código_morse.
"""

class ConverterMorse:
    """
        A class to convert between natural text and Morse code.

        Methods:
        - converter(text: str) -> None:
            Converts the provided text, either from natural text to Morse code or from Morse 
                code to natural text, 
            depending on the input format.

        Attributes:
        - morse_alphabet (dict): A dictionary that maps alphabetic characters and digits 
        to their corresponding Morse code representations.
    """

    def __init__(self):
        """
        Initializes the Morse code converter with the Morse alphabet.
        Includes letters, digits, and some common symbols.
        """

        self.morse_alphabet = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
            "E": ".", "F": "..-.", "G": "--.", "H": "....",
            "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---", "P": ".--.",
            "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---",
            "3": "...--", "4": "....-", "5": ".....", "6": "-....",
            "7": "--...", "8": "---..", "9": "----.", "0": "-----",
            ",": "--..--", ".": ".-.-.-", "?": "..--..", "!": "-.-.--", "/": "-..-."
        }

    def converter(self, text: str) -> None:
        """
        Converts the given text to Morse code or vice versa. 
        Automatically detects the format of the input and performs the corresponding conversion.

        Parameters:
        - text (str): The text to convert. Can be a string in natural language or Morse code.

        Output:
        - Prints the result of the conversion to the console.
        """

        if all(c.isalpha() or c.isdigit() or c.isspace() for c in text):
            code_morse = []
            for char in text.upper():
                if char == " ":
                    code_morse.append("")
                else:
                    code_morse.append(self.morse_alphabet.get(char, "?"))

            print(" ".join(code_morse))
        elif all(c in ".- " for c in text):
            inverted_alphabet = {v: k for k, v in self.morse_alphabet.items()}
            words = text.split("  ")
            natural_text = []
            for word in words:
                chars = word.split(" ")
                for char in chars:
                    natural_text.append(inverted_alphabet.get(char, "?"))
                natural_text.append(" ")

            print("".join(natural_text).lower().strip())
        else:
            print("Ingrese un dato válido.")


if __name__ == "__main__":
    converter = ConverterMorse()
    print("Texto a morse:")
    converter.converter("Te amo")

    print("\nMorse a texto:")
    converter.converter("- .  .- -- ---")
