
("---------")
print("Ejercicio")
print("---------")

#x = list(range(2, 21, 2))
#print(x)

#print("\n---------")

#x = list(range(16, -10, -2))
#print(x)

#print("\n---------")

#lista = [1, 2.5, 'Code', [5,6], 4]
#print(lista[1:3])
#print(lista[1:6])
#print(lista[1:6:2])
#print(lista[::-1])
#print(lista[::1])

#print("\n---------")

#lista = [1, 2.5, "Enya Isabel", [5, 6], 99] 

#for element in lista:
 #   print(lista)

#print("\n---------Append*********")
#* añade elemento al final
#my_list = [2,3,"DevCode", 1.2, 5]
#my_list.append(10)
#my_list.append([3,9])

#print(my_list)

#print("\n---------Insert*********")
#* añade elemento dando la posicion
#Nombres = ["David", "Elkin", "Juliana", "Silvia"]
#Nombres.insert(1,"Ivon")
#print(Nombres)

#Nombres.insert(1,"Carmen")
#print(Nombres)

#Nombres.insert(5,"Joel")
#print(Nombres)


#Nombres = ["David", "Elkin", "Juliana", "Silvia", "Elkin",  "Elkin","Felipe" ]

#Nombres.remove("Elkin")
#print(Nombres)

#Nombres.pop(1)
#print(Nombres)

#hobbies = ["Fotografia", "Lectura", "VideoJuegos","natacion"]

#for element in hobbies:
#    print("Mis Hobbies son: " + str(hobbies))

"""#!DICCIONARIOS
nombre = input("Su nombres es: ")
apellidos = input("Su Apellidos: ")
edad = input("Su edad es: ")
correo = input("Su correo es: ")
celular = input("Su numero es: ")
direccion = input("Su dirección es: ")

datos = {"Nombres" : nombre, "Apellidos" : apellidos, "Edad" : edad, "Correo" : correo,"Celular": celular ,"Direccion": direccion}

print(datos["Nombres"], datos["Apellidos"], datos["Edad"], datos["Correo"], datos["Celular"], datos["Direccion"])
"""

def materias(materia):
    materias = materia.split(",")
    return materias

materia = "Inglés,Física,Sociales,Historia,Programación"
print(materias(materia))
#
    
def listaFrutas(lista):
    for i in lista:
        print(i)

print(listaFrutas( ["Manzana", "Uva","Aguacate"]))

def multiplicarNumeros(numeros):
    mult = 1
    for i in numeros:
        mult *= i
    return mult

def multiplicarNumeros(numeros):
    import math
    mult = math.prod(numeros)
    return mult

print(multiplicarNumeros([2,3,5]))
