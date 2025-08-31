def bubble_sort(fila):
    """Ordena una lista (fila de la matriz) usando Bubble Sort"""
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


def ordenar_fila(matriz, fila_index):
    """Ordena en orden ascendente la fila 2 de la matriz"""
    if 0 <= fila_index < len(matriz):
        bubble_sort(matriz[fila_index])
    else:
        print("Índice de fila fuera de rango.")


def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


# Programa principal
if __name__ == "__main__":
    # Matriz 3x3
    matriz = [
        [9, 3, 5],
        [7, 1, 8],
        [4, 6, 2]
    ]

    print("Matriz original:")
    imprimir_matriz(matriz)

    # Ordenar la segunda fila (índice 1)
    ordenar_fila(matriz, 1)

    print("\nMatriz con la fila 2 ordenada:")
    imprimir_matriz(matriz)
