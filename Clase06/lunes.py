print("---------------------------------------------------------------------------------")
print("Escribir un programa que pida al usuario su peso en kg y estatura y hallar el IMC")
print("---------------------------------------------------------------------------------")

peso=float(input("Digite su peso en KG: "))
altura=float (input("Digite su altura en M: "))

imc = peso / (altura**2)

print ("Su IMC es de: ", round(imc,2))
print("-------------------------------------------------------")

print("---------------------------------------------------------------")
print("Calcular interes porcentual anual y numero de años y mostrar") 
print("el capital obtemnido en la inversion redondeado en 2 decimales")
print("---------------------------------------------------------------")

capitalinicial = float(input("Digite capital inicial: "))
interes = float(input("Digite el interes porcentual anual: "))
año = int(input("Digite el tiempo en años: "))

cdt = (capitalinicial * interes / 100) * año

print("Capital obtenido: ", round(cdt + capitalinicial,2))

print("---------------------------------------------------------------")
