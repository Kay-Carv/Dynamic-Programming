# Dynamic Problem                    27/02/2026
#

# Interação VS Recursão
# Memoização

"""
INTERAÇÃO - Percorre todos os valores de n em sequência
Geralmente mais eficiente em memória (evita criar mutiplos stackes de memória)

RECURSÃO
Recursão pode ser mais elegante para problemas naturalmente divisíveis

MEMOIZAÇÃO
Diferente da recursão pura, a memoização consegue armazenar os resultados das etapas
de tal forma que usa como ponto de referência para melhoria da performance de código

"""

# %%
def fatorial_it(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

print(fatorial_it(6))                   # Output: 720

def fatorial_rec(n):
    if n == 1:
        return 1
    return n * fatorial_rec(n - 1)

print(fatorial_rec(6))                  # Output: 720

# %%
# INVERTER STRING

# Nesse caso temos dois exemplos no qual cada um tem performances e qtd de etapas diferentes
#nesse cenário a interação leva vantagens por ter menos etapas e ser mais rápido
def inverter_it(s):
    """Inverter str com recursão"""
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

print(inverter_it("python"))                # output: nohtyp

def inverter_rec(s):
    """Inverter str com recursão"""
    # Caso base: string vazia ou 1 caractere
    if len(s) <= 1:
        return s
    # Passo recursivo: inverte o resto + primeiro caractere
    return inverter_rec(s[1:]) + s[0]
#Teste
print(inverter_rec("fiap"))                 # ouput: paif


###########################
"""EXEMPLOS DE MEMOIZAÇÃO"""
###########################

# Finonacci com Memoização
def fibo(n, memo={}):           # memo = espaço cash da memória
    if n in memo:           # O caso base verifica se o resultado do calculo de N já foi realizado
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]

print(fibo(5))                  #output: 5


########################
# Fatorial com memoização

#%time
def fatorial_memo(n, memo=None):
    """Fatorial utilizando memoização"""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 1:
        return 1

    memo[n] = n * fatorial_memo(n-1, memo)
    return memo[n]

print(fatorial_memo(5))                     #output: CPU times: total: 0 ns
                                            #        Wall time: 3.1 μs
                                            #        120
