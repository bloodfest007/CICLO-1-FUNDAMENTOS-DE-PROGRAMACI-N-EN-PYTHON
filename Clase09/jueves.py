from socket import NI_NUMERICHOST


print("-------------------------------------------------------")
print("Ejercicio")
print("-------------------------------------------------------")

edad=int(input("Digite edad: "))

valorBoleta1 = 0
valorBoleta2 = 5000
valorBoleta3 = 12000
valorBoleta4 = 18000
valorBoleta5 = "Invitado"

if edad  >=0 and edad < 8:
    print("Valor boleta", valorBoleta1)

elif edad >= 8 and edad <= 15:
    print("Valor boleta: ", valorBoleta2)

elif edad >= 16 and edad <= 29:
    print("Valor boleta: ", valorBoleta3)

elif edad >= 30 and edad <= 60:
    print("Valor boleta: ", valorBoleta4)

elif edad > 60:
    print("Valor boleta:", valorBoleta5)

else: 
    print("Valor boleta indeterminado")

    