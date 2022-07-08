#print("---------------------------------------------------------------------------------")
#print("EJERCICIO WHILE")
#print("---------------------------------------------------------------------------------")

#numero = 6
#while (numero <= 10):
#    print(numero)
#    numero = numero + 1
      
#else: 
#    print("\nel recorrido con WHILE finalizó")

#print("---------------------------------------------------------------------------------")
#print("EJERCICIO FOR")
#print("---------------------------------------------------------------------------------")

#num = 6

#for i in range(6, 11, 1):
#    print(i)
    
#print("\nel recorrido con FOR finalizó")

#print("---------------------------------------------------------------------------------")
#print("Hacer un programa que reciba una contraseña en una variable contraseña reciba por")
#print("teclado")
#print("---------------------------------------------------------------------------------")


#contraseña = "grupoA71"
#password = ""

#while (password != contraseña):
#      password = input("\nDigite contraseña: ")

#     if(password == contraseña):
#         print("contraseña correcta!")
#         
#     elif (password != contraseña):
#        print("contraseña Incorrecta!")



print("----------------------------------------------------------------------------------")
print("Hacer un programa que pida la cifra a depositar, y le pida el interes por año, que")
print("el interes por año")
print("---------------------------------------------------------------------------------")

capitalInicial = float(input("Ingrese el valor a ahorrar: "))
interes = float(input("Ingrese tasa de interes: "))
año = int(input("Ingrese los años: "))
gananciaAño = 0
print("")

for año in range(1, año + 1):
    ganancia = (capitalInicial * interes/100)
    gananciaAño += ganancia
    print("La ganancia del año " + str(año) + " es: ", round(gananciaAño,2))
    print("")

