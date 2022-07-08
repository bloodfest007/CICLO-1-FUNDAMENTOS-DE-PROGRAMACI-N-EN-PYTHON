print("---------------------------------------------------------------------------------")
print("WHILE")
print("---------------------------------------------------------------------------------")

numero = int(input("Por favor ingrese un numero que sea mayor de 2: "))
d = 2

while (numero % d != 0):
     d+= 1

if (d == numero):
    print(numero, "Es numero primo")
else: 
    print(numero, "No es numero primo")

 