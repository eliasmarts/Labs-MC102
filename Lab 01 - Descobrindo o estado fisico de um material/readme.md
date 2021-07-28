# Tarefa de Laboratório 01 - Condicionais
## Identificando o estado físico de um material
Os laboratórios Repsol são especializados em coletar, analisar e redistribuir materiais de diversos tipos. Como nem sempre há uma garantia do estado de cada um desses materiais após a coleta, o processo de análise foi instaurado de forma a garantir certos procedimentos antes que os outros setores possam receber os insumos.

Você foi contratado para auxiliar no processo de análise dos materiais. Escreva um programa que, dados o nome de um material, sua temperatura atual e seus pontos de fusão e ebulição, diga em qual estado físico o material está, podendo ser sólido, líquido ou gasoso.

As temperaturas dos pontos de fusão e ebulição sempre estarão em Celsius, pois foram catalogados assim. No entanto, por um erro de comunicação interna e por outros fatores (como falta de verba para comprar mais equipamentos), os laboratórios Repsol só conseguiram aparelhos que aferem a temperatura atual em Fahrenheit. Você precisará tomar os devidos cuidados para fazer sua solução.

## Descrição da entrada
Nesta tarefa serão trabalhados os conceitos de leitura de valores, operações aritméticas e condicionais. A entrada que seu programa recebe é composta por 4 linhas:

- A primeira terá o nome do material e.g. Sodio.
- A segunda terá o ponto de fusão (sempre em Celsius) do material. Esse dado sempre será um tipo float e.g. 97.5. Considere que esta entrada sempre será um valor numérico, menor que o ponto de ebulição.
- A terceira terá o ponto de ebulição (também sempre em Celsius) do material. Esse dado sempre será um tipo float e.g. 882.8. Considere que esta entrada sempre será um valor numérico, maior que o ponto de fusão.
- A quarta linha terá a temperatura atual (sempre em Fahrenheit) aferida do material. O dado também será do tipo float e.g. 200.6. Considere que esta entrada sempre será um valor numérico.

OBS: Você deve ter notado que o nome do material foi dado sem acento. Isso é intencional para garantir que seu programa possa funcionar direito e não ter problemas com o run.codes. Sempre evite utilizar caracteres com acentos de qualquer forma em seus programas, seja na entrada, nomes de variáveis ou saída.

O exemplo descrito acima quando colocado no formato de entrada esperado pelo seu programa é o seguinte:

```
Sodio
97.5
882.8
200.6
```

## Descrição da saída
A saída de seu programa deve ser composta da seguinte forma, porém sem acentos, como comentado anteriormente:

- Material: o nome do material lido na entrada.
- Ponto de fusão (Celsius): a temperatura do ponto de fusão lida na entrada. Formatada com 2 casas decimais.
- Ponto de ebulição (Celsius): a temperatura do ponto de fusão lida na entrada. Formatada com 2 casas decimais.
- Temperatura atual (Celsius): a temperatura atual lida na entrada, convertida para Celsius. Formatada com 2 casas decimais.
- Estado físico do material: o estado físico do material (sólido, líquido ou gasoso) calculado de acordo com os dados recebidos.

Para o exemplo com o Sódio descrito acima, a saída correspondente seria:

```
Material: Sodio
Ponto de fusao (Celsius): 97.50
Ponto de ebulicao (Celsius): 882.80
Temperatura atual (Celsius): 93.67
Estado fisico do material: Solido
```

## Importante: Operações com *float* e erros de precisão
A representação de números em ponto flutuante no computador utiliza frações binárias (na base 2). Como nem sempre é possível converter uma fração na base 10, que é a que utilizamos no dia-a-dia, para a base 2, aproximações precisam ser feitas. Dessa forma, podem ocorrer erros de precisão que são propagados e, quando tentamos aplicar uma lógica aritmética nossa utilizando float, nem sempre sai o resultado esperado. Considere o seguinte código, realizado em um terminal do Python:

```
>>> a = 1.1
>>> b = 2.2
>>> a + b
3.3000000000000003
```

Então se você tentar realizar uma comparação com o valor esperado, que seria 3.3, o resultado não é bem o que você imagina. Veja:
```
>>> a = 1.1
>>> b = 2.2
>>> a + b == 3.3
False
```

Como nessa tarefa a comparação com valores em float será necessária, você precisa se atentar pro caso disso acontecer. Uma solução é utilizar a função round() no resultado da operação para que ele saia como o esperado. Observe o exemplo abaixo:

```
>>> a = 1.1
>>> b = 2.2
>>> c = a + b

c
3.3000000000000003
d = round(c, 1)
d
3.3
d == 3.3
True
```

Ainda iremos estudar funções com mais detalhes, mas a round() precisa ser utilizada da seguinte forma: o primeiro valor (chamado de parâmetro) colocado dentro dos colchetes é o valor que você quer arredondar. Pode ser uma expressão aritmética direta, como a + b, ou uma variável que já possui um valor (como no caso do exemplo, a variável c).

O segundo valor é a quantidade de casas decimais que se deseja obter (as que ficam após o ponto decimal). Nesse caso, como queríamos comparar com o valor 3.3 precisávamos utilizar apenas 1 casa decimal, por isso a utilização no exemplo ficou como round(c, 1). Note que há uma vírgula separando os parâmetros da função! Isso deve ser respeitado.

Como nesta tarefa você irá realizar operações com float e, principalmente, realizar comparações com os resultados, talvez esses erros de precisão aconteçam e você não obtenha os resultados esperados dos casos de teste, então fique atento ao uso da função round(), mas lembre-se que o valor a ser arredondado (o primeiro parâmetro) deve ser sempre o resultado de uma operação com float. Arredondar os valores antes de operar sobre eles pode resultar em valores incorretos.

Se quiser obter mais informações a respeito de representações em pontos flutuantes e erros de precisão, você pode consultar esta página da documentação do Python 3.

Importante: E se a temperatura atual for igual ao ponto de fusão ou ebulição?
Como os pontos de fusão e ebulição são estados transientes, para afirmar para qual estado físico o material está se tornando quando nessas temperaturas, precisaria saber se o mesmo está recebendo ou perdendo calor. Para fins de simplificação, considere que sempre há agitação do material para o mesmo ter sua temperatura aferida pelos profissionais da Repsol, então, se a mesma for igual ao ponto de fusão, o material está no estado líquido. Já se a temperatura atual for igual ao ponto de ebulição, considere que o material está no estado gasoso.

## Dicas para esta tarefa
Um dos lemas dos Laboratórios Repsol é que você nunca está sozinho. Adam, seu supervisor, preparou algumas dicas pra te ajudar nessa tarefa.

### Lendo os valores de entrada:
Você pode usar o comando input() do Python pra isso. Esse comando faz com que seu programa espere uma entrada de dado vinda externamente, como alguém digitando no teclado, ou lendo dos arquivos de teste que serão utilizados para verificar seu programa.

Por exemplo, para ler o nome do material, você pode fazer assim:

material = input()
O comando input() pode ser utilizado junto com outros tipos comuns de dados e.g. int ou float que são empregados para que o valor lido seja convertido automaticamente para o tipo especificado. Por exemplo, para ler uma temperatura qualquer, que é dada em float, você pode fazer assim:

pontoFusao = float(input())

### Formatando a saída com casas decimais específicas:
O comando format() em Python pode te ajudar nessa parte. Ela é bem similar à round() que vimos acima, mas dessa vez seu uso é mais voltado na hora de utilizar um valor impresso, formatando-o com o número de casas decimais especificado, arredondando-o se necessário. Observe o exemplo abaixo:

```
>>> a = 1.1
>>> b = 2.2
>>> c = round(a+b, 2)
>>> c
3.3
format(c, '.1f')
'3.3'
format(c, '.2f')
'3.30'
```

Repare que, ao arredondar o valor de a+b com 2 casas decimais, o resultado ainda foi 3.3, com 1 casa decimal "mostrada". Ao utilizar o valor da format() pedindo 1 casa decimal, o valor resultante foi '3.3', parecendo igual a c, só que no formato de string. Mais abaixo, ao utilizar format() com 2 casas decimais, o resultado foi '3.30', apresentando um 0 ao final. Nesta tarefa, você deve utilizar a format() pedindo que sejam apresentadas 2 casas decimais.
Se estiver interessado em saber mais como esse comando funciona, você pode consultar esta página sobre [Formatação em Python](https://www.ic.unicamp.br/~mc102/mc102-1s2020/labs/format.html).