
# %%

""" CP1 Dynamic Programming             29/08/2025

Exercícios de busca linear
Altenativas de buscas binárias e linear

"""


# %%
"""
Ex.1

Utilize a busca linear escreva uma função em Python que retorna duas listas:
- Uma lista com os códigos dos equipamentos que têm status pendente.
- Uma lista com os códigos dos equipamentos que têm status concluído.

codigos_equipamentos = [101, 102, 103, 104, 105, 106, 107, 108]status_manutencao = [0, 1, 0, 1, 0, 1, 1, 0]

Sendo: 0 = pendente, 1 = concluído
"""

# Listas de equipamentos e número de status
codigos_equipamentos = [101, 102, 103, 104, 105, 106, 107, 108]

status_manutencao = [0, 1, 0, 1, 0, 1, 1, 0]

# Função para segregar status e equipamento
def status_equipamento(lista_equipamentos, lista_status):
    status_concluido = []
    status_pendende = []

    # Estrutura de looping for e condição
    for i in range(len(lista_status)):
        if lista_status[i] == 1:
            status_concluido.append(lista_equipamentos[i])
        else:
            status_pendende.append(lista_equipamentos[i])
        
    return status_concluido, status_pendende

concluido, pendente = status_equipamento(codigos_equipamentos, status_manutencao)

print(f"Os códigos dos equipamentos concluídos são: {concluido}")
print(f"Os códigos de equipamentos ainda pendentes são: {pendente}")



# %%

"""Em uma linha de produção, cada produto tem um número de série, e o status de qualidade é armazenado em uma lista separada. 
O objetivo é criar três listas: uma com os produtos aprovados, outra com os produtos reprovados, e outra com produtos pendentes.
Crie uma estrutura com input para o usuário a qual seja possível o usuário inserir 10 números de série e os respectivos status de qualidade para cada número de série.

Exemplo para número de série = 1001, 1002, 1003....Exemplo para status = aprovado, reprova, pendente,..., 
Sendo 1 = aprovado, 0 = reprovado, -1 = pendente."""

sku_produto = []
status_sku = []

print("=== Programa para verificar o status de um produto ===\n")

# Estrutura de Input do usuário 
for i in range(1):
    sku = int(input(f"Digite o número de série do {i + 1}° produto:"))
    sku_produto.append(sku)
    status = int(input(f"Digite um número de status para o {i + 1}° produto sendo: 1 = aprovado, 0 = reprovado, -1 = pendente "))
    status_sku.append(status)

# Função para separar definir status do produto
def definir_produtos(sku_produto, num_status):
    """Função de produtos função server para essas coisas"""
    produtos_aprovados = []
    produtos_reprovados = []
    produtos_pendente = []

    # Estrutura de condição para verificar status
    for i in range(len(sku_produto)):
        if num_status[i] == 1:
            produtos_aprovados.append(sku_produto[i])
        elif num_status[i] == 0:
            produtos_reprovados.append(sku_produto[i])
        elif num_status[i] == -1:
            produtos_pendente.append(sku_produto[i])

    return produtos_aprovados, produtos_reprovados, produtos_reprovados

# Chamando função
lista_aprovados, lista_reprovados, lista_pendentes = definir_produtos(sku_produto, status_sku)

# Output
print("=== Lista dos códigos separados por status ===")
print(f"\nTemos um total de {len(lista_aprovados)} códigos com os produtos aprovados, são eles: {lista_aprovados}")
print(f"Temos um total de {len(lista_reprovados)} códigos com os produtos, são ele(s): {lista_reprovados}")
print(f"Temos um total de {len(lista_aprovados)} códigos com os produtos ainda pendentes, são ele(s): {lista_pendentes}")