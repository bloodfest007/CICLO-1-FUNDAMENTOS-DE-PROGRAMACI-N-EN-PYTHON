def procesar_dato(peso,volumen):
    if (peso < 2  and volumen < 0.027):
       return True
    else: 
       return False
    
def par_impar(N):
    if (N%2==0):
        return True
    else:
        return False

def peso_a_euro(valor):
    return valor/4500
