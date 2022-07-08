#print("---------------------------------------------------------------------------------")
#print("FOR")
#print("---------------------------------------------------------------------------------")

#print("Se ha iniciado el carrito. En total hay : 0 manzanas")

#for i in range(1,6):
    #print("Se ha agregado una manzana a la canasta. Ahora hay "+ str(i) +" manzanas" )
    #print("---------------------------------------------------------------------------------")

#print("---------------------------------------------------------------------------------")
#print("EJERCICIO")
#print("---------------------------------------------------------------------------------")

#palabra = input("Digite una palabra cualquiera: ")

#for i in range(1, 10):
 #   print(str(i) + ". "+ palabra)


print("-----------------------------------------------------------------------------------------")
print("Hacer un programa que reciba un dato entero por teclado, preguntando la edad, debe")
print("mostrar por pantalla todos los años que ha cumplido desde el primer el año hasta su edad")
print("----------------------------------------------------------------------------------------")

edad = int(input("Digite su edad: "))

for i in range(edad):
    if (i == 0):
        print(i, "Niño de meses") 
      
    print("Edad:",i + 1, "años")

print("tu edad actual es", edad)