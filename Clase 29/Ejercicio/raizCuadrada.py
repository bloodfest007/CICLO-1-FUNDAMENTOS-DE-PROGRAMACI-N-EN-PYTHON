"""ELabore un algoritmo que lea los 3 lados de un triangulo cualquiera y calcule
su area, considerar: Si A, B, C son lados y S el semiperimetro"""

from cmath import sqrt
import math


a = float(input("Digite lado A: "))
b = float(input("Digite lado B: "))
c = float(input("Digite lado C: "))

ls = (a + b + c) / 2 #!Longitud semiperimetro

#area = (ls * (ls - a) * (ls - b) * (ls-c) )**(1/2) #!Forma de calcular Raiz al cuadrado
area =  (ls * (ls - a) * (ls - b) * (ls-c) )**(1/2)

#area1 = sqrt(ls * (ls - a) * (ls - b) * (ls-c))

print(area)
#print(type(area1))

