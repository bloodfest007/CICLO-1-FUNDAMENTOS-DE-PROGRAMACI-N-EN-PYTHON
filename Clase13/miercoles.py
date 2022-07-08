print("---------------------------------------------------------------------------------")
print("BANDERAS")
print("---------------------------------------------------------------------------------")

#suma_realizada = False
#total = 2
#a = 5
#b = 10

#if (suma_realizada == False):
#   total = a + b
#    suma_realizada = True

#if suma_realizada == True:
#    print("Se ha realizado una suma y su valor es: " + str(total))

print("---------------------------------------------------------------------------------")
print("EJEMPLO")
print("---------------------------------------------------------------------------------")

contagio_validado = "Si"
paciente = "Lisa"

if (contagio_validado == "Si"):
    print("La paciente "+ paciente + " terminó cuarentena, se recomienda aplicar la prueba PCR")
    print("\nAplicando prueba...")
    contagio_validado = "Pendiente"

if (contagio_validado == "Pendiente"):
    print("\n"+ paciente + ", por favor valide en su correo el resultado de la prueba")
    contagio_validado = "No"

if (contagio_validado == "No"):
    print("\n"+ paciente + ", de acuerdo a su resultado, usted no tiene Covid")
    

contagio_validado= "si"
paciente = "lisa"

