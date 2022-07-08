"""elaborar un algoritmo que solicite le numero de respuestas correctas, incorrectas
y en blanco, correspondientes a postulantes y muestre su puntaje final considerando 
que por cada respuesta correcta tendrá 4 puntos, respuestas incorrectas tendrá -1 y 
en blanco tendrá 0"""

respuestasCorrectas = int(input("Digite numero de respuestas correctas: "))
respuestasIncorrectas = int(input("Digite numero de respuestas incorrectas: "))
respuestasBlanco = int(input("Digite numero de respuestas en blanco: "))

prc = respuestasCorrectas * 4
pri = respuestasIncorrectas * -1
prb = respuestasBlanco * 0

puntaje = prc + pri + prb

print("El puntaje es de:", puntaje )




