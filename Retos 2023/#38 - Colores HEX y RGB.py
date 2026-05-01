"""
Crea las funciones capaces de transformar colores HEX
    a RGB y viceversa.
Ejemplos:
    RGB a HEX: r: 0, g: 0, b: 0 -> #000000
    HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
"""

def rgb_to_hex(r: int, g: int, b: int) -> str:
    """ Function to convert RGB color values to HEX format. 

    Args:
        r (int): Red color value (0-255)
        g (int): Green color value (0-255)
        b (int): Blue color value (0-255)

    Returns:
        str: The HEX color representation in the format "#RRGGBB"

    Raises:
        TypeError: If any of the color values are not integers.
        ValueError: If any of the color values are outside the range 0-255.
    """
    if not all(isinstance(color, int) for color in (r, g, b)):
        raise TypeError("Los valores de r, g y b deben ser enteros.")
    if not all(0 <= color <= 255 for color in (r, g, b)):
        raise ValueError("Los valores de r, g y b deben estar entre 0 y 255.")

    return f"#{r:02X}{g:02X}{b:02X}"

def hex_to_rgb(hex_color: str) -> tuple:
    """ Function to convert a HEX color value to RGB format.

    Args:
        hex_color (str): The HEX color representation in the format "#RRGGBB"

    Returns:
        tuple: A tuple containing the RGB color values (r, g, b)

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the HEX color format is incorrect or if the characters are not valid hexadecimal digits.
    """
    if not isinstance(hex_color, str):
        raise TypeError("El valor de entrada debe ser una cadena de texto.")
    if not hex_color.startswith("#") or len(hex_color) != 7:
        raise ValueError("El formato del color HEX es incorrecto. Debe comenzar con '#' seguido de 6 caracteres hexadecimales.")

    try:
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
    except ValueError as e:
        raise ValueError("El formato del color HEX es incorrecto. Asegúrate de que los caracteres después de '#' sean hexadecimales.") from e

    return (r, g, b)

if __name__ == "__main__":
    print(rgb_to_hex(255, 0, 0))
    print(hex_to_rgb("#00FF00"))
