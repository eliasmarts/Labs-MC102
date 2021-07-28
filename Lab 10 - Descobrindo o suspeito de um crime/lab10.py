def imprimir(pessoas):
    """Imprime uma lista de suspeitos
    """
    if len(pessoas) == 0:
        print('Nenhum suspeito(a) com essas caracteristicas foi identificado(a).')
    elif len(pessoas) == 1:
        print('Suspeito(a):')
        print(pessoas[0])
    else:
        pessoas = sorted(pessoas)
        print('Suspeitos(as):')
        for i in pessoas:
            print(i)

# dicionarios que guardam as informacoes
suspeitos = {}
evidencias = {}

# entrada dos dados das pessoas
continua = True
while continua:
    linha = input().split(': ')
    nome = linha[1]
    caracteristicas = {}
    while True:
        l = input().split(': ')
        if l[0] == '-':
            break
        elif l[0] == '--':
            continua = False
            break     
        caracteristicas[l[0]] = l[1]
    nome = linha[1]
    suspeitos[nome] = caracteristicas

# entrada das evidencias
while True:
    linha2 = input().split(': ')
    if linha2[0] == '---':
        break
    evidencias[linha2[0]] = linha2[1]

# dicionario que associa a pessoa a quantas evidencias ela tem
comum = {}
for pessoa in suspeitos.keys():
    comum[pessoa] = 0

# compara as caracteristicas de cada pessoa com as evidencias
for caracteristica, tipo in evidencias.items():
    for suspeito, dicio in suspeitos.items():
        if caracteristica in dicio.keys():
            if tipo == dicio[caracteristica]:
                comum[suspeito] += 1

# cria uma lista de quem foi confimado a suspeita, caso ela tenha TODAS
# as caracteristicas das evidencias
confirmados = []
for pessoa in comum:
    if comum[pessoa] == len(evidencias):
        confirmados.append(pessoa)

# saida
imprimir(confirmados)