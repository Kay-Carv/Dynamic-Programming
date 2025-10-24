
# Ex 1 - Recursão para o problema de Fatorial

# Utilizando estrutura de repetição

def fatorial_repeticao(arr):
    resultado = 1
    for i in range(1, 1+ arr):
        resultado *= i
    return resultado

# print(fatorial_repeticao(9))

# Utilizando estrutura de recursão
def fatorial_recursao(n):
    if n == 0:
        return 1
    
    return n * fatorial_recursao(n - 1)


# print(fatorial_recursao(9)) 

"""A ideia da utilização de recursão ao invés de estrutura de repetição é para trazer mais eficiência"""

#########################################################################

# def recursao(n):
#     if n == 0:
#         return 1
#     return n * recursao(n - 1)

# print(recursao(999))            # OUTOUT: "RecursionError: maximum recursion depth exceeded"
# Nesse caso temos um problema de "pilha de stack", onde a função criar vários valores na memório e fazem eles em pilha


#%%
#Exercício - Invert String

# Ex1 - Crie uma função que receba uma string e retorne a string invertida

def string_invertida(s):
    invertida = ''
    for letra in s:
        invertida = letra + invertida

    return invertida

print(string_invertida("abcdef"))   # OUTPUT: fedcba

# Ex2 - Versão recursiva: sem usar métodos prontos como [::-1]

def inversao(s):
    if len(s) <= 1:
        return s                    # inversao(s[1:])  === Retira cada letra/caractere da palavra
    return inversao(s[1:]) + s[0]   # + s[0]

print(inversao("Python"))           # OUTPUT: nohtyP

# Ex3 - Versão iterativa: usando um loop

def inverter_it(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida


print(inverter_it("Engenharia"))
# %%

"""TAREFA PARA CASA

Crie uma estrutura com recursão para o problema de Fibonaci

Verique o tempo de execusão
"""