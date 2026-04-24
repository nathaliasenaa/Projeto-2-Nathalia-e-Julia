import random
def rolar_dados (n): 
    resultado = []
    for i in range (n): 
        dado = random.randint (1, 6)
        resultado.append (dado)
    return resultado 

