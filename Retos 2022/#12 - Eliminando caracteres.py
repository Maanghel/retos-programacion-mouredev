"""
Crea una función que reciba dos cadenas como parámetro (str1, str2)
    e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO
    estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
    estén presentes en str1.
"""

def missing_char(str1: str, str2: str) -> tuple[str, str]:
    """
    Returns the characters that are unique to each of the two input strings.

    Characters are compared in a case-insensitive way. Each result string contains
    the characters that are present in one input string but not in the other,
    sorted in alphabetical order.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        tuple[str, str]: A tuple containing two strings:
            - The characters in `str1` but not in `str2`.
            - The characters in `str2` but not in `str1`.
    """
    str1_set = set(str1.lower())
    str2_set = set(str2.lower())

    out1 = ''.join(sorted(str1_set.difference(str2_set)))
    out2 = ''.join(sorted(str2_set.difference(str1_set)))

    return out1, out2

o1, o2 = missing_char("hola python", "adios java")
print(o1)
print(o2)
