""" 12/10/2025

Fazendo um teste com um código sobre o triângulo de floyd que eu vi no instagram e estou tentando aplicar programação dinâmica nele

Ex do código:
rows = 4
num = 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

"""

def floyds_triangle_dp(rows):
    # Cria uma tabela (lista de listas) para armazenar os resultados
    dp = [[] for _ in range(rows)]  # Cria primeira tabela já com a quantidade exata de colunas que teremos {if rows = 7 significa que teremos 7 colunas a serem prenchidas}
    print(f"Primeira tabela {dp}")

    num = 1

    print("\nVerificar passo a passo da tabela___:")
    for i in range(rows):
        # Calcula cada linha com base nos resultados anteriores
        for j in range(i + 1):
            dp[i].append(num)
            num += 1
            print(dp)

    # Exibe o triângulo armazenado
    for row in dp:
        print(*row) # Asteristico (*) serve para pegar cada elemento da lista sem printar [4, 5, 6] mas sim printar 4 5 6

floyds_triangle_dp(8)


# Output
# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36
# 37 38 39 40 41 42 43 44 45
# 46 47 48 49 50 51 52 53 54 55
# 56 57 58 59 60 61 62 63 64 65 66
# 67 68 69 70 71 72 73 74 75 76 77 78
# 79 80 81 82 83 84 85 86 87 88 89 90 91



"""Tentando replicar a lógica de cabeça"""
def triangulo_floyd(linhas):
    dp = [[] for _ in range(linhas)]

    num = 1

    for i in range(linhas):
        for j in range(i + 1): # Eu errei aqui no range tinha posto como range(num), mas o resto da lógica eu acertei
            dp[i].append(num)
            num += 1

    for linhas in dp:
        print(*linhas)

triangulo_floyd(0)



# Usando Memoização no processo, Foi usado outra lógica
from functools import lru_cache

print("\n\nUsando Memoização: \n")
# Função que calcula o número na posição (i, j) usando fórmula matemática
@lru_cache(maxsize=None)
def floyd_number(i, j):
    """
    Retorna o número na posição (i, j) do Triângulo de Floyd.
    A memoização garante que cálculos repetidos sejam armazenados em cache.
    """
    start = (i - 1) * i // 2 + 1
    return start + (j - 1)


def floyds_triangle(rows):
    """
    Imprime o Triângulo de Floyd até 'rows' linhas,
    reutilizando resultados armazenados pela memoização.
    """
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(floyd_number(i, j), end=" ")
        print()


# Exemplo de uso
rows = 4
floyds_triangle(rows)
