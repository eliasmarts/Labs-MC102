# commandos de comparacao
def soma(a,b):
    return a + b

def subtr(a,b):
    return a - b

def igual(a,b):
    return a == b

def diferente(a,b):
    return a != b

def menor(a,b):
    return a < b

def menorigual(a,b):
    return a <= b

def maior(a,b):
    return a > b

def maiorigual(a,b):
    return a >= b

def ande(a,b):
    return a and b

def orrr(a,b):
    return a or b

# dicionarios que guardam os comandos possiveis
comandos = {'+': soma, '-': subtr} 
comparacoes = {'==': igual, '!=': diferente, '<': menor, 
    '<=': menorigual, '>': maior, '>=': maiorigual}
logicas = {'OR': orrr, 'AND': ande}

# dicionario que guarda as variaveis
variaveis = {}

def resultante(lista, variaveis):
    """Retorna o resultado de uma expressão

    Analisa as posicoes impares, vendo o tipo de comando
    na ordem de operações lógicas, comparacões, e contas.
    Quando detecta um comando lógico ou comparação, divide
    a expressão em duas e aplica a função sobre cada uma
    """
    for j in range(0, len(lista)+1, 2):  # teste se as variaveis existem
        if lista[j][0].isalpha() and lista[j] not in variaveis:
            print(f'Erro de referencia: a variavel {lista[j]} nao foi definida.')
            return None
    
    for k in range(len(lista) - 2, 0, -2):
        if lista[k] in logicas:
            esquerda = resultante(lista[:k], variaveis)
            direita = resultante(lista[k+1:], variaveis)
            return logicas[lista[k]](esquerda, direita)
    
    for i in range (1, len(lista), 2):
        if lista[i] in comparacoes:
            esquerda = resultante(lista[:i], variaveis)
            direita = resultante(lista[i+1:], variaveis)
            return comparacoes[lista[i]](esquerda, direita)
    
    if lista[0][0].isalpha():
        resultado = variaveis[lista[0]]
    else:
        resultado = int(lista[0])
    
    operador = 1
    while operador <= len(lista)-1:
        if lista[operador + 1][0].isalpha():
            resultado = comandos[lista[operador]](resultado, variaveis[lista[operador + 1]])
        else:
            resultado = comandos[lista[operador]](resultado, int(lista[operador + 1])) 
        operador += 2
    return resultado

def processar(linha, variaveis):
    """Detecta o processo pedido no terminal e da a resposta

    se so há um valor, é para printar a variavel, se há um sinal
    de igual, é uma aribuição, e se não é uma expressao a ser calculada
    """
    variaveis = variaveis
    if len(linha) == 1:
        if linha[0][0].isalpha():  # teste pra ver se é um nome de variavel
            try:
                resposta = variaveis[linha[0]]
                if resposta == True:
                    print(1)
                elif resposta == False:
                    print(0)
                else:
                    print(resposta)
            except KeyError:
                print(f'Erro de referencia: a variavel {linha[0]} nao foi definida.')
        else:
            print(linha[0])
    elif linha[1] == '=':   # teste pra ver se é uma atribuição
        if linha[0][0].isalpha() and linha[0].isalnum():
            variaveis[linha[0]] = resultante(linha[2:], variaveis)
        else:
            print(f'Erro de sintaxe: {linha[0]} nao e um nome permitido para uma variavel.')
    elif True:     # como só pode ser uma expressao, calcula o resultado dela
        resposta = resultante(linha, variaveis)
        if resposta != None:
            if resposta == True:
                print(1)
            elif resposta == False:
                print(0)
            else:
                print(resposta)
    return variaveis

# entrada
while True:
    try:
        linha = input().split(' ')
    except EOFError:
        print("Encerrando... Bye-bye.")
        break
    # processa a linha e atualiza o dicionario das variaveis
    variaveis = processar(linha, variaveis)