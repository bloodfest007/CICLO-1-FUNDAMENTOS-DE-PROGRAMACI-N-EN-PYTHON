from urllib.error import ContentTooShortError


print("---------")
print("Ejercicio")
print("---------")

valorTotal = 0
cantidadCajas = int(input("Digite cantidad de cajas: "))

for i in range(1, cantidadCajas + 1):
    
    alto = float(input("Digite alto de la caja: "))
    costo = float(input("Digite costo: "))

    if (alto >= 45):
        costo += 3000

    if (costo >= 20000):
        costo *= 1.19

    valorTotal += costo
    print("El valor total de cajas es:", costo)
    
print("El valor total es: ", valorTotal)
