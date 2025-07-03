"""
Crea una función que imprima los 30 próximos años bisiestos
    siguientes a uno dado.
- Utiliza el menor número de líneas para resolver el ejercicio.
"""

last_leap_year = 2020
for i in range(0, 30):
    print(last_leap_year + (4 * i))
