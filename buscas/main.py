#   PROGRAMAÇÃO DINÂMICA

"""Tema: BUSCA BINÁRIA"""

# Ter um algoritimo de busca eficiente = PRIMEIRO ordene o array (lista)

# É preciso definir um alvo
# Geralmente temos um valor "low" e um "high" onde a gente incrementa ou decrementa em um dos dois para que o alvo fique mais próximo de "low" e "high"
# E nesse low e high separamos uma lista em 2 e sempre em 2 (por isso o nome binário)
# <--1, 2, 3||low|  middle  |high|| 800, 801, 802-->

# Pegando através do index
# lista = [1, 2, 3, 4, 5, 6, 7, 8]
# mid = left  + (low - left)/2    ou   meio = (inicio + fim) // 2
# = 0+ (7-0)/2
# = 3,5
# = INDEX 3

"""===ORDENANDO LISTAS==="""

lista1 = [ 5, 6 , 3 ,4 ,2]

"""Organiza a lista"""
lista1.sort() # reverse=True para inverter a ordem
print(lista1)       #[2, 3, 4, 5, 6]

lista1.sort(reverse=True)

"""Sorted ordena a lista tendo a possibilidade de criar uma variável nova"""
lista = [5, 2, 6, 5 ,6]
listaOrdenada = sorted(lista)
print(listaOrdenada)            # [2, 3, 4, 5, 6]

listaOrdenadaRev = sorted(lista, reverse=True)
print(listaOrdenadaRev)     # [6, 6, 5, 5, 2]

"""Prâmetro key = lambda"""
lista = [("string", 2, 4), ("Kayque", 6, 2), ("Joao", 4, 1), ("user", 1, 10)]
listaOrdenada = sorted(lista, key=lambda X: X[-1]) # Utilizando uma variável X pelo indice "1"  para organizar a lista baseandosse nos números
print(listaOrdenada) 
#output = [('Kayque', 6, 2), ('string', 2, 4), ('Joao', 4), ('user', 1, 10)]
# %%

"""Ex: BUSCA BINÁRIA"""
def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        meio_valor = lista[meio]

        if meio_valor == item:
            return meio  # Elemento encontrado, retorna o índice
        elif item < meio_valor:
            fim = meio - 1  # Busca na metade esquerda
        else:
            inicio = meio + 1  # Busca na metade direita

    return "Elemento não encontrado", -1  # Elemento não encontrado


# %%
lista = [1, 2, 3, 4, 5, 6, 7]

ordena = []
i = 0

for i in range(50):
    i = i + 1
    ordena.append(i)

#print(ordena)

busca_binaria(lista, 9)         # Output: ('Elemento não encontrado', -1)
busca_binaria(ordena, 30)       # Output:  29...Isso porque temos uma lista ordenada 1 até 50


# %%
"""
Você está trabalhando no sistema de um grande e-commerce. Uma das tarefas mais comuns é verificar rapidamente se um produto,
 identificado por um código numérico único (SKU), está disponível no inventário do depósito.

O inventário do depósito é uma lista gigante de códigos de produtos (SKUs), que já está ordenada numericamente.
 Para otimizar o sistema e evitar lentidão, você não pode percorrer a lista item por item (busca linear), pois isso seria muito demorado com milhões de produtos.

Sua tarefa é criar uma função chamada verificar_estoque(inventario, sku_produto) que receba a lista de SKUs do 
inventário e o código do produto que você deseja encontrar.

1.A função deve implementar o algoritmo de busca binária.
2.Se o sku_produto for encontrado na lista inventario, a função deve retornar o índice (a posição) onde ele foi encontrado.
3.Se o sku_produto não estiver no inventário, retorne uma mensagem
"""


# Lista de SKUs de produtos em estoque
inventario_deposito = [
    1001, 1005, 1540, 1203,  1877, 2010, 2345, 2890, 3012, 3050,
    3110, 3115, 3498, 4040, 4567, 4899, 5001, 5023, 5555, 6789,
    7123, 7543, 8008, 8134, 8888, 9010, 9123, 9999, 10000
]

def verificar_estoque(lista_sku, item):
    lista_sku.sort()    # Ordena a lista
    inicio = 0
    fim = len(lista_sku)-1

    while inicio <= fim:
        meio = (inicio + fim) //2
        meio_valor = lista_sku[meio]

        if meio_valor == item:
            return meio  # Elemento encontrado, retorna o índice
        elif item < meio_valor:
            fim = meio - 1  # Busca na metade esquerda
        else:
            inicio = meio + 1  # Busca na metade direita

    return "Nenhum protudo foi encontrado"


print(verificar_estoque(inventario_deposito, 1540))    #output: 3

print(verificar_estoque(inventario_deposito, 5000))    #output: Nenhum protudo foi encontrado

print(verificar_estoque(inventario_deposito, 1001))    #output: 0

print(verificar_estoque(inventario_deposito, 9999))    #output: 27

print(len(inventario_deposito))    #output: 29
# %%
