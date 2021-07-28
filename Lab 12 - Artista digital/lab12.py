def criar_tela(m, n):
    """Cria uma tela(matriz) m x n para ser pintada
    """
    tela = []
    for i in range(m):
        tela.append(['-' for j in range(n)])
    return tela


def imprimir_tela(tela):
    """Imprime uma tela(matriz)
    """
    for i in range(len(tela)):
        print(' '.join(tela[i]))


def distancia(p1, p2):
    """Retorna a distancia euclidiana ao quadrado de dois pontos
    """
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def pintar_quadrado(tela, i, j, l):
    """Pinta um quadrado usando recursao por camadas
    
    cada chamada pinta o contorno do quadrado

    Exemplo:
    - - - - -         - - - - -         - - - - -
    - - - - -         - x x x -         - x x x -
    - - - - -   -->   - x - x -   -->   - x x x -
    - - - - -         - x x x -         - x x x -
    - - - - -         - - - - -         - - - - -
    """
    linhas = len(tela)
    colunas = len(tela[0])
    
    if l == 1:  # centro
        if 0 <= i < linhas and 0 <= j < colunas:  # dentro da tela
            tela[i][j] = 'x'
        return tela
    else:
        # pinta o contorno e diminui o quadrado
        m = l // 2
        for o in range(-m, m+1, 2*m):
            for p in range(-m, m+1):
                if 0 <= i+o < linhas and 0 <= j+p < colunas:
                    tela[i+o][j+p] = 'x'

        for q in range(-m + 1, m):
            for r in range(-m, m+1, 2*m):
                if 0 <= i+q < linhas and 0 <= j+r < colunas:
                    tela[i+q][j+r] = 'x'

        return pintar_quadrado(tela, i, j, l - 2)


def pintar_circulorec(tela, i, j, r, m):
    """Pinta um circulo usando recursao por camadas

    Usa como se fosse pintar um quadrado de lado 2r + 1,
    mas verifica se o ponto faz parte do circulo

    Exemplo:
    - - - - -         - - - - -         - - - - -
    - - - - -         - - x - -         - - x - -
    - - - - -   -->   - x - x -   -->   - x x x -
    - - - - -         - - x - -         - - x - -
    - - - - -         - - - - -         - - - - -
    """
    linhas = len(tela)
    colunas = len(tela[0])
    
    if m == 1:   # centro
        try:
            tela[i][j] = 'x'
        except IndexError:
            pass
        return tela
    else:
        # pinta a camada mais extrena do circulo
        n = m // 2
        for o in range(-n, n+1, 2*n):
            for p in range(-n, n+1):
                if 0 <= i+o < linhas and 0 <= j+p < colunas:
                    if distancia((i+o,j+p), (i, j)) <= r ** 2:
                        tela[i+o][j+p] = 'x'
  
        for q in range(-n + 1, n):
            for s in range(-n, n+1, 2*n):
                if 0 <= i+q < linhas and 0 <= j+s < colunas:    
                    if distancia((i+q,j+s), (i, j)) <= r ** 2:
                        tela[i+q][j+s] = 'x'

        return pintar_circulorec(tela, i, j, r, m - 2)


def pintar_circulo(tela, i, j, r):
    return pintar_circulorec(tela, i, j, r, 2 * r + 1)


def main():
    # Entrada
    m, n = [int(x) for x in input().split(' ')]
    q = int(input())
    pintura = criar_tela(m, n)

    for h in range(q):
        forma, i, j, r = input().split(' ')
        i, j, r = int(i), int(j), int(r)
        if forma == 'quadrado':
            pintura = pintar_quadrado(pintura, i, j, r)
        else:
            pintura = pintar_circulo(pintura, i, j, r)

    imprimir_tela(pintura)


if __name__ == '__main__':
    main()
