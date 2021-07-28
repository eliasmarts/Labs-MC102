# Tarefa de Laboratório 11 - Busca e Ordenação
## Ajudando a Yelena
Os eldianos que vivem na ilha de Paradis basicamente declararam guerra a nação de Marley, após [Eren Jaeger](https://attackontitan.fandom.com/pt-br/wiki/Eren_Jaeger_(Anime)) atacar Marley para conseguir mais poder. Ao retornarem para a ilha de Paradis, o Capitão [Levi Ackerman](https://attackontitan.fandom.com/pt-br/wiki/Levi_Ackerman_(Anime)) recebeu ordens para transportar [Zeke Jaeger](https://attackontitan.fandom.com/pt-br/wiki/Zeke_Jaeger_(Anime)), chefe da Unidade de Guerreiros que servem o exército da nação de Marley, como prisioneiro a partir do porto da ilha até as prisões subterrâneas localizadas dentro das Muralhas. A [Yelena](https://attackontitan.fandom.com/pt-br/wiki/Yelena_(Anime)), ex-soldado de Marley e seguidora de Zeke Jaeger, pretende resgatá-lo e escondê-lo em um de seus esconderijos fora das Muralhas. Talvez você não queira ajudar a Yelena, mas ela precisa muito da sua ajudar para determinar o melhor local para a intercepção da tropa liderada pelo Capitão Levi, que está escoltando Zeke.

Considere então um plano cartesiano para a ilha de Paradis, em que o seu porto está na coordenada (0, 0) e o portão da Muralha Maria, primeira e a maior, está na coordenada (0, Y). O curso da viagem é feita em linha reta, ou seja, sobre o eixo das ordenadas. A Yelena pretende interceptar a tropa em algum ponto (0, Yi), para 0 < Yi < Y. Ela quer esconder Zeke no esconderijo mais distante de (0, Yi).

A sua tarefa será escrever um programa que leia a coordenada do portão da Muralha Maria e as coordenadas dos N esconderijos que a Yelena possui na ilha de Paradis. A saída do seu programa é a coordenada (0, Yi), onde Yi é inteiro, tal que o esconderijo mais distante é minimizado.

## Descrição da entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém dois inteiros N e Y, indicando respectivamente o número de esconderijos e o valor da ordenada que representa a coordenada do portão da Muralha Maria. Cada uma das N linhas seguintes contém dois inteiros x e y que representam os valores da coordenada do esconderijo.

O último caso de teste é seguido por uma linha que contém apenas dois números zero.

**Observações:**

- As coordenadas dos esconderijos estarão presentes apenas nos 1º e 2º quadrantes.
- Restrições **2 ≤ N ≤ 130** e **5 ≤ Y ≤ 10^6** (N = 0 e Y = 0 apenas para indicar o fim da entrada).

## Descrição da saída
Para cada caso de teste da entrada, seu programa deve imprimir uma linha contendo o valor (inteiro positivo) Yi que representa a coordenada (0, Yi), tal que o a distância do esconderijo mais distante para qualquer outra coordenada (0, Yj), para j ≠ i, é maior que a distância do esconderijo mais distante de (0, Yi), ou seja, a distância do esconderijo mais distante é minimizada.

**Observações:**
- Para cada caso de teste sempre existe apenas uma única coordenada (0, Yi), tal que o esconderijo mais distante é minimizado.
- Aliás, todas as Y-1 distâncias do esconderijo mais distante, ou seja, de cada coordenadas (0, Yi), para 0 < Yi < Y, são distintas.
- A métrica a ser utilizada para a distância entre dois pontos é a distância euclidiana.

### Exemplo de entrada
```
7 11
3 10
-1 4
3 4
2 1
-2 7
-1 10
4 7
0 0
```
### Saída
```
6
```

A Yelena quer encontrar logo a posição da interceptação da tropa. Mais precisamente, o tempo limite de execução é 1 segundo.