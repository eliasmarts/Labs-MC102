def lermatriz(n):
    """Faz a leitura de uma matriz quadrada n x n
    """
    matriz = []
    for i in range(n):
        matriz.append([int(x) for x in input().split(' ')])
    return matriz

def comum(matriz1, matriz2, a, b):
    """Retorna o tamanho da matriz p x q, intersecao de duas matrizes

    A matriz 1 é a menor, e a matriz 2 a maior. o código procura as quinas de 1
    em 2, e, ao achar uma quina de 1 em 2, sabe o tamanho da intersecao
    """
    p = 0
    q = 0
    continua = True
    for k in range(b):
        if not continua:
            break
        for j in range(b):
            if matriz1[0][0] == matriz2[k][j]:
                if b - k <= a:
                    p = b - k
                else:
                    p = a
                if b - j <= a:
                    q = b - j
                else:
                    q = a
                continua = False
                break
            elif matriz1[a-1][0] == matriz2[k][j]:
                p = k + 1
                if b - j <= a:
                    q = b - j
                else:
                    q = a
                continua = False
                break
            elif matriz1[0][a-1] == matriz2[k][j]:
                if b - k <= a:
                    p = b - k
                else:
                    p = a
                q = j + 1
                continua = False
                break
            elif matriz1[a-1][a-1] == matriz2[k][j]:
                p = k + 1
                q = j + 1
                continua = False
                break
    return p, q

while True:
    # Entrada
    dimensao = [int(x) for x in input().split(' ')]
    if dimensao[0] == 0:
        break
    m = dimensao[0]
    n = dimensao[1]
    
    matrizM = lermatriz(m)
    matrizN = lermatriz(n)
    
    # ve qual é maior
    if m < n:
        interp, interq = comum(matrizM, matrizN, m, n)
    else:
        interp, interq = comum(matrizN, matrizM, n, m)
    
    # interp e interq é o tamanho da matriz de intersecao
    # calcula o tamanho da supermatriz
    superp = m + n - interp
    superq = m + n - interq
    print(f'{superp} x {superq}')
