# Tarefa de Laboratório 06 - Classes
## Torneios de Cyberlutas

Medabots são robôs lutadores com uma excelente inteligência artificial garantida por meio de medalhas especiais. Cada medabot é composto por três partes: o tinpet, as medapeças e a medalha.

O tinpet é o esqueleto metálico que é a base de todos os medabots, onde será equipado as medapeças. A figura abaixo ilustra os modelos de tinpet masculino e feminino, respectivamente.

As medapeças são o revestimento do medabot, como sua pele e músculo. São chamadas de torso (reveste o tronco e a cabeça do medabot); braço esquerdo e braço direito (revestem o braço respectivo); e pernas (reveste as pernas e quadris do medabot).

As medalhas são um pequeno hexágono metálico dourado com uma joia e desenho no centro. Uma medalha é o ''cérebro'' de um medabot e lhe dá também a sua personalidade.

Um medabot recebe ordens do seu medalutador que o utiliza em batalha, um esporte de combate popular em que dois medabots se enfrentam. Em batalhas profissionais, conhecidas por cyberlutas, os medalutadores usam seus medabots para se qualificar para o Torneio Mundial e batalhar entre a elite para ganhar o título de campeão.

Em todas as cyberlutas oficiais, o medalutador que perdeu a batalha deve dar uma medapeça, entre as peças equipadas em seu medabot, para o vencedor. Com isso, conforme um medalutador for vencendo batalhas, ele pode criar as mais variadas combinações de braços, pernas e torso para tornar seu medabot cada vez mais poderoso.

## Tarefa
Ocorrerá um torneio de cyberlutas com  medalutadores, enumerados de  a , conforme a ordem de chegada. Ou seja, cada medalutador tem um número de registro. Como é de conhecimento geral as informações sobre cada medalutador e seu medabot (inclusive suas medapeças sobressalentes), a sua tarefa neste lab será escrever um programa que simulará este torneio de cyberlutas a fim de indicar o campeão. Esta simulação é muito útil para diversos apostadores.

As informações de conhecimento geral são as seguintes.

**Medalutador**

Cada medalutador tem a sua habilidade dada por H, que representa a média de atributos importantes em cyberlutas como estratégias, raciocínio, etc. O medalutador só pode participar com um único medabot durante todo o torneio, mas é permitido a troca de medapeças de seu medabot antes do início de cada cyberluta. Deste modo, os medalutadores carregam consigo várias medapeças sobressalentes (pelos menos dois pares de cada parte). A medapeça recebida dos medalutadores vencidos em batalha são sempre adicionadas ao seu conjunto de medapeças sobressalentes.

**Medabot, medapeças e medalha**

Cada medabot possui uma quantidade de pontos de ataque e defesa, resultante das somas pontos de suas medapeças equipadas. Já cada medapeça possui uma quantidade de pontos conforme a sua parte do tinpet, conforme descrito a seguir.

- O torso é uma medapeça que serve como escudo, pois é dedicada a defesa do medabot. Não é tão frágil como as outras, mas se quebra, o medabot para de funcionar, mesmo com as outras peças intactas. Seus pontos são adicionados como pontos de defesa.
- Os braços esquerdo e direito são medapeças mais eficientes no ataque. Seus pontos são adicionados como pontos de ataque.
- As pernas são medapeça dedicada para a agilidade, deste modo seus pontos são adicionados como pontos de defesa.

A medalha de um medabot concede um bônus de pontos de ataque e defesa. O resultado da soma dos pontos das medapeças mais os bônus da medalha resultam na ficha final de pontos de ataque e defesa de um medabot, onde A e D denotam respectivamente esses pontos.

Para vencer uma batalha, um medalutador sempre equipa seu medabot com as suas melhores medapeças (i.e., as com mais pontos).

O torneio será realizado no formato de dupla eliminação, o que significa que são necessárias duas derrotas para que um medalutador seja eliminado da competição. Ao ser derrotado pela primeira vez, o medalutador é enviado para a repescagem. As cyberlutas da repescagem são intercaladas com as cyberlutas do torneio principal, ou seja, após a primeira rodada de batalhas no torneio principal, a primeira rodada de batalhas da repescagem é realizada e assim por diante. O vencedor do torneio principal deve esperar que a repescagem termine para conhecer seu adversário na grande final.

A associação de medalutadores já tem o código da execução do torneio, mas precisa que você diga quem ganha cada batalha e que gerencie as medapeças e habilidades. Para isso, você deve fazer uso de classes em python como uma forma de organizar os dados e as funcionalidades.

O código em python a seguir é o código da execução do torneio disponibilizado pela associação de medalutadores.
```
class Medalutador:
    def __init__(self, ID, ...):
        self.ID = ID
        ...

    def obter_ID(self):
        return self.ID

    def __repr__(self):
        return str(self.ID)

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
```

E o código a seguir também é disponibilizado pela associação de medalutadores e simula cada rodada de batalhas, seja a rodada do torneio principal ou da repescagem.
```
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
```

Note que você precisará implementar as funções:

- batalhar
    - Parâmetros: Dois medalutadores i e j que irão batalhar entre si (será explicado mais adiante).
    - Retorno: O medalutador vencedor da batalha.

- imprimir_ficha_tecnica
    - Parâmetros: Dois medalutadores i e j.
    - Retorno: Sem retorno. Deve apenas imprimir a ficha técnica de cada medalutador, no seguinte formato:
```
print(f'\tA{ID} = E{pontos_do_braco_e} + D{pontos_do_braco_d} + {bonus_de_ataque} = {pontos_de_ataque}')
print(f'\tD{ID} = T{pontos_do_torso} + P{pontos_das_pernas} + {bonus_de_defesa} = {pontos_de_defesa}')
print(f'\tH{ID} = {habilidade_atual}')
```

- imprimir_resultado_da_batalha
    - Parâmetros: Um medalutador k vencedor de uma batalha.
    - Retorno: Sem retorno. Deve apenas imprimir uma mensagem indicando o vencedor e a sua medapeça ganha, no formato:
```
print(f'Medalutador {k} venceu e recebeu a {tipo_da_medapeca_ganha}{pontos_da_medapeca_ganha}\n')
```

Quando dois medalutadores i e j batalham, o vencedor é definido da seguinte maneira.

- Se (Ai > Dj ou Aj > Di) e Ai-Dj ≠ Aj-Di:
    - O medalutador vencedor da batalha é i se Ai-Dj > Aj-Di; o contrário é j.

- Senão, se Hi ≠ Hj (habilidade atual de cada medalutador):
    - O medalutador vencedor da batalha é i se Hi > Hj; o contrário é j.

- Senão:
    - O medalutador vencedor da batalha é i se i < j (comparação entre o número de registro); o contrário é j.
Por exemplo, considere o medabot do medalutador i esteja equipado com um torso de 20 pontos (T20), braço esquerdo de 18 pontos (E18), braço direito de 30 pontos (D30) e pernas de 15 pontos (P15); e que a sua medalha concede 7 pontos de ataque e 3 pontos de defesa. A sua ficha final de pontos é:
- Ai = E18 + D30 + 7 = 55 pontos; e
- Di = T20 + P15 + 3 = 38 pontos.

E considere também que o medabot do medalutador j esteja equipado com um torso de 35 pontos (T35), braço esquerdo de 25 pontos (E25), braço direito de 11 pontos (D11), e pernas de 20 pontos (P20); e que a sua medalha concede 5 pontos de ataque e 4 pontos de defesa. A sua ficha final de pontos é:
- Aj = E25 + D11 + 5 = 41 pontos; e
- Dj = T35 + P20 + 4 = 59 pontos.
Neste caso, medalutador j é o vencedor da batalha entre i e j.

O medalutador que perdeu a batalha dará uma de suas medapeças utilizadas em batalha ao vencedor. Como é de praxe, a medapeça dada é aquela que dará mais pontos de ataque ou defesa ao medabot que venceu a batalha, caso for utilizada por ele em outra batalha. Seguindo com o exemplo, temos que a diferença de pontos das medapeças dos medabots de j e i é:

- -15 pontos para o torso;
- -7 pontos para o braço esquerdo;
- 19 pontos para o braço direito; e
- -5 pontos para as pernas.
Deste modo, a medapeça dada ao medalutador j é o braço direito (i.e., D30). Em caso de empate na diferença de pontos, considere a ordem torso, braço esquerdo, braço direito e pernas.

O vencedor tem a sua habilidade decrementada da habilidade do oponente (definir como 0 quando o valor for negativo), devido ao desgaste mental da batalha. Já o perdedor tem sua habilidade reduzida pela metade (considere a divisão inteira por 2, i.e., H = H//2), sendo enviado para a repescagem caso seja a sua primeira derrota.

Antes de sua próxima batalha, cada medalutador tem tempo para descansar e conseguem recuperar sua habilidade em no máximo K, porém nunca ultrapassa seu valor inicial.

## Descrição da entrada
A primeira linha da entrada é composta por um inteiro N, onde N = . Para cada medalutador 1 ≤ i ≤ N, a primeira linha contém os inteiros Hi, Ki e Mi, que indicam respectivamente os pontos de habilidade e de recuperação e o números de medapeças do medalutador i; a segunda linha contém dois inteiros indicando respectivamente os bônus de ataque e defesa de sua medalha; e cada uma das Mi linhas seguintes contêm o tipo da medapeça, podendo ser os caracteres 'T' (torso), 'E' (braço esquerdo), 'D' (braço direito) e 'P' (pernas), seguindo de um inteiro que indica a quantidade de pontos da medapeça.

Observe um exemplo de entrada abaixo:
```
4
99 58 11
5 6
P 34
E 44
P 33
E 55
T 73
P 36
T 78
D 40
D 54
T 76
D 54
104 42 11
14 7
T 65
E 52
E 45
P 30
D 41
D 50
T 79
P 32
D 43
T 61
P 31
89 56 11
9 5
D 43
P 34
E 42
P 31
D 43
P 34
D 60
T 64
T 72
T 77
E 46
110 49 11
8 9
P 35
T 73
D 45
D 58
T 79
D 45
E 48
T 73
T 61
P 34
E 60
```

## Descrição da saída
Para cada cyberluta do torneio (exceto a final), o seu programa deverá imprimir uma linha contendo uma mensagem que indica o tipo de batalha, podendo ser ou "Cyberluta do Torneio Principal" ou "Cyberluta da Repescagem". A segunda linha de cada batalha conterá uma mensagem com o número de registro dos medalutadores, em ordem de menor para o maior, no formato "Medalutadores: i vs j", seguida de outras 6 linhas contendo a ficha técnica de cada, iniciando-se com um caractere de tabulação (i.e., '\t'), conforme indicado no exemplo. A última linha conterá uma mensagem com o número de registro do medalutador que venceu a batalha, no formato "Medalutador k venceu e recebeu a {identificação da medapeça}\n" (com uma quebra de linha extra). Para a grande final, seu programa deverá imprimir uma sequência de linhas de forma semelhante as demais, exceto pelo seguinte. A primeira linha conterá a mensagem "Cyberluta Final". A segunda linha conterá uma mensagem com o número de registro dos medalutadores, no formato "Medalutadores: i vs j", onde i​ e j​ são os finalistas respectivamente do torneio principal e da repescagem. A última linha conterá uma mensagem com o número de registro do medalutador campeão do torneio, no formato "Campeao: medalutador k".

A saída correspondente ao exemplo de entrada fornecido é:
```
Cyberluta do Torneio Principal
Medalutadores: 1 vs 2
    A1 = E55 + D54 + 5 = 114
    D1 = T78 + P36 + 6 = 120
    H1 = 99
    A2 = E52 + D50 + 14 = 116
    D2 = T79 + P32 + 7 = 118
    H2 = 104
Medalutador 2 venceu e recebeu a D54

Cyberluta do Torneio Principal
Medalutadores: 3 vs 4
    A3 = E46 + D60 + 9 = 115
    D3 = T77 + P34 + 5 = 116
    H3 = 89
    A4 = E60 + D58 + 8 = 126
    D4 = T79 + P35 + 9 = 123
    H4 = 110
Medalutador 4 venceu e recebeu a D60

Cyberluta da Repescagem
Medalutadores: 1 vs 3
    A1 = E55 + D54 + 5 = 114
    D1 = T78 + P36 + 6 = 120
    H1 = 99
    A3 = E46 + D43 + 9 = 98
    D3 = T77 + P34 + 5 = 116
    H3 = 89
Medalutador 1 venceu e recebeu a T77

Cyberluta do Torneio Principal
Medalutadores: 2 vs 4
    A2 = E52 + D54 + 14 = 120
    D2 = T79 + P32 + 7 = 118
    H2 = 47
    A4 = E60 + D60 + 8 = 128
    D4 = T79 + P35 + 9 = 123
    H4 = 70
Medalutador 4 venceu e recebeu a T79

Cyberluta da Repescagem
Medalutadores: 1 vs 2
    A1 = E55 + D54 + 5 = 114
    D1 = T78 + P36 + 6 = 120
    H1 = 68
    A2 = E52 + D54 + 14 = 120
    D2 = T65 + P32 + 7 = 104
    H2 = 65
Medalutador 1 venceu e recebeu a D54

Cyberluta Final
Medalutadores: 4 vs 1
    A4 = E60 + D60 + 8 = 128
    D4 = T79 + P35 + 9 = 123
    H4 = 72
    A1 = E55 + D54 + 5 = 114
    D1 = T78 + P36 + 6 = 120
    H1 = 61
Campeao: medalutador 4
```