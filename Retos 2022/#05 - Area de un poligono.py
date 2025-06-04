"""
Crea una única función (importante que sólo sea una) que sea capaz
    de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""

def polygon_area(polygon: dict) -> float:
    """
    Calculate and return the area of a polygon.

    Supported polygons:
    - triangle: requires 'base' and 'height'
    - square: requires 'side'
    - rectangle: requires 'width' and 'height'
    
    Parameters:
    - polygon (dict): Dictionary with a 'type' key and necessary dimensions.

    Returns:
    - float: The area of the polygon.
    """
    type_ = polygon.get("type")

    if type_ == "triangle":
        base = polygon.get("base")
        height = polygon.get("height")
        return 0.5 * base * height
    elif type_ == "square":
        side = polygon.get("side")
        return side ** 2
    elif type_ == "rectangle":
        width = polygon.get("width")
        height = polygon.get("height")
        return width * height
    else:
        raise ValueError("Unsupported polygon type.")


print("Área del triángulo:", polygon_area({"type": "triangle", "base": 10, "height": 5}))
print("Área del cuadrado:", polygon_area({"type": "square", "side": 4}))
print("Área del rectángulo:", polygon_area({"type": "rectangle", "width": 8, "height": 3}))