"""
Crea una función que encuentre todas las combinaciones de los números
    de una lista que suman el valor objetivo.
- La función recibirá una lista de números enteros positivos
    y un valor objetivo.
- Para obtener las combinaciones sólo se puede usar
    una vez cada elemento de la lista (pero pueden existir
    elementos repetidos en ella).
- Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
    Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
    (Si no existen combinaciones, retornar una lista vacía)
"""

def find_combinations(nums: list[int], target: int) -> list:
    """ Function to find all unique combinations of numbers in a list that sum up to a target value.

    Args:
        nums (list[int]): A list of positive integers.
        target (int): The target sum value.

    Returns:
        list: A list of lists, where each inner list is a unique combination of numbers that sum up to the target value.
    """

    if not nums:
        raise ValueError("Error. La lista de números no puede estar vacía.")
    if target <= 0:
        raise ValueError("Error. El valor objetivo debe ser un número entero positivo.")
    if any(num <= 0 for num in nums):
        raise ValueError("Error. Todos los números en la lista deben ser enteros positivos.")

    def backtrack(start: int, path: list[int], remaining: int):
        if remaining == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if nums[i] > remaining:
                continue
            backtrack(i + 1, path + [nums[i]], remaining - nums[i])

    result = []
    nums.sort()
    backtrack(0, [], target)
    return result

if __name__ == "__main__":
    try:
        print(find_combinations([1, 5, 3, 2], 6))
        print(find_combinations([2, 4, 6], 5))
    except ValueError as e:
        print(e)

