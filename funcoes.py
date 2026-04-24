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

def calcula_pontos_soma (faces_dados): 
    n = 0 
    i = 0 
    while i < len(faces_dados): 
        n = n + faces_dados[i] 
        i = i + 1 
    return n

def calcula_pontos_sequencia_baixa (dados_rolados):
    if 1 in dados_rolados and 2 in dados_rolados and 3 in dados_rolados and 4 in dados_rolados: 
        return 15 
    if 2 in dados_rolados and 3 in dados_rolados and 4 in dados_rolados and 5 in dados_rolados: 
        return 15 
    if 3 in dados_rolados and 4 in dados_rolados and 5 in dados_rolados and 6 in dados_rolados: 
        return 15 
    else: 
        return 0 

def calcula_pontos_sequencia_alta (dados_rolados): 
    if 2 in dados_rolados and 3 in dados_rolados and 4 in dados_rolados and 5 in dados_rolados and 6 in dados_rolados: 
        return 30 
    if 1 in dados_rolados and 2 in dados_rolados and 3 in dados_rolados and 4 in dados_rolados and 5 in dados_rolados: 
        return 30 
    else: 
        return 0 























































































































































































































