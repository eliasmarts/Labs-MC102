def menor(lista):
    """Ve o menor valor comparando o segundo elemento das listas de 2 elementos
    e retorna o primeiro elemento do menor
    """
    indice = 0
    valor = lista[0][1]
    for k in range(len(lista)):
        aux = lista[k][1]
        if aux < valor:
            valor = aux
            indice = k
    return lista[indice][0]

def distancia(p1, p2):
    """Retorna a distancia euclidiana ao quadrado de dois pontos
    """
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def maisdistante(esconderijos, ymuralha):
    """Calcula o esconderijo mais distante de um ponto (0, y)
    """
    distanciamaior = 0
    indice = 0
    for i in range(len(esconderijos)):
        dist = distancia(esconderijos[i], (0, ymuralha))
        if dist > distanciamaior:
            distanciamaior = dist
            indice = i
    return indice

def criarintervalos(esconderijos, y):
    """Cria intervalos de valores de y para o qual o esconderijo mais longe
    é o mesmo

    Retorna uma lista de tuplas, sendo 
    (comeco do intervalo, fim do intervalo, esconderijo)
    """
    intervalos = []
    comeco = 1
    while comeco < y:
        distantec = maisdistante(esconderijos, comeco)
        # busca binaria para achar o fim do intervalo
        e = comeco
        d = y - 1
        while True:
            m = (e + d) // 2
            distantem = maisdistante(esconderijos, m)
            # verifica se os esconderijos mais distantes sao iguais:
            if distantec == distantem:
                if distantec != maisdistante(esconderijos, m + 1) or e == d: 
                    intervalos.append((comeco, m, distantec))
                    comeco = m + 1  # para comecar outro intervalo
                    break
                else:
                    e = m + 1
            else:
                d = m - 1
    return intervalos

def calculardistancias(esconderijos, intervalos):
    """Calcula a menor distancia de um intervalo ao esconderijo
    """
    distancias = []
    for i in intervalos:
        ponto = esconderijos[i[2]]
        if ponto[1] < i[0]:
            distancias.append([i[0], distancia(ponto, (0, i[0]))])
        elif ponto[1] > i[1]:
            distancias.append([i[1], distancia(ponto, (0, i[1]))])
        else:
            distancias.append([ponto[1], ponto[0]])
    return distancias


def main():
    # Entrada
    while True:
        n, y = [int(x) for x in input().split(' ')]
        if n == 0 and y == 0:
            break
        esconderijos = []
        for i in range(n):
            esconderijos.append(tuple([int(a) for a in input().split(' ')]))
        inter = criarintervalos(esconderijos, y)
        dist = calculardistancias(esconderijos, inter)
        print(menor(dist))

if __name__ == '__main__':
    main()