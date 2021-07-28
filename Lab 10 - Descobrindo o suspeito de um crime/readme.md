# Tarefa de Laboratório 10 - Combinando e Usando Estruturas de Dados
## Descobrindo o suspeito de um crime
```
Você foi identificado, recruta.
Seu posto atual é: Aluno de Graduação.

*** URGENTE ***
A intrépida gangue V.I.L.E recrutou incontáveis novos membros
que já estão cometendo diversos crimes pelo mundo.

Sua missão:
Ajude a equipe de detetives a criar um programa que
identifique o suspeito de um crime com base nas eventuais 
evidências encontradas.

Prazo para entrega:
Segunda, 20/06/2021, às 6h.

Boa sorte, recruta.
```
Parabéns, seu excelente trabalho ajudando a MAGAMI a não ter um prejuízo catastrófico devido ao furo em seus sistemas de proteção residencial lhe rendeu um novo cargo na empresa: agora você está na divisão destinada a investigação criminal. No seu primeiro dia de trabalho, a mensagem acima já está impressa em seu computador.

A mensagem veio seguida de um arquivo com mais detalhes sobre sua missão: com base em anos de inteligência, a MAGAMI conseguiu criar dossiês que compilam informações sobre os vilões. Esses dossiês são cruciais para que os detetives descubram quem é o suspeito de um crime para que possam redigir o mandato de prisão a tempo de sua captura.

Sua missão é desenvolver um programa que leia os dados do dossiê e um conjunto de evidências e, com base nelas, possa identificar o possível suspeito do crime.

Por exemplo, se seu dossiê (D) fosse:
```
Nome: Dr Wily
Sexo: Masculino
Tracos: Bigode

Nome: Fast Eddie B
Sexo: Masculino
Cabelo: Preto
Veiculo: Conversivel
```
E seu conjunto de evidências (EV1) fosse:
```
Cabelo: Preto
```
O suspeito seria: Fast Eddie B, pois aplicando EV1 em D, Fast Eddie B é o único que possui a característica de ter cabelo preto.

## Descrição da entrada
A entrada será composta por diversas linhas, que estarão divididas em dois conjuntos: os dados do dossiê e os dados das evidências.

Sobre o dossiê:
- O conjunto de dados do dossiê aparecerá primeiro. Cada linha seguirá um formato Característica: Valor (separados por dois pontos ':' e com um espaço em branco entre os ':' e o Valor), representando as informações sobre um suspeito que estão catalogadas na base de dados da MAGAMI.
- O conjunto de dados para cada suspeito não necessariamente tem quantidades iguais de características, nem é necessariamente composto pelas mesmas: repare que, no dossie D exemplificado acima, o suspeito "Dr Wily" possui a característica "Tracos: Bigode", enquanto "Fast Eddie B" não possui. A única característica garantida que aparece em todos é o Nome, que será sempre a primeira no conjunto de dados sobre um suspeito. Além disso, você pode considerar que não haverão suspeitos com o mesmo nome, tampouco existirem caracteres especiais em suas características e valores.
- A leitura de um hífen ("-", sem as aspas) sozinho numa linha informa o fim da entrada de dados para aquele suspeito, indicando que ainda tem mais informações a serem lidas sobre outros suspeitos.
- A leitura de dois hífens consecutivos ("--", sem as aspas) sozinhos numa linha informa o fim das entradas para o conjunto de dados do dossiê.

Sobre as evidências:
- O conjunto de dados das evidências tem início na linha após a leitura dos dois hífens consecutivos.
- As informações sobre as evidências seguem o exato formato das que compõe o dossiê, com a exceção de que o Nome jamais aparecerá neste conjunto de dados. Você pode considerar que o conjunto de evidências sempre terá pelo menos uma entrada válida no formato Característica: Valor.
- A leitura de três hífens consecutivos ("---", sem as aspas) indica o fim das entradas para o conjunto de evidências, representando também o fim da entrada deste laboratório.

Tomando o exemplo utilizado, a entrada representando D e EV1 seria:
```
Nome: Dr Wily
Sexo: Masculino
Tracos: Bigode
-
Nome: Fast Eddie B
Sexo: Masculino
Cabelo: Preto
Veiculo: Conversivel
--
Cabelo: Preto
---
```

## Descrição da saída
A saída é condicional ao fator de existirem ou não possíveis suspeitos com base no conjunto de evidências lido:

- Caso exista somente um suspeito identificado, seu programa deve imprimir a mensagem: "Suspeito(a):", seguido do nome do suspeito na próxima linha.
- Caso mais de um suspeito tenha sido identificado, seu programa deve imprimir a mensagem: "Suspeitos(as):", seguido dos nomes dos suspeitos, em ordem alfabética, com apenas o nome de um suspeito por linha.
- Caso não tenha sido possível identificar nenhum suspeito, seu programa deve exibir a mensagem "**Nenhum suspeito(a) com essas caracteristicas foi identificado(a).**" (sem as aspas).

Considerando novamente o exemplo dado por D e EV1, a saída seria:
```
Suspeito(a):
Fast Eddie B
```

### Importante: como assim nenhum ou mais de um suspeito?
Com base no conjunto de evidências, a ocorrência de algum desses dois casos é possível. Vamos considerar dois exemplos ainda com o mesmo dossiê D utilizado até agora.

Se o conjunto de evidências (EV2) fosse o seguinte:
```
Sexo: Masculino
```
Ambos Dr Wily e Fast Eddie B se encaixam nesse conjunto EV2, portanto, a saída seria:
```
Suspeitos(as):
Dr Wily
Fast Eddie B
```
Agora, considere esse outro conjunto de evidências (EV3):
```
Sexo: Feminino
Veiculo: Conversivel
```
Repare que, por mais que exista uma característica válida do conjunto de evidências, você precisa considerar todas as características para que um suspeito seja válido. Nesse caso, não há ninguém do sexo feminino em D, portanto, com base em EV3, a saída seria:
```
Nenhum suspeito(a) com essas caracteristicas foi identificado(a).
```

## Dicas para esta tarefa
Certamente você não aceitaria um novo cargo sem seu fiel escudeiro, o caderninho de dicas. Novas entradas surgiram nele conforme sua experiência vem crescendo:
#### Lidando com espaços em branco no começo/fim de uma string
Você deve ter percebido que a presença desse espaço em branco antes do valor de uma característica pode atrapalhar o funcionamento do seu programa. Para eliminar espaços em branco no começo e fim de uma string, você pode invocar seu método .strip(). Por exemplo:
```
>>> s1 = ' Hello, world! '
>>> print(s1)
 Hello, world!
>>> print(len(s1))
15
>>> s1 = s1.strip()
>>> print(s1)
Hello, world!
>>> print(len(s1))
13
```
Repare que apenas os espaços em branco no começo e fim de s1 foram removidos. Além disso, o valor de s1 por si só não é atualizado só pela utilização do strip(), pois ele retorna o valor de s1 sem os espaços em branco no começo e no final.

#### Imprimindo os suspeitos em ordem alfabética
Neste laboratório não é esperado que você implemente sua função para ordenar. Tendo uma lista de nomes, você pode se lembrar da ajuda que deu a Zunisha e utilizar a função sorted(). Relembrando seu uso:
```
>>> nomes = ['Lady Agatha', 'Dr Wily', 'Carmen Sandiego']
>>> ordenados = sorted(nomes)
>>> print(ordenados)
['Carmen Sandiego', 'Dr Wily', 'Lady Agatha']
```
Nesse caso, também não é necessário se preocupar em implementar uma ordenação "alternativa", pois a padrão que a sorted() usa é a por ordem lexicográfica crescente.