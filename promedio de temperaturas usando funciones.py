def promedio_temperaturas(datos):
    """
    Calcula la temperatura promedio de cada ciudad.
    Retorna:
        El promedio de cada ciudad
    """
    promedios = {}
    for ciudad, temps in datos.items():
        if temps:  # evitar división por cero
            promedio = sum(temps) / len(temps)
        else:
            promedio = None
        promedios[ciudad] = promedio
    return promedios


# parametros de ciudad y temperaturas
datos_temperaturas = {
    "Quito": [18, 19, 20, 21, 20, 18, 20],
    "Guayaquil": [28, 19, 30, 31, 20, 16, 17],
    "Cuenca": [16, 17, 19, 18, 16, 19, 19]
}
# almacenamos el promedio de temperaturas en la variable resultado
resultado = promedio_temperaturas(datos_temperaturas)
# se imprime el nombre de la ciudad con su respectivo promedio
print("Temperaturas promedio por ciudad:")
for ciudad, promedio in resultado.items():
    print(f"{ciudad}: {promedio:.2f} °C")