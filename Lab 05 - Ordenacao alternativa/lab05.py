def ordem_segunda(texto):
    """Retorna a key de segunda

    conta o número de letras minúsculas na string"""
    valor = 0
    for i in range(len(texto)):
       if texto[i].islower():
           valor += 1
    return valor

def ordem_terca(texto):
    """Retorna a key de terça

    conta o número de letras maiúsculas na string"""
    valor = 0
    for i in range(len(texto)):
       if texto[i].isupper():
           valor += 1
    return valor

def ordem_quarta(texto):
    """Retorna a key de quarta

    conta o número de letras do alfabeto na string"""
    valor = 0
    for i in range(len(texto)):
       if texto[i].isalpha():
           valor += 1
    return valor

def ordem_quinta(texto):
    """Retorna a key de quinta

    conta o número de palavras, com base na quantidade de espaços"""
    valor = 1
    for i in range(1, len(texto) - 1):
       if texto[i] == ' ':
           valor += 1
    return valor

def ordem_sexta(texto):
    """Retorna a key de quinta

    soma os valores ASCII de cada caractere da string"""
    valor = 0
    for i in range(len(texto)):
       valor += ord(texto[i])
    return valor

def ordenar(lista, dia):
    """Ordena a lista com base no dia"""
    if dia == 'Segunda':
        lista_ordenada = sorted(lista, key=ordem_segunda)
    elif dia == 'Terca':
        lista_ordenada = sorted(lista, key=ordem_terca, reverse=True)
    elif dia == 'Quarta':
        lista_ordenada = sorted(lista, key=ordem_quarta)
    elif dia == 'Quinta':
        lista_ordenada = sorted(lista, key=ordem_quinta)
    elif dia == 'Sexta':
        lista_ordenada = sorted(lista, key=ordem_sexta, reverse=True)
    return lista_ordenada

# Entrada
linha1 = input().split(' ')
dia = linha1[0]
entradas = int(linha1[1])
enderecos = []
for i in range(entradas):
    enderecos.append(input())
ende_ordem = ordenar(enderecos, dia)
for q in ende_ordem:
    print(q)
