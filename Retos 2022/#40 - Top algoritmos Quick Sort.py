"""
Implementa uno de los algoritmos de ordenación más famosos:
    el "Quick Sort", creado por C.A.R. Hoare.
- Entender el funcionamiento de los algoritmos más utilizados de la historia
    Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
- Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
    donde trabajaremos y entenderemos los más famosos de la historia.
"""

class QuickSortExample():
    """
    Implements the QuickSort algorithm using recursion.
    
    This class provides a static method to sort a list of integers.
    """

    @staticmethod
    def quick_sort( numbers: list[int]) -> list[int]:
        """
        Sorts a list of integers using the QuickSort algorithm.

        Args:
            numbers (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list.
        """
        if len(numbers) <= 1:
            return numbers
        pivot = numbers[0]
        minors = [number for number in numbers[1:] if number <= pivot]
        greaters = [number for number in numbers[1:] if number > pivot]

        return QuickSortExample.quick_sort(minors) + [pivot] + QuickSortExample.quick_sort(greaters)


if __name__ == "__main__":
    example = QuickSortExample()
    lista_desordenada = [10, 7, 8, 9, 1, 5]
    lista_ordenada = example.quick_sort(lista_desordenada)
    print(f"Lista desordenada: {lista_desordenada}")
    print(f"Lista ordenada: {lista_ordenada}")
