print("---------------------------------------------------------------")
print("Calcular ganancia año tras año") 
print("---------------------------------------------------------------")

capitalInicial = float(input("Ingrese el valor a ahorrar: "))

#*el interes es fijo por año
gananciaPrimerAño = float(capitalInicial*(1.04))
gananciaSegundoAño = float(gananciaPrimerAño*(1.04))
gananciaTercerAño = float(gananciaSegundoAño*(1.04))

print("La ganancia del primer año es: ", round(gananciaPrimerAño,2))
print("La ganancia del segundo año es: ", round(gananciaSegundoAño,2))
print("La ganancia del tercer año es: ", round(gananciaTercerAño,2))
print("---------------------------------------------------------------")

print("----------------------------------------------------------------")
print("Calcular ganancia año tras año, otro modelo digitando el interes") 
print("----------------------------------------------------------------")

capitalInicial = float(input("Ingrese el valor a ahorrar: "))
interes = float(input("Ingrese tasa de interes: "))

#*el interes se digita y es fijo por año
gananciaPrimerAño = (capitalInicial * interes/100) + capitalInicial
gananciaSegundoAño = (gananciaPrimerAño * interes/100) + gananciaPrimerAño
gananciaTercerAño = (gananciaSegundoAño * interes/100) + gananciaSegundoAño

print("La ganancia del primer año es: ", round(gananciaPrimerAño,2))
print("La ganancia del segundo año es: ", round(gananciaSegundoAño,2))
print("La ganancia del tercer año es: ", round(gananciaTercerAño,2))

print("----------------------------------------------------------------")