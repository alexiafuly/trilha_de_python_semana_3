# Dados do inventário físico (cada índice representa um frasco individual)

reagentes = ['Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno', 'Acetona',
'Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno', 'Etanol', 'Acetona', 'Ácido Acético',
'Etanol', 'Benzeno', 'Ácido Sulfúrico', 'Metanol', 'Ácido Acético',
'Etanol', 'Acetona', 'Tolueno', 'Ácido Sulfúrico', 'Benzeno', 'Etanol', 'Acetona',
'Metanol', 'Ácido Sulfúrico', 'Acetona', 'Ácido Acético', 'Etanol']

lotes = ['2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01',
'2023-BEN-01', '2024-ACE-01', '2023-ETA-02', '2024-SUL-01', '2023-MET-01',
'2024-TOL-01', '2023-ETA-01', '2023-ACE-01', '2023-ACA-01', '2023-ETA-02',
'2023-BEN-01', '2023-SUL-01', '2023-MET-01', '2024-ACA-01', '2023-ETA-01',
'2023-ACE-01', '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01',
'2023-ACE-01', '2023-MET-01', '2023-SUL-01', '2024-ACE-01', '2024-ACA-01',
'2023-ETA-02']

purezas = [99.5, 92.0, 99.5, 98.0, 99.9, 98.5, 96.0, 99.0, 99.0, 98.8, 99.5, 92.0, 99.2,
96.0, 99.9, 98.0, 99.0, 95.0, 99.5, 92.0, 98.8, 99.0, 99.9, 99.5, 92.0, 99.0, 98.0, 98.5,
95.0, 96.0]


# Identificação dos Tipos de Reagentes

## Utilizando a função set para remover repetições na lista de reagentes

set_reagentes = set(reagentes)

## Imprimindo os reagentes disponíveis e a quantidade total de reagentes sem repetições

print(f'\n Reagentes disponíveis: {set_reagentes}')
print(f'\n Quantidade total de reagentes diferentes: {len(set_reagentes)}')

# Estruturação do Inventário

## Utilizando a função zip para combinar as três listas, gerando tuplas com um item de cada lista

listas_combinadas = zip(reagentes, lotes, purezas)

## Utilizando a função list para listar as tuplas

lista_de_tuplas = list(listas_combinadas)

# Geração de Relatório

print('\n Relatório:')

## Usando for para fazer o unpacking das tuplas, imprimindo um relatório com o frasco do lote, o nome do reagente e o grau de pureza

for tupla in lista_de_tuplas:
   nome,lote,pureza = tupla
   print('Frasco do lote: {} | Reagente: {} | Pureza: {}%'.format(lote, nome, pureza))

# Filtragem por Critério de Qualidade

## Utilizando list comprehension para criar uma nova lista contendo somente os lotes que atendem ao critério de pureza

lista_lotes_aprovados = [lote for nome, lote, pureza in lista_de_tuplas if pureza >= 98.0]
print(f'\n Lotes aprovados com alto grau de pureza (>=98%): {lista_lotes_aprovados}')