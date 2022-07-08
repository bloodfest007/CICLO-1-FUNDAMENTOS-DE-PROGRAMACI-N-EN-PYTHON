print("-------------------------------------------------------------")
print("Hacer un programa que ingrese por datos de entrada 3 Numeros"
      "donde van a comparar los numeros, si son iguales, mayor que"
      "o menor que o menor o mayor donde si son diferentes hagan un"
      "calculo matematico")
print("-------------------------------------------------------------")

a = int(input("Digite primer numero: "))
b = int(input("Digite segundo numero: "))
c = int(input("Digite tercer numero: "))

multiplicacion= a * b * c

if a == b and b == c:
   print(a,",", b,"y", c, "son iguales")

elif a > b and a > c:
    print(a, "es mayor que", b, "y que", c, ", multiplicacion:", multiplicacion)

elif a > b and a > c:
    print(a, "es mayor que", b, "y que", c, ", multiplicacion:", multiplicacion)

else: 
    print(a, "es menor que", b, "y que", c, ", multiplicacion:", multiplicacion)

print("-------------------------------------------------------------")