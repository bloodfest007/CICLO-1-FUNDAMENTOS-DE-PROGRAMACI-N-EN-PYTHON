"""e necesita obtener el promedio simple de un estudiante a partir de sus tres notas parciales"""

n1 = float(input("Digite primera nota: "))
n2 = float(input("Digite segunda nota: "))
n3 = float(input("Digite tercera nota: "))

prom = (n1 + n2 + n3) / 3

print("El promedio es "+ str(round(prom,2)))