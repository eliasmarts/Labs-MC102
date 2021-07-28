def criar_lista(n):
    """Cria uma lista de tamanho n x n"""
    lista = [0]
    for i in range(n*n):
        lista.append('-')
    return lista

# A posicao na lista é uma ordenada relacionada a
# posicao no tabuleiro pela formula:
# posicao na lista = (linha - 1) * n + coluna
# a lista é cheia de '-', e as funcoes de movimento
# substituem as casas atacadas por 'x' e a posicao da
# peca por 'o'

def movimento_peao(n, coluna, linha):
    lista = criar_lista(n)
    posicao = (linha - 1) * n + coluna
    lista[posicao] = 'o'
    if linha == 2:
        lista[posicao + n] = 'x'
        lista[posicao + 2*n] = 'x'
    else:
        lista[posicao + n] = 'x'
    return lista

def movimento_torre(n, coluna, linha):
    lista = criar_lista(n)
    posicao = (linha - 1) * n + coluna
    for i in range(1, n + 1):
        lista[(linha - 1) * n + i] = 'x'       # monta a coluna
    for i in range(1, n + 1):
        lista[(i - 1) * n + coluna] = 'x'       # monta a linha
    lista[posicao] = 'o'
    return lista

def movimento_bispo(n, coluna, linha):
    lista = criar_lista(n)
    posicao = (linha - 1) * n + coluna
    i = 1 - linha
    for j in range(1, n + 1):            # monta a diagonal crescente
        if 0 < (coluna - i) <= n:           # checa se a posicao existe no tabuleiro
           lista[(j - 1) * n + (coluna - i)] = 'x'
        i += 1
    k = 1 - linha
    for j in range(1, n + 1):                # monta a diagonal decrescente
        if 0 < (coluna + k) <= n:
           lista[(j - 1) * n + (coluna + k)] = 'x'
        k += 1
    lista[posicao] = 'o'
    return lista

def movimento_dama(n, coluna, linha):
    lista = movimento_bispo(n, coluna, linha)
    posicao = (linha - 1) * n + coluna          # junta os movimentos do bispo e torre
    for i in range(1, n + 1):
        lista[(linha - 1) * n + i] = 'x'
    for i in range(1, n + 1):
        lista[(i - 1) * n + coluna] = 'x'
    lista[posicao] = 'o'
    return lista

def movimento_cavalo(n, coluna, linha):
    lista = criar_lista(n)
    posicao = (linha - 1) * n + coluna
    if 0 <= linha + 1 < n and 0 < coluna + 1 <= n:          # testa casa por casa que o cavalo ataca
        lista[(linha + 1) * n + coluna + 1] = 'x'
    if 0 <= linha + 1 < n and 0 < coluna - 1 <= n:
        lista[(linha + 1) * n + coluna - 1] = 'x'
    if 0 <= linha - 3 < n and 0 < coluna - 1 <= n:
        lista[(linha - 3) * n + coluna - 1] = 'x'
    if 0 <= linha - 3 < n and 0 < coluna + 1 <= n:
        lista[(linha - 3) * n + coluna + 1] = 'x'
    if 0 <= linha < n and 0 < coluna + 2 <= n:
        lista[(linha) * n + coluna + 2] = 'x'
    if 0 <= linha < n and 0 < coluna - 2 <= n:
        lista[(linha) * n + coluna - 2] = 'x'
    if 0 <= linha - 2 < n and 0 < coluna + 2 <= n:
        lista[(linha - 2) * n + coluna + 2] = 'x'
    if 0 <= linha - 2 < n and 0 < coluna - 2 <= n:
        lista[(linha - 2) * n + coluna - 2] = 'x'
    lista[posicao] = 'o'
    return lista

def movimento_rei(n, coluna, linha):
    lista = criar_lista(n)
    posicao = (linha - 1) * n + coluna
    for i in range(- 1, 2):                               # testa cada casa que o rei ataca
        if 0 < coluna - i <= n and 0 <= linha - 1:
            lista[(linha - 1) * n + coluna - i] = 'x'
    for i in range(- 1, 2):
        if 0 < coluna - i <= n and 0 <= linha - 2:
            lista[(linha - 2) * n + coluna - i] = 'x'
    for i in range(- 1, 2):
        if 0 < coluna - i <= n and 0 <= linha < n:
            lista[(linha) * n + coluna - i] = 'x'
    lista[posicao] = 'o'
    return lista

def imprimir_tabuleiro(peca, n, lista, letra, numero):
    numero = str(numero)
    print('Movimentos para a peca', peca, 'a partir da casa', letra+numero+'.')
    print(n, end=' ')
    k = n
    for i in range(n*n, 0, -1):             # cria o tabuleiro a partir das ordenadas da lista
        if i % n == 0 and i < n*n:
            k -= 1
            if k == 0:
                break
            print()
            print(k, end=' ')
        print(lista[i], end=' ')
    print()
    print('  ', end='')
    for i in range(n):
        print(chr(ord('a')+i), end=' ')

# juntando todas as funcoes
def montar_jogo(n, peca, letra, numero):
    coluna = (n+1) - (ord(letra) - 96)
    linha = numero
    if peca == 'Peao':
        lista = movimento_peao(n, coluna, linha)
    elif peca == 'Torre':
        lista = movimento_torre(n, coluna, linha)
    elif peca == 'Bispo':
        lista = movimento_bispo(n, coluna, linha)
    elif peca == 'Dama':
        lista = movimento_dama(n, coluna, linha)
    elif peca == 'Cavalo':
        lista = movimento_cavalo(n, coluna, linha)
    else:
        lista = movimento_rei(n, coluna, linha)
    imprimir_tabuleiro(peca, n, lista, letra, numero)

# entrada
while True:
    n = int(input())
    if n == 0:
        break
    dados = input().split(' ')
    montar_jogo(n, str(dados[0]), str(dados[1]), int(dados[2]))
    print()
    print()
