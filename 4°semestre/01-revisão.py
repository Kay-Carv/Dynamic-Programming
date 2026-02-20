# AULA - 2 ___ Funções com Recursão vs Repetição     20/02/2026
# 


# %%

# Recursão sendo mais rápida, porém ocupa espaço na memória
def fatorial_rec(n):
    if n == 1:
        return 1
    return n * (fatorial_rec(n - 1))

fatorial_rec(5)

# Função sem recursão é mais rápida
def fatorial_it(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

fatorial_it(5)
# %%

# Exercício - contagem regressiva(pilha LIFO)

def contagem_regressiva_loop(n):
    while n > 0:
        print(n)
        n -=1

print(f"Contagem regressiva com estrutura de repetição: ")
contagem_regressiva_loop(5)

# 

def contagem_recursão(n):
    if n == 0:
        return
    print(n)
    contagem_recursão(n - 1)

print(f"\nContagem regressiva com recursão")
contagem_recursão(5)


# %% Soma linear

def soma_loop(n):
    """Soma linear com laço de repetição"""
    total = 0

    while n > 0:
        total += n
        n -= 1
    
    return total

soma_loop(10)

def soma_loop_for(n):
    """Soma linear com estrutura de repetição FOR"""
    total = 0

    for i in range(1, n + 1):
        total += i
    return total

soma_loop_for(10)

def soma_recursao(n):
    """Soma linear com recursão"""
    if n == 0:
        return 0
    return n + soma_recursao(n - 1)

soma_recursao(5)

# %%

# Estrutura de repetição para dataframes

# Estrutura de repetição com recursão df
import pandas as pd

df = pd.DataFrame({"Valor":[10, 5, 2, 7]})

def soma_acum_recursao(values, i):
    if i == 0:
        return values[0]
    return soma_acum_recursao(values, i-1) + values[i]

vals = df['Valor'].to_list()

df['soma_resultado'] = [soma_acum_recursao(vals, i) for i in range(len(vals))]

print(df)

# %%

