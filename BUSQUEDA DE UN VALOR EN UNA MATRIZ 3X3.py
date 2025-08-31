
# Crear una matriz bidimensional (3x3)
matriz = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9]
]

# Búsqueda de un valor específico en la matriz 3X3
valor_buscado = 5
if any(valor_buscado in fila for fila in matriz):
    print(f"Se encontró {valor_buscado} en la matriz.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
