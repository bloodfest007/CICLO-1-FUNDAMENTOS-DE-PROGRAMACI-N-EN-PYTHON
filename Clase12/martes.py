print("---------------------------------------------------------------------------------")
print("Calcular precio del cemento, si el peso es de 25 kilos sumar 3000 a la variable")
print("costo del cemento. Si el peso es de 50 kilos le van a sumar el iva 19%")
print("---------------------------------------------------------------------------------")

kilos = float(input("Digite peso de Cemento: "))

#
#if kilos == 25:
#    precioCemento = 16000 + 3000
#    print("El precio del Cemento de 25 kgs es de", precioCemento)

#elif kilos == 50:
#    precioCemento = 32000 * 1.19
#    print("El precio del Cemento de 50 kgs es de", precioCemento)

#else: print("Solo tenemos en existencia 25 y 50 kilos")
    

#!OTRA FORMA ESTILO RETO

print("---------------------------------------------------------------------------------")
print("Calcular precio del cemento, si el peso es de 25 kilos sumar 3000 a la variable")
print("costo del cemento. Si el peso es de 50 kilos le van a sumar el iva 19%")
print("---------------------------------------------------------------------------------")

kilos = float(input("Digite peso de Cemento: "))

if kilos == 25:
    precioCemento = 16000 + 3000
    print("El precio del Cemento de 25 kgs es de", precioCemento)

if kilos == 50:
    precioCemento = 32000 * 1.19
    print("El precio del Cemento de 50 kgs es de", precioCemento)



#!Estilo profesor
print("---------------------------------------------------------------------------------")

peso = float(input("Ingresa el peso: "))
costo = float(input("Ingrese el costo del cemento"))

if peso < 26:
    costo += 3000 #& Esto es un acumulador, lo que tiene costo almacenado, se le suma
    print("El valor total del cemento es:", costo)

if peso > 25:
    costo *= 1.19
    print("El valor total del cemento es:", costo)
