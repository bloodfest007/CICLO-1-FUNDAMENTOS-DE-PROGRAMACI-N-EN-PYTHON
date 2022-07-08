def calcularCosto(alto, ancho, profundo):
    volumen = alto * ancho * profundo
    costo = volumen * 5
    if alto > 30:
       costo = costo + 2000
    if costo> 10000:
        costo = costo * 1.19
    return costo

def costoTotal (listaPaquetes, dto):
    costoTotal = 0
    for i in listaPaquetes:
        alto = i["ALTO"]
        ancho = i["ANCHO"]
        profundo = i["PROFUNDO"]
        costoTotal = costoTotal + calcularCosto(alto, ancho, profundo)
    costoTotal = costoTotal - (costoTotal * (dto /100))
    return costoTotal