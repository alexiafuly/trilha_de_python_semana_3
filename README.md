# Trilha de Python - Semana 3: Iterables, loops avançados e list comprehension
Desafio 3 da trilha de python da for_code, no qual aprendemos sobre manipulação de iteráveis, unpacking em listas de tuplas, list comprehension, etc.

## Funcionamento do programa
O programa analisa os dados fornecidos pelo sistema de inventário de um laboratório. O processamento das informações envolve manipulações de iterables, como o uso do set para remover duplicações, o uso do zip para unir listas, o uso do for para o unpacking dos valores e list comprehension para selecionar os valores que atendem a uma determinada condição. No fim, o programa imprime os tipos de reagentes disponíveis (sem repetições), a quantidade de reagentes diferentes, um relatório com os dados das listas zippadas (frasco do lote, reagente e pureza) e uma lista dos lotes cujo grau de pureza é maior que 98%.

## Respostas às perguntas teóricas
1) Levando em consideração a estrutura do nosso inventário, por que seria incorreto usar a função dict() para transformar o resultado do nosso zip() em um dicionário, utilizando o nome do reagente como "Chave" e o lote como "Valor"?
R: A função dict() só seria adequada se a função zip() tivesse 2 argumentos, em que um deles seria a chave e o outro o valor. Como há 3 argumentos, o uso do dict() gera um ValueError.

2) O que a função zip() gera na memória do Python antes de usarmos a função list() para forçar a visualização dos dados?
R: Gera uma tupla cujos elementos são as listas combinadas.

3) Observando o seu código final, de que forma o List Comprehension substitui a necessidade de criar uma lista vazia e usar a estrutura de repetição for tradicional acompanhada do método .append()?
R:  Utilizando for + .append(), o código ficaria da seguinte forma:

lista_lotes_aprovados = []
for nome, lote, pureza in lista_de_tuplas:
   if pureza >=98.0:
      lista_lotes_aprovados.append(lote)

Utilizando list comprehension, é possível fazer tudo que foi feito no bloco acima em uma só linha de código, otimizando a sintaxe.
