"""
Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
¿De cuántas maneras eres capaz de hacerlo?
Crea el código para cada una de ellas.
"""

def count_with_for():
    """Prints numbers from 1 to 100 using a for loop."""
    for i in range(1, 101):
        print(i, end="-")

def count_with_while():
    """Prints numbers from 1 to 100 using a while loop."""
    count = 1
    while count <= 100:
        print(count, end="-")
        count += 1

def count_with_recursion(n: int = 1):
    """Prints numbers from 1 to 100 using recursion."""
    if n > 100:
        return
    print(n, end="-")
    count_with_recursion(n + 1)

def count_with_join_comprehension():
    """Prints numbers from 1 to 100 using str.join and list comprehension."""
    print("-".join(str(i) for i in range(1, 101)))

def count_with_join_map():
    """Prints numbers from 1 to 100 using str.join and map."""
    print("-".join(map(str, range(1, 101))))

def count_with_unpacking():
    """Prints numbers from 1 to 100 using unpacking and sep."""
    print(*range(1, 101), sep="-")


if __name__ == "__main__":
    count_with_for()
    print()
    count_with_while()
    print()
    count_with_recursion()
    print()
    count_with_join_comprehension()
    count_with_join_map()
    count_with_unpacking()
