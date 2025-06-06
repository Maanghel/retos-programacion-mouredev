"""
Crea un programa que comprueba si los paréntesis, llaves y corchetes
    de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran
    en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios.
    No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

def balanced_expression(expression: str) -> bool:
    """
    Checks whether the given expression has balanced parentheses '()', 
    brackets '[]', and braces '{}'.

    An expression is considered balanced if each opening symbol has a 
    corresponding closing symbol, and all are properly nested in the correct order.

    Parameters:
        expression (str): The input string containing the expression to validate.

    Returns:
        bool: True if the expression is balanced, False otherwise.
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack

print(balanced_expression("{ [ a * ( c + d ) ] - 5 }"))
print(balanced_expression("{ a * ( c + d ) ] - 5 }"))
print(balanced_expression("(((())))"))
print(balanced_expression("{[(])}"))
print(balanced_expression("({[]})"))
print(balanced_expression("["))
print(balanced_expression(""))
