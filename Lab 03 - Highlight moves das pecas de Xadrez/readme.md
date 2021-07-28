# Tarefa de Laboratório 03 - Repetição - Parte 2
## Highlight moves das peças de Xadrez
O Xadrez é um jogo de estratégia que auxilia no desenvolvimento cognitivo, para a realização de tarefas que exijam raciocínio lógico, a reflexão e a memória. Devido à esses fatos, muitas pessoas buscam aprender a jogar xadrez. Para facilitar o seu aprendizado, em versões virtuais do jogo, utilizam-se o realce (highlighting) das casas para o movimento básico de uma peça.

### Movimentos básicos
**Torre**
A Torre se movimenta em direções ortogonais, isto é, pelas linhas (horizontais) e colunas (verticais).

**Bispo**
O Bispo se movimenta nas direções diagonais, não podendo se mover pelas ortogonais como as torres.

**Dama**
A Dama (também chamada de Rainha) pode movimentar-se tanto na diagonal, como na vertical ou na horizontal.

**Rei**
O Rei se movimenta em todas as direções, mas limitado somente à sua casa vizinha.

**Cavalo**
O Cavalo se movimenta em "L", ou seja, anda duas casas em linha reta e depois uma casa para o lado. O círculo formado pela possíveis casas finais do seu "pulo" corresponde ao movimento octogonal permitido pelo quadriculado do tabuleiro.

**Peão**
O Peão é a única peça do xadrez que nunca retrocede no tabuleiro. Esta peça move-se em coluna (vertical) somente para a frente e uma casa, nunca para trás. Quando se encontra na segunda fila, sempre estará disponível para fazer o seu primeiro movimento. Nesse caso ele pode optar entre andar uma ou duas casas sempre na mesma coluna. Passando da segunda fila, não mais pode se deslocar duas casas, mesmo que não o tenha feito em seu primeiro movimento.

**Importante:** Existem outros movimentos no jogo de Xadrez, pórem, para este lab, considere apenas os movimentos básicos apresentados acima.

## Tarefa
A sua tarefa neste lab será escrever um programa que imprime um tabuleiro de highlighting para as possíveis casas que uma dada peça do jogo de Xadrez pode permanecer após um movimento básico.

Para este lab iremos considerar variantes do jogo em que o tabuleiro pode apresentar outras dimensões, em vez de fixa no padrão 8x8.

## Descrição da entrada
A entrada é composta de vários conjuntos de teste. A primeira linha de um conjunto de testes contém um número inteiro N que indica o número de linhas e de colunas do tabuleiro. A seguir, é dado o nome da peça, sem o sinal gráfico de til (~), e a casa atual da peça o tabuleiro, no formato letra de coluna e número de linha separados com um espaço em branco.

**Importante:** Em particular a peça Peão, considere sempre que esta trata-se de uma peça "branca" e, portanto, segue a orientação utilizada no exemplo acima. Por exemplo, se a peça estiver na linha 4, então só pode avançar para a linha 5 (não muda de coluna).

### Restrições
- 8 ≤ N ≤ 26 (N = 0 apenas para indicar o fim da entrada).
Observe um exemplo de entrada abaixo:
```
8
Torre d 4
9
Cavalo e 5
0
```

## Descrição da saída
Para cada conjunto de teste da entrada, seu programa deve produzir a saída da seguinte forma. A primeira linha deve conter uma mensagem no formato '**Movimentos para a peca {nome da peça} a partir da casa {identificação da casa}.**'. As próximas N+1 linhas devem formar uma ilustração do tabuleiro, conforme o exemplo abaixo, onde os caracteres '-', 'x' e 'o' indicam respectivamente as casas não-alcançáveis e alcançáveis com um movimento, e origem da peça no tabuleiro. Após cada conjunto de teste imprima uma linha em branco.

A saída correspondente ao exemplo de entrada fornecido é:
```
Movimentos para a peca Torre a partir da casa d4.
8 - - - x - - - -
7 - - - x - - - -
6 - - - x - - - -
5 - - - x - - - -
4 x x x o x x x x
3 - - - x - - - -
2 - - - x - - - -
1 - - - x - - - -
  a b c d e f g h

Movimentos para a peca Cavalo a partir da casa e5.
9 - - - - - - - - -
8 - - - - - - - - -
7 - - - x - x - - -
6 - - x - - - x - -
5 - - - - o - - - -
4 - - x - - - x - -
3 - - - x - x - - -
2 - - - - - - - - -
1 - - - - - - - - -
  a b c d e f g h i
```

## Dicas de Python para esta tarefa
Os computadores representam tudo através de zeros e uns. No caso de textos, é utilizado um sistema de codificação que faz a conversão de caracteres para números, para que depois o computador possa ter a representação binária disso.

A codificação [ASCII](https://pt.wikipedia.org/wiki/ASCII) é usada para representar textos em computadores, que faz a conversão de 95 sinais gráficos (letras do alfabeto latino, algarismos arábicos, sinais de pontuação e sinais matemáticos).

Por exemplo, o caractere 'a' minúsculo é representado na codificação ASCII pelo decimal 97; enquanto que o caractere 'b' minúsculo é representado na codificação ASCII pelo decimal 98.

Em Python, você pode obter o valor decimal ASCII de um caractere com a função ord. Por exemplo, no terminal do Python:
```
>>> print(ord('a'))
97
```
Obs.: os caracteres >>> são do próprio ''terminal'' do Python antes de executar o comando.

Também é possível converte o valor decimal em um caractere com a função chr:
```
>>> print(chr(97))
a
```
Ainda é possível obter o alfabeto de forma fácil, como no exemplo abaixo.
```
>>> for i in range(26):
...       print(chr(ord('a')+i), end=' ')
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

## Escrevendo no terminal
Você já sabe que para escrever no terminal podemos utilizar a função print. Porém, existem algumas opções que podemos utilizar para melhorar a visualização do conteúdo que será exibido.

Para escrever uma cadeia de caracteres sem uma quebra de linha, você pode alterar o finalizador padrão end, como no exemplo anterior, em que o alfabeto é impresso em uma única linha.

Podemos controlar a separação entre os parâmetros passados para a impressão alterando o separador padrão sep. Veja um exemplo:
```
>>> print('a', 'b', sep='')
ab
```

## Revisão de for e range
É comum o uso do gerador de sequências range com o laço for. Lembre-se que o range permite especificar o início da sequência, o valor final e o passo. Veja um exemplo em ordem crescente e outro em ordem decrescente.
```
>>> for i in range(1, 8, 2) :
...   print(i, end=' ')
1 3 5 7
```
```
>>> for i in range(7, 0, -2) :
...   print(i, end=' ')
7 5 3 1
```