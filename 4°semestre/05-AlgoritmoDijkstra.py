""" Dynamic Programming -- 10/04/2026


Algoritmo de Dijkstra parte II


"""


grafo_simples = {
    'a':{'b':4, 'c':4},
    'b':{'a':4, 'c':1, 'd':2},
    'c':{'a':3, 'b':5, 'd':1, 'e':3},
    'd':{'b':2, 'c':1},
    'e':{'c':3}
}

grafo = {
    'A':{'B':1, 'C':4},
    'B':{'C':2, 'D':2, 'E':5},
    'C':{'E':1},
    'D':{'E':1},
    'E':{}
}

def dijkistra(grafo, inicio):
    dist = {}
    visitados = []

    #Distância inicial
    for no in grafo:
        dist[no] = float('inf')

    dist[inicio] = 0

    while len(visitados) < len(grafo):
        # Encontrar menor distância não visitada

        menor_no = None

        for no in grafo:
            if no not in visitados:
                if menor_no is None or dist[no] < dist[menor_no]:
                    menor_no = no

        # marcar como visitado
        visitados.append(menor_no)

        # Atualizar
        for vizinho in grafo[menor_no]:
            nova_dist = dist[menor_no] + grafo[menor_no][vizinho]
            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist

    return dist

print(dijkistra(grafo, 'A'))



# %%


"""
De A até F quantos caminhos existem?
"""
# import networkx as nx
# import matplotlib.pyplot as plt

grafo_2 = {
    'A':{'B':5, 'C':2},
    'B':{'A':5,'C':7, 'D':8},
    'C':{'A':2,'B':7,'D':4,'E':8},
    'D':{'B':8, 'C':4,'E':6, 'F':4},
    'E':{'C':8, 'D':6, 'F':3},
    'F':{}
}

# # 2. Criar o objeto Graph do NetworkX
# G = nx.Graph(grafo_2)

# # 3. Definir o layout (posicionamento dos nós)
# pos = nx.spring_layout(G)

# # 4. Desenhar o grafo
# nx.draw(G, pos, with_labels=True, node_color='lightblue', 
#         edge_color='gray', node_size=2000, font_size=15)

# # 5. Exibir o gráfico
# plt.show()



print(dijkistra(grafo_2, 'A'))

# %%
