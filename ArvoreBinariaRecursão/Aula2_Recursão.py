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


# %%
