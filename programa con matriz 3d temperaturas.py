
# Ciudades, semanas y días
ciudades = ["GUAYAQUIL", "QUITO", "CUENCA"]
semanas = 4
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Inicializamos la matriz 3D con valores de ejemplo
# temperaturas[ciudad][semana][día]
temperaturas = [
    [  # GUAYAQUIL
        [10, 11, 12, 13, 14, 15, 16],  # Semana 1
        [12, 15, 15, 18, 19, 20, 15],  # Semana 2
        [12, 15, 15, 18, 19, 20, 15],  # Semana 3
        [12, 13, 14, 15, 14, 13, 12],  # Semana 4
    ],
    [  # QUITO
        [10, 11, 12, 13, 14, 15, 16],  # Semana 1
        [12, 15, 15, 18, 19, 20, 15],  # Semana 2
        [18, 19, 10, 11, 12, 10, 19],  # Semana 3
        [17, 18, 19, 10, 11, 10, 18],  # Semana 4
    ],
    [  # CUENCA
        [12, 13, 14, 15, 14, 13, 12],  # Semana 1
        [11, 12, 13, 14, 15, 14, 13],  # Semana 2
        [18, 19, 10, 11, 12, 10, 19],  # Semana 3
        [17, 18, 19, 10, 11, 10, 18],  # Semana 4
    ]
]

# Calcular promedios semanales por ciudad
for i, ciudad in enumerate(ciudades):  # Recorremos ciudades
    print(f"\nCiudad: {ciudad}")
    for semana_idx in range(semanas):  # Recorremos semanas
        semana_temperaturas = temperaturas[i][semana_idx]
        promedio = sum(semana_temperaturas) / len(semana_temperaturas)
        print(f"Promedio de temperaturas en {ciudad}, Semana {semana_idx + 1}: {promedio:.2f} grados")
