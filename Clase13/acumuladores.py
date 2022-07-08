print("---------------------------------------------------------------------------------")
print("ACUMULADORES")
print("---------------------------------------------------------------------------------")

lista_compras = ""

precio_manzana = 1200
cant_manzana = 5

precio_cilantro = 200
cant_cilantro = 3

precio_perejil = 300
cant_perejil = 2

subtotal = 0

print("La abuelita está escribiendo su lista de compras...")

lista_compras = lista_compras + "5 manzanas "
total_manzana = precio_manzana * cant_manzana
subtotal = subtotal + total_manzana

print("\n---Lista de compras")
print(lista_compras, "Total Manzana:", total_manzana)

lista_compras = lista_compras + ", 3 lb Cilantro "
total_cilantro = precio_cilantro * cant_cilantro
subtotal = subtotal + total_cilantro

print("\n---Lista de compras")
print(lista_compras, "Total Cilantro:", total_cilantro)

lista_compras = lista_compras + ", 3 lb Perejil"
total_perejil = precio_perejil * cant_perejil
subtotal = subtotal + total_perejil

print("\n---Lista de compras")
print(lista_compras, "Total perejil:", total_perejil)



print("\n---Total a pagar:", subtotal)
