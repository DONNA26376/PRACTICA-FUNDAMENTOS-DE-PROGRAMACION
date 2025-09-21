# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total.

    Parámetros:
    monto_total (float): El valor total de la compra.
    porcentaje_descuento (float, opcional): El porcentaje de descuento (por defecto 10%).

    Retorna:
    float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
# 1. Llamada solo con el monto (usa descuento por defecto del 10%)
monto1 = 100.0
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

print("Compra 1:")
print(f"Monto total: ${monto1:.2f}")
print(f"Descuento aplicado: ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")

# 2. Llamada con monto y porcentaje de descuento específico
monto2 = 200.0
porcentaje2 = 20
descuento2 = calcular_descuento(monto2, porcentaje2)
monto_final2 = monto2 - descuento2

print("Compra 2:")
print(f"Monto total: ${monto2:.2f}")
print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")