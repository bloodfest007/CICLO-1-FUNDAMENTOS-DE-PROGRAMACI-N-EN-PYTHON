#*condicionales anidados combinados

edad = int(input("Por Favor ingrese edad: "))

if edad > 0:
     print(" ya confirmo la edad", edad)
     
     if edad >= 18:
        print("Es mayor de edad")

        if edad >= 50:
            print("Es una persona con mas de 50 años")

else:
    print("Edad Incorrecta", edad)