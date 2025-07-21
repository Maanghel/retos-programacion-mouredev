"""
Crea un programa se encargue de transformar un número binario
    a decimal sin utilizar funciones propias del lenguaje que
    lo hagan directamente.
"""

class BinaryConverter():
    """
    A utility class for converting binary strings to decimal integers.

    This class contains only static methods and does not require instantiation.
    It ensures input validation and performs manual binary-to-decimal conversion
    using basic arithmetic and iteration.

    Methods:
        convert_to_decimal(binary: str) -> int:
            Converts a binary string to its decimal integer equivalent.
    """

    @staticmethod
    def convert_to_decimal(binary: str) -> int:
        """
        Converts a binary string to its decimal integer equivalent.

        Args:
            binary (str): A string containing only '0' and '1'.

        Returns:
            int: The decimal representation of the binary number.

        Raises:
            ValueError: If the input contains characters other than '0' or '1'.
        """
        if not all(char in "01" for char in binary):
            raise ValueError("Solo se aceptan '0' y '1'.")
        return sum(int(bit) * 2**i for i, bit in enumerate(binary[::-1]))


if __name__ == "__main__":
    print(BinaryConverter.convert_to_decimal("10110"))
