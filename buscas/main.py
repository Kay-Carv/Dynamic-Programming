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