# Tarefa de Laboratório 05 - Funções - Parte 2
## Ordenação alternativa
Zunisha está organizando um evento para os alunos de computaçao desse semestre e preparou alguns brindes para recebê-los. Como os brindes são diferentes, os primeiros alunos a receber terão mais possibilidades de escolha e portanto serão mais privilegiados.

Pensando em como tornar as coisas mais justas e mais divertidas, Zunisha percebeu que tem acesso ao endereço dos alunos inscritos no evento. A partir disso, ela decidiu ordenar a entrega dos brindes com base em algumas estratégias não-convencionais envolvendo os endereços. Afinal, Zunisha sabe muito bem o que é ser a última numa lista de nomes em ordem alfabética.

Sua tarefa neste lab será ajudar Zunisha a ordenar uma lista de endereços com base em um critério específico para cada um dos cinco dias do evento (segunda a sexta). Os critérios são os seguintes:

- **Segunda-feira:** ordenar os endereços de forma crescente com base no número de letras minúsculas da string.
- **Terça-feira:** ordenar os endereços de forma decrescente com base no número de letras maiúsculas da string.
- **Quarta-feira:** ordenar os endereços de forma crescente com base no número de caracteres da string que são letras do alfabeto.
- **Quinta-feira:** ordenar os endereços de forma crescente com base no número de palavras. Para esta tarefa, vamos considerar que uma palavra é uma sequência de letras e/ou números separada por espaços em branco.
- **Sexta-feira:** ordenar os endereços de forma decrescente com base na soma dos valores ASCII dos caracteres da string (incluindo os caracteres que são espaços em branco).

## Descrição da entrada
A entrada de um caso de teste é composta por diversas linhas:

- A primeira linha contém o dia da semana (Segunda, Terca, Quarta, Quinta ou Sexta) e um número N representando a quantidade de endereços que devem ser ordenados. Os dois valores são separados por um espaço em branco.
- Seguem N linhas, cada uma contendo um endereço. Cada endereço sempre será uma string composta de espaços em branco, letras do alfabeto ou números.
Veja um exemplo de entrada abaixo:
```
Quinta 4
Av do Bom Fim Qd 15 N 12
Rua das Laranjeiras 14
Av Albert Einstein 1251
Rua Pitagoras 9
```

## Descrição da saída
A saída deve conter os endereços ordenados, isto é, você deve imprimir um total de N linhas, onde a i-ésima linha contém o endereço que aparece na posição i da ordenação.
Veja a saída correspondente ao exemplo de entrada:
```
Rua Pitagoras 9
Rua das Laranjeiras 14
Av Albert Einstein 1251
Av do Bom Fim Qd 15 N 12
```
**Obs.**: caso haja empate entre dois ou mais endereços, dê preferência para os endereços que apareceram primeiro na entrada. Observe, por exemplo, o segundo e o terceiro endereços do exemplo de entrada.

## Dicas para esta tarefa
Preparamos algumas dicas para ajudar você nesse lab, veja abaixo.

### Ordenando uma lista no Python
Você pode ordenar uma lista no Python utilizando a função sorted(iterable, key=None, reverse=False). Essa função recebe três parâmetros, sendo o primeiro obrigatório e os últimos dois opcionais:
- iterable: é a sequência que desejamos ordenar. No nosso caso, este parâmetro será uma lista.
- key: é uma função que define o valor que cada elemento da lista terá na ordenação. Essa função deve receber um único parâmetro e devolver um único valor. Por padrão, o valor utilizado é o do próprio elemento.
- reverse: é um valor do tipo Boolean que define o sentido da ordenação. Quando o valor desse parâmetro for False (valor padrão) os elementos serão ordenados de maneira crescente. Quando esse parâmetro receber True, os elementos serão ordenados em ordem decrescente.

Veja um exemplo de como podemos ordenar uma lista de inteiros em ordem crescente:
```
>>> lista = [9, 4, 20, -1, 40, -8, 2, -3, -2]
>>> lista_ordenada = sorted(lista)
>>> print(lista_ordenada)
[-8, -3, -2, -1, 2, 4, 9, 20, 40]
```

Se quisermos ordenar a mesma lista em ordem decrescente podemos utilizar o parâmetro reverse:
```
>>> lista = [9, 4, 20, -1, 40, -8, 2, -3, -2]
>>> lista_ordenada = sorted(lista, reverse=True)
>>> print(lista_ordenada)
[40, 20, 9, 4, 2, -1, -2, -3, -8]
```

E ainda, se quisermos ordenar a lista com base no quadrado de cada elemento, podemos criar uma função que computa o quadrado de um número e passá-la através do parâmetro key :
```
>>> lista = [9, 4, 20, -1, 40, -8, 2, -3, -2]
>>> def eleva_quadrado(x):
...     return x*x
...
>>> lista_ordenada = sorted(lista, key=eleva_quadrado)
>>> print(lista_ordenada)
[-1, 2, -2, -3, 4, -8, 9, 20, 40]
```
Perceba que no exemplo acima os elementos foram ordenados de forma crescente através do valor definido pela função especificada por parâmetro, entre outras palavras, quando calculamos o quadrado de cada elemento, a lista fica ordenada.

**Obs.**: a função sorted() é uma função de ordenação estável, isto é, ela sempre mantém a ordem relativa original dos elementos quando há empate entre o valor deles. Veja, por exemplo, o que aconteceu com o 2 e o -2 no último exemplo: apesar do -2 ser menor, ele apareceu depois do 2 quando a lista foi ordenada. Esse comportamento se deve ao fato de o valor de comparação dos dois elementos serem iguais e o -2 aparecer após o 2 na lista original. Nesse [link](https://docs.python.org/pt-br/dev/howto/sorting.html) você encontra outros exemplos de uso da função sorted .

### Obtendo o valor ASCII de um caractere
Assim como nos labs anteriores, você pode obter o valor decimal de um caractere utilizando a função ord(). Veja um exemplo de como obter o valor ASCII do caractere 'a':
```
>>> ord('a')
97
```

### Verificações com caracteres
Veja abaixo alguns comandos sobre strings que podem ser úteis para você nesta tarefa:

- Você pode verificar se um caractere é uma letra maiúscula através do comando .isupper(). Veja um exemplo:
```
>>> c = 'a'
>>> c.isupper()
False
>>> c = 'A'
>>> c.isupper()
True
```
- Para verificar se um caractere é uma letra minúscula, você pode usar o comando .islower():
```
>>> 'a'.islower()
True
>>> 'A'.islower()
False
```
- Para checar se um caractere é uma letra do alfabeto você pode utilizar o comando .isalpha(). Exemplo:
```
>>> 'A'.isalpha()
True
>>> '1'.isalpha()
False
```