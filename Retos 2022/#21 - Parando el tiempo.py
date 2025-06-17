"""
Crea una función que sume 2 números y retorne su resultado pasados
    unos segundos.
- Recibirá por parámetros los 2 números a sumar y los segundos que
    debe tardar en finalizar su ejecución.
- Si el lenguaje lo soporta, deberá retornar el resultado de forma
    asíncrona, es decir, sin detener la ejecución del programa principal.
    Se podría ejecutar varias veces al mismo tiempo.
"""

import asyncio
import time

async def delayed_sum(num: int, num2: int, time_: int) -> int:
    """
    Asynchronously adds two integers after a delay.

    This function waits for a given number of seconds before returning 
    the sum of two integers. It is designed to be used in asynchronous 
    contexts and supports concurrent execution with other coroutines.

    Parameters:
    - num (int): The first number to add.
    - num2 (int): The second number to add.
    - time_ (int): The number of seconds to wait before returning the result.

    Returns:
    - int: The sum of the two input integers after the delay.

    Raises:
    - ValueError: If any of the inputs are not integers.
    """
    if not all(isinstance(value, int) for value in [num, num2, time_]):
        raise ValueError("Ha ocurrido un error. Solo se admiten enteros en esta operacion.")

    await asyncio.sleep(time_)

    return num + num2

async def main():
    """
    Executes multiple asynchronous addition tasks with delays.

    This function prints the start time, runs two asynchronous tasks that 
    simulate delayed addition using the `stoping_time` coroutine, and then 
    prints their results once completed. Finally, it prints the end time.

    Tasks are executed concurrently using asyncio.TaskGroup.
    """
    print(f"Hora de inicio: {time.strftime('%X')}")

    async with asyncio.TaskGroup() as group:
        task1 = group.create_task(delayed_sum(1, 1, 1))
        task2 = group.create_task(delayed_sum(1, 2, 2))

        print(await task1)
        print(await task2)

    print(f"Hora de finalizacion: {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main())
