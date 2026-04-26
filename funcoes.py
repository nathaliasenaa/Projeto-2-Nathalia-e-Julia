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

def calcula_pontos_full_house (dados_rolados):
    n=0 #contagem de quantas vezes o primeiro número aparece
    for x in dados_rolados:
        if x == dados_rolados[0]:
            n= n+1

    n2= None 
    for x in dados_rolados:
        if x != dados_rolados[0]:
            n2= x #definição do segundo número da lista
    if n2==None:
        return 0
    
    n_2 = 0 #contagem de quantas vezes o segundo número aparece
    for x in dados_rolados:
        if x == n2:
            n_2 = n_2 + 1
    
    if (n==3 and n_2==2) or (n==2 and n_2==3):
        soma=0 
        for x in dados_rolados:
            soma = soma + x 
        return soma 
    return 0

def calcula_pontos_quadra (dados_rolados):
    for x in dados_rolados:
        n=0 #contagem de quantas vezes o numero x aparece
        for n1 in dados_rolados:
            if n1==x: #verifica se o primeiro numero é igual aos proximos 
                n= n+1 #cada vez que encontra o mesmo numero soma na contagem de quantas vezes x aparece
        if n>=4:
            soma= 0
            for y in dados_rolados:
                soma = soma + y
            return soma 
    return 0

def calcula_pontos_quina (dados_rolados):
    for x in dados_rolados:
        n=0 
        for n1 in dados_rolados:
            if n1==x: 
                n= n+1 
        if n>=5:
            return 50 
    return 0

def calcula_pontos_regra_avancada (dados_rolados): 
    pontos = { 
        'cinco_iguais': calcula_pontos_quina (dados_rolados), 
        'full_house': calcula_pontos_full_house (dados_rolados), 
        'quadra': calcula_pontos_quadra (dados_rolados), 
        'sem_combinacao': calcula_pontos_soma(dados_rolados), 
        'sequencia_alta': calcula_pontos_sequencia_alta(dados_rolados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados_rolados)
    }
    return pontos

def faz_jogada (dados_rolados, categoria, cartela): 
    pontos_simples = calcula_pontos_regra_simples(dados_rolados)
    pontos_avancados = calcula_pontos_regra_avancada(dados_rolados)

    if categoria == '1' or categoria == '2' or categoria =='3' or categoria == '4' or categoria == '5' or categoria =='6': 
        categoria_numero = int(categoria)
        cartela['regra_simples'][categoria_numero] = pontos_simples[categoria_numero]
    else: 
        cartela['regra_avancada'][categoria] = pontos_avancados[categoria] 
    
    return cartela 






















































































































































































































