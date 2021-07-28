from math import log
from sys import setrecursionlimit
setrecursionlimit(2000)


class Retangulo:
    """Define um retangulo com sua base e altura
    """
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura


    def dividir(self, lado_de_quadrado: int):
        """Remove um quadrado do retangulo
        
        Remove um quadrado de lado l na esquerda, divide o pedaço restante
        em dois retangulos menores e retorna esses dois retangulos.
        r1 é o retangulo que sobra a direita e r2 o que sobra abaixo.
        """
        r1 = Retangulo(self.base - lado_de_quadrado, lado_de_quadrado)
        r2 = Retangulo(self.base, self.altura - lado_de_quadrado)
        return r1, r2



def preencher_campo_rec(campo: Retangulo, magias_utilizadas: dict) -> dict:
    """Preenche o campo com o menor número de magias utilizando recursao
    
    Calcula qual o maior nivel de magia que pode ser aplicada no campo,
    entao a utiliza no campo. A parte que sobra sem ser atacada e dividida
    em dois retangulos menores, e a funcao e chamada recursivamente nelas.
    Retorna um dicionario com as magias utilizadas.
    """
    
    if campo.base == 0 or campo.altura == 0:
        # caso trivial, onde a divisao chegou em um retangulo nulo
        return magias_utilizadas
    else:
        menor_lado = min(campo.base, campo.altura)
        maior_magia_possivel = int(log(menor_lado, 2))
        magias_utilizadas[maior_magia_possivel] += 1
        
        # usa a maior magia no campo, divide o pedaco restante em
        # dois retangulos e preenche eles
        ret1, ret2 = campo.dividir(2 ** maior_magia_possivel)
        preencher_campo_rec(ret1, magias_utilizadas)
        preencher_campo_rec(ret2, magias_utilizadas)
        
        return magias_utilizadas


def preencher_campo(campo: Retangulo) -> dict:
    """Cria o dicionario que armazena a quantidade de magias
    e chama a funcao recursiva
    """
    menor_lado = min(campo.base, campo.altura)
    maior_magia = int(log(menor_lado, 2))
    
    magias_utilizadas = {}
    for k in range(maior_magia + 1):
        magias_utilizadas[k] = 0

    return preencher_campo_rec(campo, magias_utilizadas)


def calcular_PM(magias: dict) -> int:
    """Calcula o PM gasto usando as magias
    """
    custo = 0
    for nivel, quantidade in magias.items():
        custo += (2 ** nivel) * quantidade
    return custo


def calcular_soma(magias: dict) -> int:
    """Calcula a quantidade total de magias utilizadas
    """
    soma = 0
    for quantidade in magias.values():
        soma += quantidade
    return soma


def imprimir_resposta(magias: dict):
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
    campo_inicial = Retangulo(m, n)
    magias = preencher_campo(campo_inicial)
    imprimir_resposta(magias)

if __name__ == '__main__':
    main()
