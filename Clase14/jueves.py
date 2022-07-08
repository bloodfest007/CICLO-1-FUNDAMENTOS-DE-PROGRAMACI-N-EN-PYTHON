print("---------------------------------------------------------------------------------")
print("ACUMULADORES")
print("---------------------------------------------------------------------------------")

lista_compras = ""

precio_tornillo = 1200
cant_tornillo = 20

precio_pala = 32000
cant_pala = 2

precio_cemento = 20000
cant_cemento = 6

precio_destornillador = 4500
cant_pala = 8

precio_pintura = 18000
cant_pintura = 7

subtotal = 0

print("Lista de compras para ir a la ferreteria...")

lista_compras = lista_compras + "20 tornillos "
total_tornillo = precio_tornillo * cant_tornillo
subtotal = subtotal + total_tornillo

print("\n---Lista de compras")
print(lista_compras, "Total tornillos:", total_tornillo)

lista_compras = lista_compras + ", 2 palas "
total_pala = precio_pala * cant_pala
subtotal = subtotal + total_pala

print("\n---Lista de compras")
print(lista_compras, "Total pala:", total_pala)

lista_compras = lista_compras + ", 6 Bolsas de cemento "
total_cemento = precio_cemento * cant_cemento
subtotal = subtotal + total_cemento

print("\n---Lista de compras")
print(lista_compras, "Total cemento:", total_cemento)

print("\nLista de compras para ir a la ferreteria...")

lista_compras = lista_compras + ", 8 Destornillador "
total_destornillador = precio_destornillador * cant_tornillo
subtotal = subtotal + total_destornillador

print("\n---Lista de compras")
print(lista_compras, "Total Destornillador:", total_destornillador)

print("Lista de compras para ir a la ferreteria...")

lista_compras = lista_compras + "7 pinturas "
total_pintura = precio_pintura * cant_pintura
subtotal = subtotal + total_pintura

print("\n---Lista de compras")
print(lista_compras, "Total pintura:", total_pintura)

subtotal = subtotal * 1.19

print("\n---Total a pagar:", subtotal)