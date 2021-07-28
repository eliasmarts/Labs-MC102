# Tarefa de Laboratório 13 - Recursão - Parte 2
## Magias em área
Em um jogo de Role Playing Game (RPG) de mesa, cada jogador deve interpretar um personagem que construiu, utilizando sua criatividade e as regras de um determinado sistema. Um desses jogadores, geralmente o mais experiente, é o Dungeon Master (DM), que é o responsável por conduzir a história, tecendo as consequências das interações dos outros jogadores com o cenário. Uma das responsabilidade do DM é organizar eventuais combates que ocorrem no mundo da campanha, que podem ser dos mais diversos tipos, com base no ambiente e as habilidades dos seus participantes.

Suponha que Guildenstern, pseudônimo de um amigo seu, está sendo o DM de uma campanha e quer criar um combate contra um inimigo poderoso - um mago. Esse mago já perdeu suas faculdades mentais em busca de algo que ninguém jamais conseguiu: uma magia suprema, da qual ninguém consegue escapar, chamada de Teraf L'are.

Os grimórios antigos mencionam que ninguém consegue escapar da Teraf L'are porque ela analisa o campo de batalha e se adapta ao mesmo, criando áreas de efeito, atingindo-o por completo. No entanto, ela precisa obedecer uma série de condições:
- As áreas de efeito, também conhecidas como submagias de nível, só podem ser quadrados com cada lado sendo uma potência de base 2, ou seja, são quadrados de área , em que i = 0, 1, 2... representa o nível da submagia
- Todas as magias possuem um custo na carga espiritual do usuário para serem conjuradas, conhecido como Pontos de Mana (PM). O custo total da Teraf L'are se dá pela soma dos custos de cada uma das submagias. O custo de uma submagia é dado pelo lado do quadrado de sua área de efeito.

Os combates nessa campanha ocorrem em um campo de batalha, representado por um retângulo de área M x N, formado pela junção de vários quadrados de área 1 x 1. Guildenstern está pedindo sua ajuda para saber um total de três informações sobre a Teraf L'are: o total de submagias por nível que serão utilizadas, o número total de submagias que estão compondo a Teraf L'are e o seu custo total em PM.

Como quanto maior a área, maior o dano, o mago de Guildenstern está preocupado em otimizar seu poder de devastação, utilizando o maior número possível de submagias de níveis elevados. Em outras palavras, a Teraf L'are deve cobrir todo o campo de batalha com o menor número necessário de submagias, sendo que estas devem ser dos maiores níveis possíveis. Por exemplo, considere um campo de 2x2. Ele poderia ser totalmente coberto com:

- **4** submagias de nível ***0*** ou
- **1** submagia de nível ***1***
No caso, a resposta certa seria 1 submagia de nível 1, pois ela representa o menor número necessário pra preencher todo o campo.

#### "Rolem iniciativa e estejam preparados, pois o Mago é Implacável!"

## Descrição da entrada
A entrada será composta por uma linha com as dimensões do campo de batalha, sendo a base M, e a altura N, separados por um espaço em branco.

Um exemplo de entrada seria (EX1):
```
6 5
```
Já outro exemplo poderia ser (EX2):
```
64 8
```

## Descrição da saída
A saída deverá seguir um formato de entrada nos Anais da História, pois cada vez que Teraf L'are é utilizada, o balanço do mundo muda. Uma entrada nesse formato segue três seções: Estudo, Calamidade e Sacrifício.

A seção de Estudo descreve a magia, é uma parte que começa uma entrada no Anal da História:
- A primeira linha é composta por três traços: "---", sem as aspas. A terceira linha segue exatamente o mesmo padrão
- A segunda linha é composta pelo nome, que segue o formato: "Grimorio de Teraf L'are", sem as aspas

A seção de Calamidade começa imediatamente na linha seguinte após a de Estudo. Ela descreve quantas submagias foram utilizadas, também informando seu nível, em ordem crescente, com uma entrada por linha. O número de linhas depende da quantidade submagias, mas sempre seguem o padrão:
- "X submagia(s) de nivel Y", em que X é a quantidade de submagias de nível Y que foram utilizadas (sem as aspas)
- Ao final desta seção, outra linha composta por três traços deve ser impressa.

Por fim, a seção de Sacrifício contém as informações sobre os custos que o usuário teve para utilizar a Teraf L'are. Ela começa imediatamente na linha seguinte após a de Calamidade, sendo uma linha contendo o número total de submagias conjuradas para formar a Teraf L'are, e outra linha contendo o total de PM gastos na sua utilização:
- "Total de submagia(s) conjurada(s): G", em que G é o número otimizado de magias conjuradas (sem as aspas)
- "Total de PM gasto: T", em que T é o total de PM gastos conjurando a Teraf L'are (sem as aspas)
- Por fim, uma última linha, novamente contendo três traços deve ser impressa, finalizando a entrada nos Anais da História.

A saída de EX1 seria:
```
---
Grimorio de Teraf L'are
---
6 submagia(s) de nivel 0
2 submagia(s) de nivel 1
1 submagia(s) de nivel 2
---
Total de submagia(s) conjurada(s): 9
Total de PM gasto: 14
---
```
A saída de EX2 seria:
```
---
Grimorio de Teraf L'are
---
8 submagia(s) de nivel 3
---
Total de submagia(s) conjurada(s): 8
Total de PM gasto: 64
---
```
IMPORTANTE: O objetivo deste laboratório é trabalhar os conceitos de recursão. Portanto, **soluções que estejam corretas mas não utilizem recursão para calcular as informações requeridas pelo mago de Guildenstern NÃO serão aceitas.**