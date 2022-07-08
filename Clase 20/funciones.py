print("---------")
print("Funciones")
print("---------")


#*Primera forma
#def mensaje():
#    print("Buenos dias")
#    print(" estudiantes")
#    print(" de python")

#mensaje()
#mensaje()
#mensaje()
#mensaje()

#*Segunda forma
#def suma():
#    num1 = int(input("Digite un numero: ")) 
#    num2 = int(input("Digite un numero: "))

#suma = num1 + num2
#    print(suma)    

#suma()

#*Tercera forma
#def suma():
#    num1 = int(input("Digite un numero: ")) 
#    num2 = int(input("Digite un numero: "))

#    print(num1 + num2)    

#suma()

#*Pasando valores por argumentos o parametros, usando return imprimiendo sobre la funcion invocada
#def suma(num1, num2):
#    operacion = num1 + num2

#    return operacion

#a = print(suma(65, 6))
#b = print(suma(66, 25))
#c = print(suma(67, 51))
#d = print(suma(68, 48))

#def suma(num1, num2):
#    operacion = num1 + num2

#    return operacion

#sumar1 = suma(5,3)
#sumar2 = suma(10,20)

#print("La sumatoria de la variable suma es:", sumar1,"y de suma 2 es: ", sumar2)

#*importando funcion datetime y formateando un poco el texto -->>Leer guia sobre formateo de texto
#from datetime import datetime

#def chat(name, msg = 'hola'):
#    date = datetime.now()
#    print("{}:  {}".format(name, msg))
#    return date

#mensaje = print(chat("Victor"))
#chat("\nVictor")
#chat(msg = "Hola, como estas?", name = "Pedro")

#* Factorial de un numero usando funciones
#def factorial(n):
#    if (n == 1 or n == 0):
#       return n

#    elif n < 1:
#        return ("No existe el factorial de numeros negativos!")
    
#    else: return n* factorial(n-1)

#print("---------")
#print("Ejercicio")
#print("---------")

#fact = int(input("Digite numero para calcular factorial: "))
#print(factorial(fact))
#def factorial(n):
    
#    if (n == 1 or n == 0):
#       return n

#    elif n < 1:
#        return ("No existe el factorial de numeros negativos!")
    
#    else: 
#        for i in range(n + 1):
#            n = n * i

#    return fact

#print("---------")
#print("Ejercicio")
#print("---------")

#fact = int(input("Digite numero para calcular factorial: "))
#print(factorial(fact))

