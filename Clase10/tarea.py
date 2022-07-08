print("---------------------------------------------------------------------------------")
print("Escribir un programa que pida al usuario su peso en kg y estatura y hallar el IMC")
print("---------------------------------------------------------------------------------")

peso = float(input("Digite su peso en KG: "))
altura = float (input("Digite su altura en M: "))

imc = peso / (altura**2)

clasificacion1 = "Bajo peso"
clasificacion2 = "Normal"
clasificacion3 = "Sobre Peso"
clasificacion4 = "Obesidad"
clasificacion5 = "Obesidad I"
clasificacion6 = "Obesidad II"
clasificacion7 = "Obesidad III o Mórbida"

if imc <= 18.5:
   print("el IMC es de", round(imc,2), "por lo tanto estas en",clasificacion1)

elif imc > 18.5 and imc <= 24.9:
    print("el IMC es de", round(imc,2), "por lo tanto estas en",clasificacion2)

elif imc >= 25 and imc <= 29.9:
    print("el IMC es de", round(imc,2), "por lo tanto estas en",clasificacion3)

elif imc == 30:
    print("el IMC es de", round(imc,2), "por lo tanto estas en",clasificacion4)

elif imc > 30 and imc <= 34.9:
    print("el IMC es de", round(imc,2), "por lo tanto estas en",clasificacion5)

elif imc >= 35 and imc <= 39.5:
    print("el IMC es de", round(imc,2), "por lo tanto estas en",clasificacion6)

else: 
     print("el IMC es de", round(imc,2), "por lo tanto estas en",clasificacion7)
     
print("---------------------------------------------------------------------------------")