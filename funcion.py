def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Parameters:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, optional): El porcentaje de descuento a aplicar. Por defecto es 10.

    Returns:
        float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función calcular_descuento desde el programa principal
monto_compra1 = 1000
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

monto_compra2 = 1500
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

# Muestra los resultados
print("Llamada 1:")
print("Monto de la compra:", monto_compra1)
print("Porcentaje de descuento aplicado: 10%")
print("Descuento aplicado:", descuento1)
print("Monto final a pagar después del descuento:", monto_final1)

print("\nLlamada 2:")
print("Monto de la compra:", monto_compra2)
print("Porcentaje de descuento aplicado:", porcentaje_descuento2, "%")
print("Descuento aplicado:", descuento2)
print("Monto final a pagar después del descuento:", monto_final2)
