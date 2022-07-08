print("---------------------------------------------------------------------------------")
print("Contadores")
print("---------------------------------------------------------------------------------")

manzana = 5
cont_manzanas = 0

print("Se ha iniciado el carrito. En total hay: "+ str(cont_manzanas)+ " manzanas")
cont_manzanas += 1 

while(cont_manzanas < manzana):
    print("Se ha agregado una manzana. Ahora hay: "+ str(cont_manzanas)+ " manzanas")
    cont_manzanas += 1 

print("-----------------------------------------")
numero = 5

while (numero > 0):
    print(numero)
    numero = numero - 1
   
else: 
    print("el recorrido ya llegó a donde se quería")
