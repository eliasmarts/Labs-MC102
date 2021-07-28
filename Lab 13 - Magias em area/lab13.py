from math import log

def criar_campo(m, n):
    """Cria uma campo(matriz) m x n para jogar as magias

    - indica que as casas ainda nao foram atacadas por uma magia
    """
    campo = []
    for i in range(m):
        campo.append(['-' for j in range(n)])
    return campo


def aplicar_magia(campo, i, j, lado):
    """Aplica uma submagia no campo, marcando as casas atacadas com x
    
    A posicao do canto superior esquerdo da magia é dada por (i, j)
    e o lado é o tamanho do quadrado da magia
    """
    for k in range(lado):
        for m in range(lado):
            campo[i+k][j+m] = 'x'
    return campo


def preencher_campo_rec(campo, nivel, magias):
    """Preenche o campo com o minimo de magias possiveis
    
    Começa usando a magia de nivel mais alto sempre que possível
    e vai diminuindo os níveis. Retorna um dicionario com as magias
    utilizadas
    """
    base = len(campo)
    altura = len(campo[0])
    if nivel == 0:
        for i in range(base):
            for j in range(altura):
                if campo[i][j] == '-':
                    aplicar_magia(campo, i, j, 1)
                    magias[0] += 1
        return magias
    else:
        # aplica todas as magias possiveis de um nivel, e usa recursao
        # para aplicar as de nivel menor
        lado = 2 ** nivel
        for i in range(base):
            for j in range(altura):
                # checa se a area da magia nao esta atacada
                if campo[i][j] == '-':
                    if (0 < i+lado-1 <= base-1 and 0 < j+lado-1 <= altura-1
                    and campo[i+lado-1][j+lado-1] == '-'):
                        aplicar_magia(campo, i, j, lado)
                        magias[nivel] += 1
        return preencher_campo_rec(campo, nivel - 1, magias)


def preencher_campo(campo, m, n):
    """Calcula qual o maior nível de magia que pode ser utilizada no campo
    e usa a funcao recursiva para preencher o campo
    """
    t = min([m, n])
    nivelmax = int(log(t, 2))
    # dicionario que guardara quantas magias de cada nivel foram utilizadas
    magias = {}
    for k in range(nivelmax + 1):
        magias[k] = 0
    return preencher_campo_rec(campo, nivelmax, magias)


def calcular_PM(magias):
    """Calcula o PM gasto usando as magias
    """
    custo = 0
    for nivel, quantidade in magias.items():
        custo += (2 ** nivel) * quantidade
    return custo

def calcular_soma(magias):
    """Calcula a quantidade total de magias utilizadas
    """
    soma = 0
    for quantidade in magias.values():
        soma += quantidade
    return soma


def imprimir_resposta(magias):
    """Imprime a saida usando o dicionario com as magias usadas
    """
    print('---')
    print("Grimorio de Teraf L'are")
    print('---')
    for nivel, quantidade in magias.items():
        if quantidade != 0:
            print(f'{quantidade} submagia(s) de nivel {nivel}')
    print('---')
    print('Total de submagia(s) conjurada(s):', calcular_soma(magias))
    print('Total de PM gasto:', calcular_PM(magias))
    print('---')


def main():
    # Entrada
    m, n = [int(x) for x in input().split(' ')]
    campo = criar_campo(m, n)
    magias_lancadas = preencher_campo(campo, m, n)
    imprimir_resposta(magias_lancadas)

if __name__ == '__main__':
    main()
