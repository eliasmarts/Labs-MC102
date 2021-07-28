def separa_numero(n):
    """separa um dado numero n em uma lista com seus algarismos"""
    n = str(n)
    lista_n = []
    for i in range(len(n)):
        lista_n.append(int(n[i]))
    return lista_n

def teste_semelhanca(entrada, senha):
    """testa quantos dígitos em comum tem a entrada com a senha correta"""
    semelhanca = 0
    for i in range(len(entrada)):           # testa dígito por dígito
        if entrada[i] == senha[i]:
            semelhanca += 1
    return semelhanca

def teste_senha(entrada, senha, i):
    """testa a senha digitada, imprime a mensagem e retorna 
    True se a senha estiver correta"""
    restante = i - 1
    if len(entrada) != len(senha):              # testa se tem a mesma quantidade de digitos
        print('Senha incorreta')
        print('Semelhanca: Erro: quantidade de digitos incongruente')
        print('Tentativas restantes:', restante)
        return False
    sem = teste_semelhanca(entrada, senha)
    if sem != len(senha):                     # testa se são diferentes
        print('Senha incorreta')
        print('Semelhanca:', sem)
        print('Tentativas restantes:',  restante)
        return False
    else:
        print('Senha reconhecida. Desativando defesas...')
        return True

# Entrada
linha1 = input().split(' ')
senha = separa_numero(linha1[0])
n = int(linha1[1])

# Usa as funcoes para testar as n entradas de senha
for i in range(n, 0, -1):
    entrada = separa_numero(input())
    resultado = teste_senha(entrada, senha, i)
    if resultado:
        break
    else:
        print()
    if i - 1 == 0:
        print('Tentativas esgotadas. Acionando defesas...')
