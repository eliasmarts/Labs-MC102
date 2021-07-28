def converte_hexa(mensagem, enxerto):
    """Codifica uma mensagem em hexadecimal
    """
    msg_separada = []
    for i in range(len(mensagem)):  # separa a mensagem em uma lista com seus caactere
        msg_separada.append(mensagem[i])
    codigo = ''
    for k in range(len(msg_separada)):
        msg_separada[k] = hex(ord(msg_separada[k])) # converte os valor ASCII para hexadecimal
        msg_separada[k] = msg_separada[k][2:len(msg_separada[k])+1] # tira o indicador
        letra = str(msg_separada[k])
        letra = letra.zfill(enxerto)  # preenche o enxerto com 0
        letra2 = ''
        for j in range(len(letra)):
            if  96 < ord(letra[j]) < 103:  # testa se a lera esta entre a e f
                letra2 += letra[j].upper()   # muda a letra pra maiuscula
            else:
                letra2 += letra[j]
        codigo += letra2
    return codigo

def converte_octa(mensagem, enxerto):
    """Codifica uma mensagem em octadecimal
    """
    msg_separada = []
    for i in range(len(mensagem)):
        msg_separada.append(mensagem[i])
    codigo = ''
    for k in range(len(msg_separada)):
        msg_separada[k] = oct(ord(msg_separada[k]))  # converte os valor ASCII para octal  
        msg_separada[k] = msg_separada[k][2:len(msg_separada[k])+1] # tira o indicador
        letra = str(msg_separada[k])
        letra = letra.zfill(enxerto)  # preenche o enxerto com 0
        codigo += letra
    return codigo

def desconverte_hexa(mensagem, enxerto):
    """Decodifica uma mensagem em hexadecimal
    """
    msg_separada = []
    for i in range(0, len(mensagem), enxerto):
        msg_separada.append(mensagem[i:i+enxerto])
    msg_decodificada = ''
    for k in range(len(msg_separada)):    
        msg_separada[k] = msg_separada[k].lstrip('0')  # tira o enxerto 
        msg_decodificada += chr(int(msg_separada[k], 16))
    return msg_decodificada

def desconverte_octa(mensagem, enxerto):
    """Descodifica uma mensagem em octadecimal
    """
    msg_separada = []
    for i in range(0, len(mensagem), enxerto):  # separa numa lista
        msg_separada.append(mensagem[i:i+enxerto])
    msg_decodificada = ''
    for k in range(len(msg_separada)):    
        msg_separada[k] = msg_separada[k].lstrip('0')  # tira o enxerto 
        msg_decodificada += chr(int(msg_separada[k], 8))
    msg_decodificada = msg_decodificada[::-1]  # inverte a mensagem
    return msg_decodificada

def codifica(mensagem, enxerto):
    """Codifica uma mensagem de varias linhas

    As linhas impar sao convertidas em hexadecimal
    e as linhas pares sao invertidas e convertidas em octadecimal
    """
    msg_codificada = []
    for i in range(len(mensagem)):
        if (i + 1) % 2 == 1:
            msg_codificada.append(converte_hexa(mensagem[i], enxerto))
        else:
            msg_codificada.append(converte_octa(mensagem[i][::-1], enxerto))
    for linha in range(len(msg_codificada)):
        print(msg_codificada[linha])

def decodifica(mensagem, enxerto):
    """decodifica uma mensagem de varias linhas
    """
    msg_decodificada = []
    for i in range(len(mensagem)):
        if (i + 1) % 2 == 1:
            msg_decodificada.append(desconverte_hexa(mensagem[i], enxerto))
        else:
            msg_decodificada.append(desconverte_octa(mensagem[i], enxerto))
    for linha in range(len(msg_decodificada)):
        print(msg_decodificada[linha])

# Entrada
linha1 = [int(x) for x in input().split(' ')]
modo = linha1[0]
enxerto = linha1[1]
nlinhas = linha1[2]
mensagem_completa = []
for i in range(nlinhas):
    mensagem_completa.append(input())
if modo == 1:
    codifica(mensagem_completa, enxerto)
else:
    decodifica(mensagem_completa, enxerto)
