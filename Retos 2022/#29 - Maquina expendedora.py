"""
Simula el funcionamiento de una máquina expendedora creando una operación
    que reciba dinero (array de monedas) y un número que indique la selección
    del producto.
- El programa retornará el nombre del producto y un array con el dinero
    de vuelta (con el menor número de monedas).
- Si el dinero es insuficiente o el número de producto no existe,
    deberá indicarse con un mensaje y retornar todas las monedas.
- Si no hay dinero de vuelta, el array se retornará vacío.
- Para que resulte más simple, trabajaremos en céntimos con monedas
    de 5, 10, 50, 100 y 200.
- Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""


class ProductError(Exception):
    """Exception raised when an invalid product ID is selected."""
    pass

class MoneyError(Exception):
    """Exception raised when there is a problem with the inserted money."""
    pass

def validate_data(id_: int, money: list[int]) -> None:
    """
    Validates the product ID and the inserted money.

    Args:
        id_ (int): Selected product ID.
        money (list[int]): List of inserted coin values.

    Raises:
        TypeError: If the ID is not an integer or any coin is not an integer.
    """
    if not isinstance(id_, int):
        raise TypeError("El id del producto debe ser un numero entero.")
    if not all(isinstance(coin, int) for coin in money):
        raise TypeError("Las monedas deben de ser un numero entero.")

def get_change(amount: int, coins: list[int]) -> list[int]:
    """
    Calculates the change to return using the fewest number of coins.

    Args:
        amount (int): The amount of change to return.
        coins (list[int]): Available denominations.

    Returns:
        list[int]: List of coins that sum up to the change.
    """
    change = []
    coins = sorted(coins, reverse=True)
    for coin in coins:
        while amount >= coin:
            change.append(coin)
            amount -= coin
    return change

def vending_machine(money: list[int], id_: int) -> list|None:
    """
    Simulates a vending machine operation.

    Args:
        money (list[int]): List of coins inserted into the machine.
        id_ (int): Product selection ID.

    Returns:
        list: On success, returns [product_name, change_list].
            On failure, returns the same list of inserted coins.

    Raises:
        ProductError: If the selected product does not exist.
        MoneyError: If the inserted money is invalid or insufficient.
    """
    products = {
        1: ["Coca cola", 5],
        2: ["Sabritas", 15],
        3: ["Caja de galletas", 60],
        4: ["Aceite", 75],
        5: ["Cereal", 55]
        }

    valid_coins = [5, 10, 50, 100, 200]

    try:
        validate_data(id_, money)

        if not id_ in products:
            raise ProductError("El producto no existe.")
        if not all(coin in valid_coins for coin in money):
            raise MoneyError("Solo se admiten monedas de 5, 10, 50, 100 y 200.")
        if sum(money) < products[id_][1]:
            raise MoneyError("El costo del producto es mayor al dinero ingresado.")

        change = sum(money) - products[id_][1]

        coins_returned = get_change(change, valid_coins)

        return [products[id_][0], coins_returned]

    except ProductError as e:
        print(f"{e}")
        return money
    except MoneyError as e:
        print(f"{e}")
        return money
    except TypeError as e:
        print(f"{e}")

if __name__ == "__main__":
    print(vending_machine([50], 2))
    print(vending_machine([5, 10], 2))
    print(vending_machine([50, 10], 1))
    print(vending_machine([100, 100], 3))
    print(vending_machine([200], 5))
    print(vending_machine([2, 1], 1))
    print(vending_machine([50], 10))
    print(vending_machine([10], 4))
