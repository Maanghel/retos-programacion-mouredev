"""
Crea una función que evalúe si un/a atleta ha superado correctamente una
    carrera de obstáculos.
- La función recibirá dos parámetros:
    - Un array que sólo puede contener String con las palabras
        "run" o "jump"
    - Un String que represente la pista y sólo puede contener "_" (suelo)
        o "|" (valla)
- La función imprimirá cómo ha finalizado la carrera:
    - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
        será correcto y no variará el símbolo de esa parte de la pista.
    - Si hace "jump" en "_" (suelo), se variará la pista por "x".
    - Si hace "run" en "|" (valla), se variará la pista por "/".
- La función retornará un Boolean que indique si ha superado la carrera.
    Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""

def steeplechase(actions: list, obstacles: str) -> bool:
    """
    Evaluates whether an athlete successfully completed an obstacle course.

    The function takes a list of actions that can contain the words "run" or "jump",
    and a string representing the track with "_" for ground and "|" for hurdles.

    The athlete must do the following:
    - "run" on "_" (ground) is correct and does not modify the track.
    - "jump" on "|" (hurdle) is correct and does not modify the track.
    - "jump" on "_" (ground) is incorrect and converts that section to "x".
    - "run" on "|" (hurdle) is incorrect and converts that section to "/".

    The function returns `True` if the athlete correctly completed all sections,
    and `False` if any action was incorrect.

    Args:
    actions (list): A list of actions (strings "run" or "jump").
    obstacles (str): A string representing the track, composed of "_" (ground) and "|" (hurdles).

    Returns:
    bool: `True` if the athlete successfully completed the course, otherwise `False`.

    Raises:
        ValueError: If actions length is different to obstacles lenght.
    """
    if len(actions) != len(obstacles):
        raise ValueError("Las acciones y los obstáculos deben ser de la misma longitud.")

    modified_road = []
    for i, action in enumerate(actions):
        if action == "run" and obstacles[i] == "_":
            modified_road.append("_")
        elif action == "jump" and obstacles[i] == "|":
            modified_road.append("|")
        elif action == "run" and obstacles[i] == "|":
            modified_road.append("/")
        elif action == "jump" and obstacles[i] == "_":
            modified_road.append("x")

    final_road = "".join(modified_road)
    print(f"Pista final: {final_road}")

    return obstacles == final_road

if __name__ == "__main__":
    print(steeplechase(["run", "jump", "run", "jump","run"], "_||__"))
    print(steeplechase(["run", "jump", "run", "jump","run"], "_|_|_"))
