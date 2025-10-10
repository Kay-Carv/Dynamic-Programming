""" Recursão
Programação Dinâmica                        10/10/2025

"""

# %% Ex: 1 - Fatorial usando recursão

"""
Um exemplo com uma lógica muito boa é usar o para calcular um fatorial
"""

# Exemplo de resultado
def fatorial(n):
    if n == 0:
        return 1
    
    # Passo da recursão
    return n * fatorial(n - 1)

num_fatorial = 4
print(f"O fatorial de {num_fatorial} é igual a: {fatorial(num_fatorial)}")

# Nesse caso a função cria um espaço na memória para cada novo (n - 1), ou seja, enquanto ela for diferente do caso base de if = 0 a função
#irá criar espaços na memória onde
# 1° passo: n = 5
# 2° passo: n = 4
# 3° passo: n = 3
# 4° passo: n = 2
# 5° passo: n = 1
# 6° passo = irá mutiplicar todas as variáveis criadas de N em sequência (LIFO)

# OBS: Algo muito interessante para ver esse processo é usar o python tutor


# %% Ex 2 fatorial com repetição

# Nesse caso a estrutura de repetição chega a ser mais rápido do que a recursiva pura 

def fatorial_it(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i

    return resultado

fatorial_it(5)  # Output -> 120

# %% Ex3: Estrutura de árvore binária

def merge_sort(arr):
    if len(arr) <= 1:       # Caso base se isso for verdade ele ira retornar a lista base para iniciar o calculo com ela, nesse caso seriam os array únicos que a gente separou com o meio da lista
        return arr
    
    meio = len(arr) //2
    esquerda = merge_sort(arr[:meio])   # Estrutura de função recursiva
    direita = merge_sort(arr[meio:])    # Onde ela vair ser responsável por tranformar a array com vários termos em uma array única

    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    return resultado + esquerda[i:] + direita[j:]

lista = [5, 3, 8, 4, 2]                       # Temos assim a lista organizada a partir da árvore binária
print("Resultado final: ", merge_sort(lista)) #Output => Resultado final:  [2, 3, 4, 5, 8]  
# %%
