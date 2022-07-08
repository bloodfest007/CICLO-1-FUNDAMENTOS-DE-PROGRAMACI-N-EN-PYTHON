from operator import truediv


print("---------------------------------------------------------------------------------")
print("WHILE")
print("---------------------------------------------------------------------------------")

numero= int (input("Por favor ingrese un numero que sea mayor a 2: "))
d = 2

if (numero >=1):
    print("Validando numero")

bandera = True

while (d < numero):
    if (numero % d == 0):
        bandera = False
    
    d+= 1

if (bandera):
    print(type(bandera))
    print(str(numero)+ "No es primo: ")
