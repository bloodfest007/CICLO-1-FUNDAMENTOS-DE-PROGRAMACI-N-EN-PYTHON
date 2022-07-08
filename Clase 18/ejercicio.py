#una empresa requiere un programa que le calcule la cantidad de cemento vendido en el dia, se deben definir uynas variables iniciales costototal = 0
#y cantifad de cemento se va a definir tpor teclado. Dentro del ciclo for van a solicitar por teclado los kilos del cemento y el valor del cemento.

#condicion 1 si 25 kgs es mayor o igual el valor va a ser de 15000 y se le adiciona 3000 al valor
#condicion 2 sison 50 kilos va a ser de 30000 y se le adiciona el iva del 19%, al final se va almacenar las ventas en la variable costo total. 

#Deben imprimir por ciclo el valor del cemento

print("---------")
print("Ejercicio")
print("---------")

costoTotal = 0
cantidadCemento = int(input("Ingresa cantidad de cemento: "))

for i in range(1,cantidadCemento + 1) :
    peso = float(input("\nIngresa el peso: "))
    costo = float(input("Ingrese el costo del cemento: "))

    if peso >= 25:
        costo = costo + 3000 
  
    if peso == 50 :
        costo = costo * 1.19

    print("El valor total del cemento es:", costo)
    costoTotal += costo

print("\nCosto total: ", costoTotal)

