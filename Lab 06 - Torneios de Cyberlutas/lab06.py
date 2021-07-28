class Medabot:
  """Representa um medabot montado.

  Recebe 5 peças, um torso, um braço esquerdo, um braço direito e uma medalha
  e calcula os valores de ataque e defesa.
  """
  def __init__(self, torso, bdireito, besquerdo, pernas, medalha):
    self.torso = torso
    self.bdireito = bdireito
    self.besquerdo = besquerdo
    self.pernas = pernas
    self.medalha = medalha
    self.ataque = self.bdireito + self.besquerdo + self.medalha[0]
    self.defesa = self.torso + self.pernas + self.medalha[1]

class Medalutador:
    """Representa um medalutador

    Armazena o ID, sua habilidade, recuperação, e suas peças, 
    e usa as melhores peças para montar um medabot.
    """
    def __init__(self, ID, habilidade, recuperacao, medalha, pecas):
      self.ID = ID
      self.habilidade = habilidade
      self.recuperacao = recuperacao
      self.medalha = medalha
      self.pecas = pecas
      self.torsos = []
      self.besquerdos = []
      self.bdireitos = []
      self.pernas = []
      self.hab_max = habilidade
      self.tipopecaganha = ''
      self.pecaganha = 0

      for i in range(len(self.pecas)):    # separa as pecas em listas
        if self.pecas[i][0] == 'T':
          self.torsos.append(self.pecas[i][1])
        elif self.pecas[i][0] == 'E':
          self.besquerdos.append(self.pecas[i][1])
        elif self.pecas[i][0] == 'D':
          self.bdireitos.append(self.pecas[i][1])
        else:
          self.pernas.append(self.pecas[i][1])
      self.medabot = Medabot(max(self.torsos), max(self.bdireitos), max(self.besquerdos), max(self.pernas), self.medalha) #cria o medabot com as melhores pecas

    def receber_peca(self, tipo, peca):
      """Adiciona uma peça a um medalutador

      Coloca a peça na lista certa, armazena a informação da peça recebida, e remonta o medabot
      """
      if tipo == 'T':
        self.tipopecaganha = 'T'
        self.pecaganha = peca
        self.torsos.append(peca)
      elif tipo == 'E':
        self.tipopecaganha = 'E'
        self.pecaganha = peca
        self.besquerdos.append(peca)
      elif tipo == 'D':
        self.tipopecaganha = 'D'
        self.pecaganha = peca
        self.bdireitos.append(peca)
      else:
        self.tipopecaganha = 'P'
        self.pecaganha = peca
        self.pernas.append(peca)
      self.medabot = Medabot(max(self.torsos), max(self.bdireitos), max(self.besquerdos), max(self.pernas), self.medalha)

    def perder_peca(self, tipo, peca):
      """Remove uma peça de um medalutador

      Procura a peça na lista certa, a remove, e remonta o medabot
      """
      if tipo == 'T':
        for i in range(len(self.torsos)):
          if self.torsos[i] == peca:      # remove a peça
            del(self.torsos[i])
            break
      elif tipo == 'E':
        for i in range(len(self.besquerdos)):
          if self.besquerdos[i] == peca:
            del(self.besquerdos[i])
            break
      elif tipo == 'D':
        for i in range(len(self.bdireitos)):
          if self.bdireitos[i] == peca:
            del(self.bdireitos[i])
            break
      else:
        for i in range(len(self.pernas)):
          if self.pernas[i] == peca:
            del(self.pernas[i])
            break
      if not (self.torsos == [] or self.bdireitos == [] or self.besquerdos == [] or self.pernas == []):    # verifica se nenhuma das peças acabaram
        self.medabot = Medabot(max(self.torsos), max(self.bdireitos), max(self.besquerdos), max(self.pernas), self.medalha)


    def imprime(self):
      """Imprime as características do medalutador e seu medabot
      """
      print(f'\tA{self.ID} = E{str(self.medabot.besquerdo)} + D{self.medabot.bdireito} + {self.medabot.medalha[0]} = {self.medabot.ataque}')
      print(f'\tD{self.ID} = T{self.medabot.torso} + P{self.medabot.pernas} + {self.medabot.medalha[1]} = {self.medabot.defesa}')
      print(f'\tH{self.ID} = {self.habilidade}')

    def obter_ID(self):
      return self.ID

    def __repr__(self):
      return str(self.ID)

def imprimir_ficha_tecnica(i, j):
  i.imprime()
  j.imprime()

def troca_peca(p, q):
  """Realiza a troca e mudança de habilidade

  p é o vencedor, q o perdedor. Usa os valores pra dar uma peça de q para p,
  e modificar as habilidades.
  """
  compara = [q.medabot.torso - p.medabot.torso, q.medabot.besquerdo - p.medabot.besquerdo, 
  q.medabot.bdireito - p.medabot.bdireito, q.medabot.pernas - p.medabot.pernas]   # Lista com as diferenças
  max_value = max(compara)
  maior = compara.index(max_value)
  if maior == 0:
    p.receber_peca('T', q.medabot.torso)
    q.perder_peca('T', q.medabot.torso)
  elif maior == 1:
    p.receber_peca('E', q.medabot.besquerdo)
    q.perder_peca('E', q.medabot.besquerdo)
  elif maior == 2:
    p.receber_peca('D', q.medabot.bdireito)
    q.perder_peca('D', q.medabot.bdireito)
  else:
    p.receber_peca('P', q.medabot.pernas)
    q.perder_peca('P', q.medabot.pernas)

  if p.habilidade - q.habilidade > 0:        # Redução das habilidades
    p.habilidade = p.habilidade - q.habilidade
  else:
    p.habilidade = 0
  q.habilidade = q.habilidade // 2

  if p.habilidade + p.recuperacao < p.hab_max:        # Recuperação das habilidades
    p.habilidade = p.habilidade + p.recuperacao
  else:
    p.habilidade = p.hab_max
  
  if q.habilidade + q.recuperacao < q.hab_max:
    q.habilidade = q.habilidade + q.recuperacao
  else:
    q.habilidade = q.hab_max

def batalhar(i, j):
  """Retorna o vencedor de uma batalha com dois medalutadores
  """
  if (i.medabot.ataque > j.medabot.defesa or j.medabot.ataque > i.medabot.defesa) and i.medabot.ataque - j.medabot.defesa != j.medabot.ataque - i.medabot.defesa:
    if i.medabot.ataque - j.medabot.defesa > j.medabot.ataque - i.medabot.defesa:
      troca_peca(i, j)
      return i
    else:
      troca_peca(j, i)
      return j
  elif i.habilidade != j.habilidade:
    if i.habilidade > j.habilidade:
      troca_peca(i, j)
      return i
    else:
      troca_peca(j, i)
      return j
  else:
    if i.ID < j.ID:
      troca_peca(i, j)
      return i
    else:
      troca_peca(j, i)
      return j

def imprimir_resultado_da_batalha(k):
  print(f'Medalutador {k.ID} venceu e recebeu a {k.tipopecaganha}{k.pecaganha}\n')

def simular_torneios_de_cyberlutas(lista_de_medalutadores):
  lista_torneio_principal = []
  lista_de_repescagem     = []
  for medalutador in lista_de_medalutadores:
    lista_torneio_principal.append(medalutador)
  while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:
    lista_torneio_principal = aplicar_rodada_de_batalhas(lista_torneio_principal, lista_de_repescagem)
    lista_de_repescagem     = aplicar_rodada_de_batalhas(lista_de_repescagem, None)
  i = lista_torneio_principal.pop(0)
  j = lista_de_repescagem.pop(0)
  print('Cyberluta Final')
  print(f'Medalutadores: {i} vs {j}')
  imprimir_ficha_tecnica(i, j)
  k = batalhar(i, j)
  print(f'Campeao: medalutador {k}')

def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem):
  if len(lista_de_medalutadores) < 2:
    return lista_de_medalutadores
  lista_de_vencedores = []
  while len(lista_de_medalutadores) >= 2:
    i = lista_de_medalutadores.pop(0) 
    j = lista_de_medalutadores.pop(0)
    if i.obter_ID() > j.obter_ID():
      i, j = j, i
    if lista_de_repescagem != None:
      print('Cyberluta do Torneio Principal')
    else:
      print('Cyberluta da Repescagem')
    print(f'Medalutadores: {i} vs {j}')
    imprimir_ficha_tecnica(i, j)
    k = batalhar(i, j)
    imprimir_resultado_da_batalha(k)
    if lista_de_repescagem != None:
      if i == k:
        lista_de_repescagem.append(j)
      else:
        lista_de_repescagem.append(i)
    lista_de_vencedores.append(k)
  lista_de_vencedores.extend(lista_de_medalutadores)
  return lista_de_vencedores

# Entrada
lista_medalutadores = []
N = int(input())
for i in range(N):        # cria os medalutadores e os coloca na lista
  linha1 = [int(x) for x in input().split(' ')]
  medalha = [int(y) for y in input().split(' ')]
  pecas = []
  for k in range(linha1[2]):
    pecas.append(input().split(' '))
    pecas[k][1] = int(pecas[k][1])
  med = Medalutador(i + 1, linha1[0], linha1[1], medalha, pecas)
  lista_medalutadores.append(med)

simular_torneios_de_cyberlutas(lista_medalutadores)
