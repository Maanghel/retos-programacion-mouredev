"""
Crea una función que calcule el valor del parámetro perdido
    correspondiente a la ley de Ohm.
- Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
    el valor del tercero (redondeado a 2 decimales).
- Si los parámetros son incorrectos o insuficientes, la función retornará
    la cadena de texto "Invalid values".
"""

def calculate_ohm(v: float = None, r: float = None, i: float = None) -> float|str:
    """
    Calculates the missing parameter from Ohm's Law (V = I * R).

    Exactly two of the three parameters (voltage `v`, resistance `r`, current `i`)
    must be provided as positive numeric values. The missing one should be `None`.

    Returns:
        float: The missing parameter calculated and rounded to 2 decimals.
        str: "Invalid values" if the input is incorrect or calculation fails.

    Examples:
        calculate_ohm(v=12, r=4) => 3.0  # I = V / R
        calculate_ohm(i=2, r=10) => 20.0 # V = I * R
        calculate_ohm(v=12, i=0) => "Invalid values" (division by zero)
    """
    inputs = [v, r, i]
    if inputs.count(None) != 1:
        return "Invalid values"

    for val in inputs:
        if val is not None:
            if not isinstance(val, (int, float)) or val <= 0:
                return "Invalid values"

    try:
        if v is None:
            return round(r * i, 2)
        if r is None:
            return round(v / i, 2)
        if i is None:
            return round(v / r, 2)
    except (TypeError, ZeroDivisionError):
        return "Invalid values"


if __name__ == "__main__":
    print(calculate_ohm(v= 12, r= 4))
