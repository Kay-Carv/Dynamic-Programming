"""
Aula 5 - Algoritmo de Dijkstra                             13/03/2026
Ontem recebi um convite para entrevista na Credsystem estou confiante
====================================================


Algoritmo de Dijkstra - Algoritmo para melhor rota, caminho, etc...

 Aqui utilizamos grafos com dicionário formando um conjunto de vértices não visitados e
suas respectivas distâncias até o vértice de origem

Pensando no grafo em que esse algortimo resolve, sempre teremos 2 caminhos onde ele busca o menor caminho
caso partirmos de um ponto A temos 2 vertices (2 e 3) onde cada uma tem um custo de distância, logo calculamos uma rota
baseada em menor custo e conforme mais caminhos temos mais possíveis rotas é criadas

APLICANDO DIJSTRA

Rotamento em redes de Computadores - Usamos para melhor rota em traféco de rede, pacotes de dados
Navegação de Mapas - Menor distância ou menor tempo (considemos apenas uma coisa por vez)
Análise de Redes Sociais - Amigos em comum

IDEIA DO ALGORTMO
1. Começamos pelo o poto inicial de valor 0
2. Todos começam ocm infinito 
3. Escolha sempre o próximo menor caminho
4. Atualiza a distância conforme avança
5. Marcamos o "nó" visitado
6. Repartimos os caminhos para encontrar o mais eficiente

Consideramos todos os pontos para achar o menor caminho

No caso desse algoritmo por analizarmos literalmente TUDO sempre te retorna o melhor resultado sendo um recurso ÓTIMO                
"""

grafo = {
    'Casa'      :   { 'Cruzamento1': 2, 'Cruzamento2':5},
    'Cruzamento1':  {'Hospital': 4, 'Cruzamento3':2},
    'Cruzamento2':  {'Cruzamento3': 1},
    'Cruzamento3':  { 'Cruzamento1': 2, 'Hospital': 3},
    'Hospital':     {}
}

"Machine Learning: Clusterização, separação dos dados, camada oculta, regressão, Classificação, rede neural"
