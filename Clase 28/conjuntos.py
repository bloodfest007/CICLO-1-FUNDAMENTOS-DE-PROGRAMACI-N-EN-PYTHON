print("---------")
print("Conjuntos")
print("---------")

#*Definicion de un conjunto
mi_conjunto= {1,2,3} 
print(mi_conjunto)
print("---------")

#*Admite dentro de sus elementos una tupla o tipo de datos no inmutables, ver guia
mi_conjunto= {1.0,"Hello",(1,2,3)} 
print(mi_conjunto)
print("---------")

#*No admite elementos repetidos dentro de los conjuntos
mi_conjunto= {1,2,3,4,3,2} 
print(mi_conjunto)
print("---------")

#*Se usa el metodo set para crear elementos en un conjunto
mi_conjunto= set([1,2,3,2])
print(mi_conjunto)
print("---------")

#*Aqui presenta error porque una lista es un tipo de dato mutable
#mi_conjunto= {1,2,[3,4]}
#print(mi_conjunto)

#*Uso del add para añadir un elemento en un conjunto
mi_conjunto = {1,2,3} 
mi_conjunto.add(8)
mi_conjunto.add(5)
mi_conjunto.add("Sopa")
print(mi_conjunto)
print("---------")

#*Recorrido de conjunto usando un For
#for i in mi_conjunto: 
#    print(i)

#* Permite agregart una lista en el conjunto
mi_conjunto.update([4,5,6,7,"libro",10])
print(mi_conjunto)
print("---------")

#^Metodos discard(), remove(),pop(), clear()
#*remove() Elimina elementos de un conjunto avisando si no existe
mi_conjunto.remove("Sopa")
print(mi_conjunto)
print("---------")

#*discard() elimina elementos de un conjunto si existe
mi_conjunto.discard("metal")
print(mi_conjunto)
print("---------")

#*pop() elimina elementos de un conjunto al azar
mi_conjunto.pop()
print(mi_conjunto)
print("---------")

#*clear() Elimina totalmente los elementos de un conjunto
mi_conjunto.clear()
print(mi_conjunto)
print("---------")


































