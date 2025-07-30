"""
Crea una función que sea capaz de encriptar y desencriptar texto
    utilizando el algoritmo de encriptación de Karaca
    (debes buscar información sobre él).
"""

from typing import Optional

vowel_replacements = {
    'a': '0', 'e': '1', 'i': '2',
    'o': '3', 'u': '4'
}

def validate_text(text: Optional[str] = None, encrypt: Optional[str] = None) -> None:
    """
    Validates the input string for encryption or decryption.

    Args:
        text (str, optional): Plain text to be encrypted.
        encrypt (str, optional): Encrypted string to be decrypted.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input is empty or doesn't match required structure.
    """
    if encrypt is not None:
        if not isinstance(encrypt, str):
            raise ValueError("El valor encriptado debe ser una cadena de texto")
        if not encrypt:
            raise ValueError("El valor encriptado no puede estar vacío")
        if not encrypt.endswith("aca"):
            raise TypeError("El valor encriptado debe terminar en 'aca'")
    elif text is not None:
        if not isinstance(text, str):
            raise TypeError("El texto a encriptar debe ser una cadena de texto")
        if not text:
            raise ValueError("El texto a encriptar no puede estar vacío")

def karaca_encrypt(text: str) -> str:
    """
    Encrypts the input text using Karaca encryption algorithm.

    Args:
        text (str): The plain text to encrypt.

    Returns:
        str: Encrypted version of the input.
    """
    validate_text(text= text)
    encrypted = [
        vowel_replacements.get(char, char)
        for char in text[::-1].lower()
    ]
    return "".join(encrypted) + "aca"

def karaca_decrypt(text: str) -> str:
    """
    Decrypts a string encoded with the Karaca encryption algorithm.

    Args:
        text (str): The encrypted string.

    Returns:
        str: The decrypted plain text.
    """
    validate_text(encrypt= text)
    text = text[:-3]
    inverted_replacements = {v: k for k, v in vowel_replacements.items()}
    decrypted = [
        inverted_replacements.get(char, char)
        for char in text.lower()
    ]
    return "".join(decrypted[::-1])


if __name__ == "__main__":
    original_text = "Hola mundo"
    encrypted_text = karaca_encrypt(original_text)
    print(f"Texto encriptado: {encrypted_text}")
    decrypted_text = karaca_decrypt(encrypted_text)
    print(f"Texto desencriptado: {decrypted_text}")
