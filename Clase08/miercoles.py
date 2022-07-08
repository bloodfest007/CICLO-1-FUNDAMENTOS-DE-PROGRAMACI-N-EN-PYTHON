print("----------------------------------------------------------------")
print("IF - ELSE") 
print("----------------------------------------------------------------")

num = int(input("Introduzca un número: "))

if num == 100:
    print("Usted escribió 100")
elif num > 100:
    print("Usted escribió un número mayor que 100")
else:
    print("Usted escribió un número mayor que 100")

print("-------------------------------------------------------")
print("Calcular promedios de notas de un estudiante")
print("-------------------------------------------------------")
nombre = input("Digite Nombre: ")
n1 = float(input("Digite Nota 1: "))
n2 = float(input("Digite Nota 2: "))
n3 = float(input("Digite Nota 3: "))

prom = (n1 + n2 + n3) / 3

if prom >= 3 and prom <=5:
   print("La nota del estudiante", nombre, "es de: ", round(prom, 2), "y aprobó el año")
elif prom >= 0 and prom <=2.9:
     print("La nota del estudiante", nombre, "es de: ", round(prom, 2), "y no aprobó el año")
else:
    print("Nota fuera del rango")

print("----------------------------------------------------------------")
print("EJEMPLO") 
print("----------------------------------------------------------------")

print ("--- Adivina Mi Número ---")
num = int( input('Indtroduzca un número: '))
compara = 6
if(num != compara ):
    print(f'El número {num} es diferente a {compara} ')
elif(num == compara ):
    print(f'El número digitado {num} igual a {compara} ')
elif(num < compara ):
    print(f'El número digitado {num} es menor a {compara} ')
elif(num > compara ):
    print(f'El número digitado {num} es mayor a {compara} ')
else:
    print(f'El número digitado es Cero')
