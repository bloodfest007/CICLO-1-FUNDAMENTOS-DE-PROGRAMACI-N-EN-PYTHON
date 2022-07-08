print("-------------------------------------------------------")
print("Calcular promedios de notas de un estudiante")
print("-------------------------------------------------------")
nombre = input("Digite Nombre: ")
n1 = float(input("Digite Nota 1: "))
n2 = float(input("Digite Nota 2: "))
n3 = float(input("Digite Nota 3: "))

prom = (n1 + n2 + n3) / 3

print("La nota del estudiante", nombre, "es de: ", round(prom, 2))
print("-------------------------------------------------------")
