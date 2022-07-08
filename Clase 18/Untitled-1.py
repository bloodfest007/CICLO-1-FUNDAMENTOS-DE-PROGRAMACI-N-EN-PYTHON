
#value = 0
#it = 0

#while value < 10:
#    if value > 5:
#       value = value * 2
#    else:
#       value= value + 2
#    it = it + 1


#print(it)


numeroPaquetes = int(input())
costoTotal = 0

for i in range (0, numeroPaquetes):

    alto = float(input())
    ancho = float(input())
    profundo = float(input())

    volumen = alto*ancho*profundo
    costo = volumen*5

    if alto > 30:
        costo = costo + 2000
        costoTotal = costoTotal + costo
    if costo > 10000:
        costo = costo*1.19
        costoTotal = costoTotal + costo

print(costoTotal)