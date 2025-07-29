"""
Crea una función que sea capaz de detectar y retornar todos los
    handles de un texto usando solamente Expresiones Regulares.
Debes crear una expresión regular para cada caso:
- Handle usuario: Los que comienzan por "@"
- Handle hashtag: Los que comienzan por "#"
- Handle web: Los que comienzan por "www.", "http://", "https://"
    y finalizan con un dominio (.com, .es...)
"""

import re

def extract_handles(text: str) -> dict:
    """
    Extracts user handles, hashtags, and website URLs from a given text using regular expressions.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary with keys 'usuarios', 'hashtags', and 'webs', containing lists of matches.
    """
    usuarios = re.findall(r'@\w+', text)
    hashtags = re.findall(r'#\w+', text)
    webs = re.findall(r'(?:https?://|www\.)\S+\.\w+', text)

    return {
        "usuarios": usuarios,
        "hashtags": hashtags,
        "webs": webs
    }


if __name__ == "__main__":
    texto = "Hola @manuel_dev, visita https://openai.com y no olvides el #AI. Mira www.ejemplo.es también."
    resultado = extract_handles(texto)
    print(resultado)