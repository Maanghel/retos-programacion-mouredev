"""
¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
    24 días, 24 regalos sorpresa relacionados con desarrollo de software,
    ciencia y tecnología desde el 1 de diciembre.

Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
    lo siguiente:
- Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
    de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
- Si la fecha es anterior: Cuánto queda para que comience el calendario.
- Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.

Notas:
- Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
    y finaliza a las 23:59:59.
- Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
    y segundos.
"""

from datetime import datetime, timedelta

def format_timedelta(delta: timedelta) -> str:
    """
    Converts a timedelta object into a human-readable string format.

    Args:
        delta (timedelta): The time difference to format.

    Returns:
        str: A human-readable string indicating days, hours, minutes and seconds.
    """
    total_seconds = int(delta.total_seconds())
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    parts = []
    if days:
        parts.append(f"{days} día{'s' if days != 1 else ''}")
    if hours:
        parts.append(f"{hours} hora{'s' if hours != 1 else ''}")
    if minutes:
        parts.append(f"{minutes} minuto{'s' if minutes != 1 else ''}")
    if seconds or not parts:
        parts.append(f"{seconds} segundo{'s' if seconds != 1 else ''}")

    return ", ".join(parts)

class AdventCalendar:
    """
    A utility class to interact with the Advent calendar of 2022.
    Provides information about gifts and timing related to a given date.
    """

    @staticmethod
    def day_gift(new_date: datetime) -> str:
        """
        Determines the gift of the day based on the Advent calendar and
        how much time remains until or since the event.

        Args:
            new_date (datetime): A datetime object representing the current date.

        Returns:
            str: Message containing gift or time to wait or passed, depending on the date.
        Raises:
            TypeError: If input is not a datetime object.
        """
        if not isinstance(new_date, datetime):
            raise TypeError("Se debe ingresar una fecha válida con año, mes, día, hora, minuto y segundo.")

        gifts = {
            1: "Libro - Git y Github desde cero",
            2: "Suscripcion mensual a Mouredev Pro",
            3: "Libro - Entiende la tecnologia",
            4: "Libro - Dominando JavaScript",
            5: "Libro - Codigo Sostenible",
            6: "Suscripcion mensual a Commit Academy",
            7: "Libro - Ultimate Python",
            8: "Libro - Aprender a programar con C#",
            9: "Libro - Git y github desde cero",
            10: "Suscripcion mensual a Mouredev Pro",
            11: "Suscripcion mensual a Hack4u",
            12: "Curso de Jetpack Compose o Firebase AppCademy",
            13: "Libro - El programador pragmatico",
            14: "Suscripcion mensual a Metal Code",
            15: "Suscripcion mensual a Hola Mundo",
            16: "Libro: Git y Github desde cero",
            17: "Suscripcion mensual a Mouredev Pro",
            18: "Libro - No todo es programar",
            19: "Libro - Clean JavaScript",
            20: "Libro - Patrones de diseño",
            21: "Libro - Curso intensivo de Python",
            22: "Dominio .dev anual en Raiola Networks",
            23: "Libro - Git y Github desde cero",
            24: "Suscripcion anual a Mouredev Pro"
        }

        START = datetime(2022, 12, 1, 0, 0, 0)
        END = datetime(2022, 12, 24, 23, 59, 59)

        if new_date < START:
            delta = abs(new_date - START)
            return f"Faltan {format_timedelta(delta)} para que comience el calendario de adviento."
        elif START <= new_date <= END:
            day = new_date.day
            gift = gifts.get(day, "Sin regalo asignado")
            end_day = datetime(2022, 12, new_date.day, 23, 59, 59)
            remaining = end_day - new_date
            return f"Regalo del día {day}: {gift}. Quedan {format_timedelta(remaining)} para que finalice el sorteo del día."
        else:
            delta = abs(new_date - END)
            return f"El calendario terminó hace {format_timedelta(delta)}."


if __name__ == "__main__":
    try:
        input_ = datetime(2022, 10, 3, 16, 30, 0)
        print(AdventCalendar.day_gift(input_))
    except TypeError as e:
        print(f"Error: {e}")
