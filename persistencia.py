"""docstring: Codigo fuernte persistencia"""
def guardar_pedido(nombre, apellidos, file_name):
    """docstring: funcion Duardar _pedido corregida"""
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()
