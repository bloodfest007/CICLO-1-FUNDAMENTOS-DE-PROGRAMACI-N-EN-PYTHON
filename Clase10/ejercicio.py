print("---------------------------------------------------------------------------------")
print("Salario")
print("---------------------------------------------------------------------------------")

empleado = input("Digite nombre del empleado: ")
salario = int(input("Salario: "))

if salario >= 1800000:
    print("El salario de", empleado, "es de", salario, "y es empleado de planta")

elif salario <= 1400000 and salario >= 1000000:
    print("El salario de", empleado, "es de", salario, "y es empleado contratista")

elif salario <= 800000 and salario >= 400000:
    print("El salario de", empleado, "es de", salario, "y es empleado por obra y labor")

elif salario < 400000 and salario >= 0:
    print("El salario de", empleado, "es de", salario, "y es empleado por horas")

else: 
    print("El salario de ",empleado, "no está catalogado", salario)

print("---------------------------------------------------------------------------------")
