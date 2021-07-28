# Tarefa de Laboratório 09 - Matrizes
## Supermatriz comum

Uma submatriz de uma matriz **A** de ordem N é qualquer matriz obtida de **A** eliminando-se certas linhas ou colunas, ou é a própria matriz **A**. Por exemplo, considere a seguinte matriz:
**A = 2 1 -1**
    **0 3 -2**

As submatrizes de **A** de ordem 2, ou seja, de dimensão 2 x 2, são as seguintes:
**2 1    2 -1    1 -1**
**0 3    0 -2    3 -2**

No exemplo, as submatrizes são obtidas respectivamente por eliminação das colunas 3, 2 e 1. A matriz **A** também possui submatrizes de dimensões 2 x 3, 2 x 1, 1 x 3, 1 x 2 e 2 x 1.

Para este laboratório de programação estamos interessado apenas nas submatrizes em que somente as primeiras ou as últimas linhas e colunas são eliminadas da matriz. Em outras palavras, mais formalmente, dada uma matriz **S**, de dimensão p x q, estamos interessado em submatrizes que inclui todos os elementos *sij* de **S**, ou seja, os elementos da I-éssima linha e J-éssima coluna, para ***l1 <= i <= l2*** e ***c1 <= j <= c2***, onde ***1 <= l1 <= l2 <= p*** e ***1 <= c1 <= c2 <= q***. Uma submatriz com essa propriedade é dita ser submatriz legal.

Considerando o exemplo anterior para submatrizes de dimensão 2 x 2 da matriz **A**, são submatrizes legais somente as submatrizes:
**2 1    1 -1**
**0 3    3 -2**


Agora, considere duas matrizes quadradas **M** e **N**, de ordem m e n, respectivamente. Dizemos que uma matriz **S**, de dimensão p x q, é uma supermatriz comum de **M** e **N** se as seguintes condições são verdadeiras:
- existe uma submatriz legal **M'** de **S** tal que **M'** e **M** são iguais; e
- existe uma submatriz legal **N'** de **S** tal que **N'** e **N** são iguais.
Por exemplo, considere as seguintes matrizes:
**M** = 83 57
    87 95

**N** = 95 37 49
    6  56 73    
    67 22 14

Uma possível supermatriz comum para essas matrizes pode ser a seguinte matriz:
**S** = 83 57 11 77
    87 95 37 49
    84 6  56 73
    70 67 22 14

A submatriz **N'** de **S**, tal que **N'** e **N** são iguais, é formada por todos os elementos *sij* de **S**, para 2 <= i <= 4 e 2 <= j <= 4.

A sua tarefa será escrever um programa que leia as matrizes **M** e **N**, onde cada matriz é formada por inteiros positivos distintos, e que imprime a dimensão da menor supermatriz comum de **M** e **N**, tal que a supermatriz comum também seja formada por apenas números distintos.

## Descrição da entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém dois inteiros m e n, indicando respectivamente a ordem das matrizes **M** e **N**, onde cada matriz é formada por números distintos. Cada uma das m linhas seguintes contém m inteiros positivos, representando os elementos da matriz **M**. Em seguida, de forma análoga, cada uma das n linhas seguintes contém n inteiros positivos, representando os elementos da matriz **N**.

O último caso de teste é seguido por uma linha que contém apenas dois números zero separados por um espaço em branco.

## Descrição da saída
Para cada caso de teste da entrada seu programa deve imprimir uma linha contendo a dimensão da menor supermatriz comum no formato "p x q", onde p é o número de linhas e q é o número de colunas, tal que a supermatriz comum seja formada por apenas números distintos.

Observações:
- As matrizes da entrada M e N possuem pelo menos um elemento em comum.
- Sempre será possível obter uma supermatriz comum com elementos distintos.

### Exemplo de entrada
```
3 2
9 7 5
2 3 4
1 6 8
10 11
23 9
2 2
1 5
9 2
3 7
1 5
0 0
```

### Saída
```
4 x 4
3 x 2
```
No primeiro caso de teste da entrada, temos:
M = 9 7 5
    2 3 4
    1 6 8

N = 10 11
    23  9

Uma possível submatriz comum, que satisfaz as condições da saída, seria a seguinte:
S = 10 11 21 12
    23  9  7  5
    15  2  3  4
    18  1  6  8

Já no segundo caso de teste da entrada, temos:
M = 1 5
    9 2

N = 3 7
    1 5

Só é possível obter uma submatriz comum, sendo:
S = 3 7
    1 5
    9 2

Dicas
1. Note que, para cada caso de teste, não é preciso gerar uma supermatriz comum para se determinar a sua dimensão. Em outras palavras, não se apegue a notação utilizada para apresentação dos conceitos.
2. Aproveite as informações contidas nas observações para criar uma solução simples.
3. Faça desenhos em um papel de quadros de tamanhos diferentes e se sobrepondo. Tente visualizar a característica em comum em cada desenho para criar uma solução simples e genérica.