"""
Crea una función que reciba días, horas, minutos y segundos (como enteros)
    y retorne su resultado en milisegundos.
"""

def convert_to_milliseconds(time_dict: dict) -> int:
    """
    Converts a time duration given in days, hours, minutes, and seconds into milliseconds.

    The input is a dictionary that may contain the following keys: 
    "day", "hour", "minute", and "second".
    If any of these keys are missing, they are assumed to be zero.

    All values must be non-negative integers. If any value is invalid, the function prints a message 
    and returns 0.

    Args:
        time_dict (dict): A dictionary with optional keys "day", "hour", "minute", "second" 
                        and non-negative integer values.

    Returns:
        int: The total time converted into milliseconds.
    """
    conversion_table = {
        "second": 1000,
        "minute": 60000,
        "hour": 3600000,
        "day": 86400000
        }

    required_keys = {"day", "hour", "minute", "second"}
    for key in required_keys:
        time_dict.setdefault(key, 0)

    if not all(isinstance(value, int) and value >= 0 for value in time_dict.values()):
        print("Todos los valores deben ser números enteros no negativos.")
        return 0

    result = sum(
        value * conversion_table[key]
        for key, value in time_dict.items()
        if key in conversion_table
        )

    return result


if __name__ == "__main__":
    time = {"day": 1, "hour": 2, "minute": 30, "second": 45}
    miliseconds = convert_to_milliseconds(time)
    print(miliseconds)
