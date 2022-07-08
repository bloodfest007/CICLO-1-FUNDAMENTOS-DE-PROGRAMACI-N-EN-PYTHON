
#def promNotas(cantAsignaturas, nombre, a ,b ,c):
#    sum = 0
#    prom = float((a + b + c) / 3)
#    sum = sum + prom
#    print("\nLa nota del estudiante", nombre, "es de: ", round(prom, 2)) 
#    return sum

#print("---------")
#print("Ejercicio")
#print("---------")

#asig = int(input("Digite cantidad a repetir: "))

#for i in range(1, asig + 1):
    
#    nota1= float(input("Digite 1ra nota: "))
#    nota2= float(input("Digite 2da nota: "))
#    nota3= float(input("Digite 3ra nota: "))
   
#    print(promNotas(asig,"Victor", nota1, nota2, nota3))

def promNotas(cant, nombre):
    
    for i in range(1, cant + 1):
        sum = 0
        calificacion= float(input("Digite nota " + str(i)+ ": "))
        sum = sum + calificacion
        calc = calificacion / i
        sum = sum + calc
    
    print("\nLa nota del estudiante", nombre, "es de: ", round(sum, 2)) 
    return round(sum, 2)

print("---------")
print("Ejercicio")
print("---------")

promNotas(3,"Victor")

def volumen():
    a = int(input())
    an = int(input())
    pro = int(input())
    volumen1 = a * an * pro

volumen()

