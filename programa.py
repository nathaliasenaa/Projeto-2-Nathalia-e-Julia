from funcoes import *
dados_rolados = rolar_dados(5)
dados_guardados = []

cartela = {
    "regra_simples": {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    "regra_avancada": {
        "sem_combinacao": -1,
        "quadra": -1,
        "full_house": -1,
        "sequencia_baixa": -1,
        "sequencia_alta": -1,
        "cinco_iguais": -1
    }
}

rodada = 0

while rodada < 12:
    rerrolagens = 0
    terminou_rodada = False

    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")

    while terminou_rodada == False:
        opcao = input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        if opcao == "1":
            indice = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
            listas = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = listas[0]
            dados_guardados = listas[1]

        elif opcao == "2":
            indice = int(input("Digite o índice do dado a ser removido (0 a 4):"))
            listas = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = listas[0]
            dados_guardados = listas[1]

        elif opcao == "3":
            if rerrolagens < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens = rerrolagens + 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            categoria = input("Digite a combinação desejada:")

            if categoria == "1" or categoria == "2" or categoria == "3" or categoria == "4" or categoria == "5" or categoria == "6":
                categoria_numero = int(categoria)

                if cartela["regra_simples"][categoria_numero] == -1:
                    cartela = faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                    terminou_rodada = True
                    rodada = rodada + 1
                else:
                    print("Essa combinação já foi utilizada.")

            elif categoria in cartela["regra_avancada"]:
                if cartela["regra_avancada"][categoria] == -1:
                    cartela = faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                    terminou_rodada = True
                    rodada = rodada + 1
                else:
                    print("Essa combinação já foi utilizada.")

            else:
                print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

        if terminou_rodada == False:
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")

    dados_rolados = rolar_dados(5)
    dados_guardados = []

pontuacao = 0

for i in cartela["regra_simples"]:
    pontuacao = pontuacao + cartela["regra_simples"][i]

for i in cartela["regra_avancada"]:
    pontuacao = pontuacao + cartela["regra_avancada"][i]

soma_simples = 0
for i in cartela["regra_simples"]:
    soma_simples = soma_simples + cartela["regra_simples"][i]

if soma_simples >= 63:
    pontuacao = pontuacao + 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")