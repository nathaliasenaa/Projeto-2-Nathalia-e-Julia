import random
def rolar_dados (n): 
    resultado = []
    for i in range (n): 
        dado = random.randint (1, 6)
        resultado.append (dado)
    return resultado 

def guardar_dado (dados_rolados, dados_guardados, indice): 
    dado = dados_rolados [indice] 
    dados_guardados.append(dado)
    dados_rolados.pop(indice) 
    return [dados_rolados, dados_guardados] 


def remover_dado (dados_rolados, dados_estoque, indice):
    dado= dados_estoque[indice]
    dados_rolados.append(dado)
    dados_estoque.pop(indice)
    return [dados_rolados, dados_estoque]

def calcula_pontos_regra_simples (faces_dados_rolados):
    calcula_pontos= {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0
    }
    for i in faces_dados_rolados:
        calcula_pontos[i]+=i
    return calcula_pontos























































































































































































































