# Desafio aceito uwu
while True:
    N = int(input())
    if N == 0:
        break
    l2 = input().split(' ')    # Entrada
    linha = int(l2[2])
    coluna = int(ord(l2[1]) - 96)  # Converte de letra pra numero
    print(f'Movimentos para a peca {l2[0]} a partir da casa {l2[1]}{l2[2]}.')
    for i in range(N, 0, -1):  # i conta a linha
        print(i, end=' ')
        for k in range(1, N + 1):               # k conta a coluna
            ataque = False          # guarda a informaçao se a casa esta atacada
            if i == linha and k == coluna:      # posicao da peca
                print('o', end=' '); ataque = True
            elif l2[0] == 'Peao':   # Testa qual é o tipo da peca e verifica a casa
                if i == linha + 1 or (linha == 2 and i == linha + 2):
                    if k == coluna:
                        print('x', end=' '); ataque = True
            elif l2[0] == 'Torre':
                    if i == linha or k == coluna:       # linha ou coluna atacada
                        print('x', end=' '); ataque = True
            elif l2[0] == 'Bispo':
                if i + k == linha + coluna or i - k == linha - coluna: # diagonais
                    print('x', end=' '); ataque = True
            elif l2[0] == 'Dama':
                if i + k == linha + coluna or i - k == linha - coluna: # diagonais
                    print('x', end=' '); ataque = True
                elif i == linha or k == coluna:           # linha ou coluna atacada
                    print('x', end=' '); ataque = True
            elif l2[0] == 'Cavalo':  # se n passar nesse teste, a peca obrigatoriamente é um rei
                if i == linha + 2 and (k == coluna - 1 or k == coluna + 1):
                    print('x', end=' '); ataque = True
                elif i == linha + 1 and (k == coluna - 2 or k == coluna + 2):
                    print('x', end=' '); ataque = True
                elif i == linha - 2 and (k == coluna - 1 or k == coluna + 1):
                    print('x', end=' '); ataque = True
                elif i == linha - 1 and (k == coluna - 2 or k == coluna + 2):
                    print('x', end=' '); ataque = True    
            elif i == linha or i == linha + 1 or i == linha - 1:  # linhas onde pode ter ataque
                    if k == coluna or k == coluna - 1 or k == coluna + 1: # colunas
                        print('x', end=' '); ataque = True
            if not ataque:
                print('-', end=' ')  
        print()             # desce a linha
    print(' ', end = ' ')
    for o in range(N):      # letras do tabuleiro
        print(chr(ord('a')+o), end=' ')
    print()         # pula uma linha para gerar o proximo tabuleiro
    print()
