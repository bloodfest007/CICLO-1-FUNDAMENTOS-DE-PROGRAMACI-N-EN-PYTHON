print("-------------------------------------------------------")
print("Operadores")
#!Operadores pendiente mayuscula al principio

print(True and False)
print(False and False)
print(False and True)
print(True and True)

print("-------------------------------------------------------")
print("Operador OR")
#!Operadores OR

x = 5
y = 5

print(x > 5 or y == 5)

print("-------------------------------------------------------")
print("Operador NOT")
#!Operadores NOT
print(not True)

print("-------------------------------------------------------")
print("Precedencia de operadores")
#!Precedencia de operadores
x = True
y = False
z = False
print(not z and (x or y))
print(not y and (z or x))
print(not x and (y or z))

print("-------------------------------------------------------")
print("Ejercicio 2")
#!Ejercicio 2

x = True
y = False
z = False

print(not(not z and not(x or y)))

