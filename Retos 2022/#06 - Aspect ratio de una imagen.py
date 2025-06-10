"""
Crea un programa que se encargue de calcular el aspect ratio de una
    imagen a partir de una url.
- Url de ejemplo:
https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una
    imagen de 1920*1080px.
"""
from PIL import Image
import requests
from io import BytesIO
from math import gcd

def aspect_ratio(url: str) -> str:
    """
    Calculate the aspect ratio of an image from a given URL.

    Parameters:
    - url (str): URL to the image.

    Returns:
    - str: Aspect ratio in the format 'W:H' (e.g., '16:9').
    """
    response = requests.get(url)
    image_ = Image.open(BytesIO(response.content))
    width, height = image_.size

    divisor = gcd(width, height)
    return f"{width // divisor}:{height // divisor}"


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
    print(f"El aspect ratio de la imagen es: {aspect_ratio(url)}")
