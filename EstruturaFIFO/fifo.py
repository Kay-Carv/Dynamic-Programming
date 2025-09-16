#%% Aula
# 
"""Exercício com FIFo (First In First Out)"""

fila = [ "Cliente 1", "Cliente 2", "Cliente 3"]
print(fila)

cliente = fila.pop(0)
print(cliente)
fila = []

# %%
"""Exemplo 2 - Utilizando While"""

fila = [ "Cliente 1", "Cliente 2", "Cliente 3"]

while(fila):
    cliente = fila.pop(0)
    print(f"Atendendo {cliente}")
# %%
"""Exemplo 3 - Utilizando for"""

fila = [ "Cliente 1", "Cliente 2", "Cliente 3"]

i = 0

for i in range(len(fila)):
    cliente = fila.pop(0)
    print(f"Cliente atendido {cliente}")        # Output
                                                # Cliente atendido Cliente 1
                                                # Cliente atendido Cliente 2
                                                # Cliente atendido Cliente 3
    

# %%

    # """
    #     Exercício 1 - Uma loja tem um sistema de atendimento por ordem de chegada. Os clientes entram
    # na fila e são atendidos na mesma ordem.
    
    # - Por nome dos clientes e adicione a fila
    # - Atenda os clientes na ordem de chegada
    # - Após atender todos os clientes, exiba "Todos foram atendidos"
    # """
    
lista_cliente = []

for i in range(3):
    cliente = input(f"Digite o nome do {i + 1}° para entrar na fila ")
    lista_cliente.append(cliente)

print("---Atendendo clientes---")
while lista_cliente:                    # Acho que nesse casos é mais interessante usar while para esvaziar um fila
    proximoFila = lista_cliente.pop(0)
    print(f"Próximo cliente:  {proximoFila}")    

print("Todos os clientes foram atendidos")
# %%

    # """
    #     Exemplo 5 - Crie um programa que solicite três informações: Nome, idade e especialidade 10 vezes.
    #     Em seguida, crie uma estrutura para inserir o custo da consulta, em função da especialidade. Por fim, crie
    # um estrutura para retirar as informações dos clientes por ordem de prioridade.
    
    # Especialidades
    
    # Clinico geral - 500,00
    # Dermatologista - 600,00
    # cardiologista - 800,00
    # Ortopedista - 550,00
    
   # """
    
fila_consulta = []

for i in range(2):
    print(f"\n--- {i + 1}º Cliente ---")
    nome = input(f"Digite o nome: ")
    idade = int(input("Idade: "))
    print("1- Clinico geral\n2- Dermatologista\n3- Cardiologista\n4- Ortopedista")
    especialidade = int(input("Selecione a especialidade (1-4): "))
    dados_cliente = [nome, idade, especialidade]
    fila_consulta.append(dados_cliente)
    
print(fila_consulta)

fila_atendimento = []
for cliente in fila_consulta:
    custo = 0
    especialidade_nome = ""
    match cliente[2]:
        case 1:
            custo = 500
            especialidade_nome = "Clinico geral"
        case 2:
            custo = 600
            especialidade_nome = "Dermatologista"
        case 3:
            custo = 800
            especialidade_nome = "Cardiologista"
        case 4:
            custo = 550
            especialidade_nome = "Ortopedista"
        case _:
            custo = 0
            especialidade_nome = "Especialidade não encontrada"
            
    fila_atendimento.append([cliente[0], cliente[1], especialidade_nome, custo])

print("--- Fila a ser atendida ---\n")
print(fila_atendimento)


print("\n---Ordem de atendimento---")
ordem_fila = 0
while fila_atendimento:
    cliente_atendido = fila_atendimento.pop(0)
    print(f"{ordem_fila + 1}.\tCliente {cliente_atendido[0]}, Idade: {cliente_atendido[1]}, Especilidade: {cliente_atendido[2]}, Custo: R${cliente_atendido[3]:.2f} ")
    ordem_fila += 1

print("Todos os clientes da fila foram atendidos")
# %%
"""Exercício feito pelo professor

    Utilizando Dicionário
"""
lista_clientes = {
    "nome" : [],
    "idade": [],
    "especialidade": [],
    "custo": []
}

for i in range(3):
    nome = input("Insira o nome: ")
    idade = int(input("Digite a idade: "))
    especialidade = (input("Digite especialidade")).lower()

    if especialidade == 'clinico geral':
        custo = 500
    elif especialidade == 'dermatologista':
        custo = 600
    elif especialidade == 'cardiologista':
        custo = 800
    elif especialidade == 'ortopedista':
        custo = 550
    else:
        custo = 0
        print("especialidade não existe!")
        
    lista_clientes['nome'].append(nome)
    lista_clientes['idade'].append(idade)
    lista_clientes['especialidade'].append(especialidade)
    lista_clientes['custo'].append(custo)


print("---Fila dos clientes")
i = 0
while lista_clientes['nome']:
    nome = lista_clientes['nome'].pop(0)
    idade = lista_clientes['idade'].pop(0)
    especialidade = lista_clientes['especialidade'].pop(0)
    custo = lista_clientes['custo'].pop(0)
    
    print(f'{i + 1}.Nome: {nome} \nIdade:{idade} \nEspecialidade:{especialidade} \nR${custo}')
    i += 1

# %%

"""
    Exemplo 6. Utilizando lambda

"""

lista_clientes = {
    "nome" : [],
    "idade": [],
    "especialidade": [],
    "custo": []
}

calcular_custo = lambda custo: (
    500 if custo == "clinico geral" else
    600 if custo == "dermatologista" else
    800 if custo == "cardiologista" else
    550 if custo == "ortopedista" else
    0
)

for i in range(3):
    print(f"---{i + 1}° cliente")
    nome = input("Insira o nome: ")
    idade = int(input("Digite a idade: "))
    especialidade = input("Digite especialidade: ").lower()
    
    custo = calcular_custo(especialidade)    # custo depende da especialidade

    lista_clientes['nome'].append(nome)
    lista_clientes['idade'].append(idade)
    lista_clientes['especialidade'].append(especialidade)
    lista_clientes['custo'].append(custo)
    
# Inclua a função para atender os clientes
print(lista_clientes)                       # Output
                                            # {'nome': ['Ana', 'Rafael', 'Beatriz'], 'idade': [19, 34, 45], 'especialidade': ['dermatologista', 'clinico geral', 'cardiologista'], 'custo': [600, 500, 800]}


print("\n--- Atendendo a Fila ---")
while lista_clientes['nome']:
    nome = lista_clientes['nome'].pop(0)
    idade = lista_clientes['idade'].pop(0)
    especialidade = lista_clientes['especialidade'].pop(0)
    custo = lista_clientes['custo'].pop(0)
    
    print(f"Atendendo: {nome} (Idade: {idade}) | Especialidade: {especialidade.capitalize()} | Custo: R${custo:.2f}")

print("\nFila de atendimento finalizada.")  # Output
                                            # Atendendo: Ana (Idade: 19) | Especialidade: Dermatologista | Custo: R$600.00
                                            # Atendendo: Rafael (Idade: 34) | Especialidade: Clinico geral | Custo: R$500.00
                                            # Atendendo: Beatriz (Idade: 45) | Especialidade: Cardiologista | Custo: R$800.00


# %%

"""Exercício 7: Sistema de Atendimento de Pedidos (FIFO)
Desenvolva um sistema para um restaurante que gerencia a fila de pedidos. Os pedidos devem ser atendidos na ordem em que foram feitos.

a) Crie um menu interativo com as seguintes opções:

Adicionar um novo pedido

Atender o próximo pedido

Exibir a fila de pedidos

Sair
b) Use uma estrutura de dados de fila (lista) para armazenar os pedidos.
c) Implemente a lógica para que, ao atender um pedido, o programa remova o primeiro item da fila. Certifique-se de que o sistema avise 
quando a fila estiver vazia."""

print("---Sistema de gerenciamento de fila de pedidos---")

lista_pedidos = []
qtd_pedido = 0

while True:
    print("\nSelecione uma opção (1 - 4)" \
    "\n1 - Adicionar um novo pedido" \
    "\n2 - Atender o próximo pedido" \
    "\n3 - Exibir a fila de pedidos" \
    "\n4 - Sair")

    opcao = input("Escreva uma opção: ").lower()

    if opcao == '1' or opcao == "adicionar um novo pedido":
        pedido = input("Escreva o pedido")
        lista_pedidos.append(pedido)
        print(f"O pedido {pedido} foi adicionado! ")

    elif opcao == "2" or opcao == "atender o próximo pedido":
        if lista_pedidos:
            pedido_atendido = lista_pedidos.pop(0)
            qtd_pedido += 1
            print(f"O {qtd_pedido}° pedido de ({pedido_atendido}) foi atendido!")
        else:
            print("Não temos pedidos")
    
    elif opcao == "3" or opcao == "exibir a fila de pedidos" :
        print("---Lista de pedidos---")
        for i, elemento in enumerate(lista_pedidos):
            print(f"{1}. {elemento}")

    elif opcao == "sair" or opcao == "4":
        print(f"\nForam atendidos um total de {qtd_pedido} pedidos durante o expediente: ")
        print("Encerrando o sistema")
        break

    else:
        print("Opção inválida")