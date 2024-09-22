# Função para calcular o número de ataques entre rainhas
def calcular_ataques(tabuleiro, N):
    ataques = 0
    for i in range(N):
        for j in range(i + 1, N):
            # Verifica se duas rainhas estão na mesma linha ou diagonal
            if tabuleiro[i] == tabuleiro[j] or abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                ataques += 1
    return ataques

# Função para gerar um tabuleiro inicial fixo
def gerar_tabuleiro_inicial(N):
    return [i for i in range(N)]  # Inicia com as rainhas posicionadas em linhas diferentes, coluna crescente

# Função para encontrar a melhor vizinhança
def obter_vizinho(tabuleiro, N):
    melhor_tabuleiro = tabuleiro[:]
    melhor_ataques = calcular_ataques(tabuleiro, N)

    # Tenta mover cada rainha para uma linha diferente e calcula os ataques
    for col in range(N):
        for row in range(N):
            if tabuleiro[col] == row:
                continue  # Se a rainha já estiver nesta linha, pula
            novo_tabuleiro = tabuleiro[:]
            novo_tabuleiro[col] = row
            ataques = calcular_ataques(novo_tabuleiro, N)

            if ataques < melhor_ataques:  # Se o novo tabuleiro for melhor, atualiza
                melhor_tabuleiro = novo_tabuleiro[:]
                melhor_ataques = ataques

    return melhor_tabuleiro, melhor_ataques

# Função principal que resolve o problema das N-Rainhas usando Hill Climbing
def N_rainhas_hill_climbing(N):
    # Gera uma solução inicial fixa
    tabuleiro = gerar_tabuleiro_inicial(N)
    ataques = calcular_ataques(tabuleiro, N)

    # Continua enquanto houver melhorias
    while True:
        # Encontra o melhor vizinho
        novo_tabuleiro, novo_ataques = obter_vizinho(tabuleiro, N)

        # Se o número de ataques não melhorar, termina o algoritmo
        if novo_ataques >= ataques:
            break

        # Atualiza o tabuleiro atual para o melhor vizinho
        tabuleiro = novo_tabuleiro
        ataques = novo_ataques

    # Exibe a solução encontrada
    print("Tabuleiro final:")
    exiba_tabuleiro(tabuleiro, N)
    print("Número de ataques:", ataques)

    # Se não houver ataques, uma solução foi encontrada
    if ataques == 0:
        print("Solução encontrada!")
    else:
        print("Máximo local atingido, sem solução perfeita.")

# Função para exibir o tabuleiro
def exiba_tabuleiro(tabuleiro, N):
    for i in range(N):
        linha = ["-"] * N
        linha[tabuleiro[i]] = "R"
        print(" ".join(linha))

# Executa o Hill Climbing para resolver o problema das N-Rainhas
N = int(input("Digite o número das (N) Rainhas: "))  # Defina o número de rainhas
N_rainhas_hill_climbing(N)
