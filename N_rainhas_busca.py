# Função para verificar se a posição atual da rainha é segura
def verifica_seguro(tabuleiro, linha, coluna, N):
    # Verifica as colunas anteriores
    for i in range(coluna):
        if tabuleiro[linha][i] == 1:
            return False

    # Verifica a diagonal superior esquerda
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False

    # Verifica a diagonal inferior esquerda
    for i, j in zip(range(linha, N, 1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False

    return True

# Função recursiva para resolver o problema das N-Rainhas
def resolver_N_rainhas(tabuleiro, coluna, N):
    # Caso base: se todas as rainhas foram colocadas
    if coluna >= N:
        return True

    # Tenta colocar a rainha em cada linha desta coluna
    for i in range(N):
        if verifica_seguro(tabuleiro, i, coluna, N):
            # Coloca a rainha nesta posição
            tabuleiro[i][coluna] = 1

            # Recursivamente tenta colocar as rainhas nas próximas colunas
            if resolver_N_rainhas(tabuleiro, coluna + 1, N):
                return True

            # Se não funcionar, remove a rainha (backtracking)
            tabuleiro[i][coluna] = 0

    # Se a rainha não puder ser colocada em nenhuma linha desta coluna, retorna False
    return False

# Função para exibir o tabuleiro
def exiba_tabuleiro(tabuleiro, N):
    for i in range(N):
        for j in range(N):
            print("R" if tabuleiro[i][j] == 1 else "-", end=" ")
        print()

# Função principal para resolver o problema das N-Rainhas
def N_rainhas(N):
    # Inicializa o tabuleiro com zeros
    tabuleiro = [[0 for _ in range(N)] for _ in range(N)]

    if not resolver_N_rainhas(tabuleiro, 0, N):
        print("Não existe solução")
        return False

    exiba_tabuleiro(tabuleiro, N)
    print("Solução encontrada!")

# Defina o número de rainhas
N = int(input("Digite o Número das (N) Rainhas: "))

# Resolva o problema das N-Rainhas
N_rainhas(N)
