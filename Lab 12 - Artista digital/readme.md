# Tarefa de Laboratório 12 - Recursão - Parte 1
## Artista digital
Smeargle é um pintor russo do século XX adepto ao [suprematismo](https://pt.wikipedia.org/wiki/Suprematismo). Seu principal lema de vida é acreditar que grandes quadros podem ser criados sobrepondo apenas formas geométricas elementares como o quadrado e o círculo.

Fascinado com a modernização trazida pela computação, Smeargle decidiu criar suas próximos artes abstratas utilizando um computador e pediu sua ajuda para isso. Dada uma matriz representando uma tela de pintura, sua tarefa nesse laboratório será desenhar uma sequência de quadrados e círculos na tela de pintura de acordo com os comandos de Smeargle.

## Descrição da entrada
A entrada de um caso de teste é composta por diversas linhas:
- A primeira linha possui dois inteiros M e N, indicando que a tela de pintura possui M linhas e N colunas.
- A segunda linha possui um inteiro Q, indicando a quantidade de formas geométricas que serão desenhadas.
- Seguem Q linhas, cada uma com a descrição de um círculo ou de um quadrado a ser desenhado:
    1. se a linha se tratar da descrição de um círculo, ela será apresentada na forma "circulo i j r", indicando que deve ser desenhado um círculo com centro na posição (i, j) da matriz e com raio r. Os valores i, j, e r sempre serão inteiros;
    2. se a descrição for de um quadrado, a linha será da forma "quadrado i j l", indicando que deve ser desenhado um quadrado com lado de tamanho l e o centro do quadrado deve estar na posição (i,j) da matriz. Os valores i, j e l sempre serão inteiros, e o valor do lado l sempre será ímpar.

Veja um exemplo de entrada abaixo:
```
20 21
2
quadrado 3 4 7
circulo 11 11 8
```

## Descrição da saída
A saída de um caso de teste deve ser composta por M linhas, cada uma com N caracteres separados por espaços em branco, formando uma ilustração da tela de pintura com os desenhos. Uma posição da matriz pintada deve ser representada pelo caractere x e uma posição não-pintada deve ser representada por um traço (-).

**Observações:**
- Para desenhar os círculos, você deve considerar que uma posição (x, y) da matriz faz parte de um círculo se a distância euclidiana entre o centro (i, j) do círculo e a posição (x, y) for menor ou igual ao raio r.
- Para os casos em que o desenho de uma forma geométrica ultrapassar os limites da tela de pintura, pinte somente as posições do desenho que estão contidas dentro da matriz.
Veja a saída correspondente ao exemplo de entrada:
```
- x x x x x x x - - - - - - - - - - - - -
- x x x x x x x - - - - - - - - - - - - -
- x x x x x x x - - - - - - - - - - - - -
- x x x x x x x - - - x - - - - - - - - -
- x x x x x x x x x x x x x x - - - - - -
- x x x x x x x x x x x x x x x x - - - -
- x x x x x x x x x x x x x x x x x - - -
- - - - - x x x x x x x x x x x x x - - -
- - - - x x x x x x x x x x x x x x x - -
- - - - x x x x x x x x x x x x x x x - -
- - - - x x x x x x x x x x x x x x x - -
- - - x x x x x x x x x x x x x x x x x -
- - - - x x x x x x x x x x x x x x x - -
- - - - x x x x x x x x x x x x x x x - -
- - - - x x x x x x x x x x x x x x x - -
- - - - - x x x x x x x x x x x x x - - -
- - - - - x x x x x x x x x x x x x - - -
- - - - - - x x x x x x x x x x x - - - -
- - - - - - - - x x x x x x x - - - - - -
- - - - - - - - - - - x - - - - - - - - -
```
O objetivo deste laboratório é trabalhar os conceitos de **recursão**. Portanto, **soluções que estejam corretas mas não utilizem recursão para pintar os desenhos não são permitidas.**

## Dicas para esta tarefa
Quando você executa uma função recursiva com o Python, é possível que seu programa gere o erro "RecursionError: maximum recursion depth exceeded". Esse erro nos diz que a quantidade de chamadas recursivas que foram armazenadas simultaneamente na pilha de chamadas excedeu o limite de segurança do Python.

Essa trava de segurança busca prevenir que o Python pare de funcionar devido a um "estouro de memória", causado por uma recursão infinita (i.e., uma função recursiva que nunca alcança os casos base) ou por um número de chamadas recursivas muito grande.

Para essa tarefa, o limite padrão do Python deve ser suficiente para resolver todos os casos de teste usando funções recursivas. Portanto, se o seu programa gerar um RecursionError, tente revisar a implementação em busca de pontos em que seja possível reduzir o número de chamadas recursivas realizadas ou de pontos que estejam causando uma recursão infinita.

Caso seja necessário, você pode tentar ajustar o limite do Python para permitir o uso de um número maior de chamadas recursivas. Para consultar o limite de recursão atual, podemos utilizar a função getrecursionlimit da biblioteca sys. Veja um exemplo:
```
>>> import sys
>>> sys.getrecursionlimit()
1000
```
Para alterar o limite de recursão, podemos utilizar a função setrecursionlimit, passando o novo limite como parâmetro:
```
>>> import sys
>>> sys.setrecursionlimit(1500)
```
**Cuidado:** alterar o limite de recursão para um valor muito alto pode permitir que seu programa gere erros inesperados.