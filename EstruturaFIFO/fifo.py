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
    print(f"Cliente atendido {cliente}")
    

# %%

    # """
    #     Exercício 1 - Uma loja tem um sistema de atendimento por ordem de chegada. Os clientes entram
    # na fila e são atendidos na mesma ordem.
    
    # - Por nome dos clientes e adicione a fila
    # - Atenda os clientes na ordem de chegada
    # - Após atender todos os clientes, exiba "Todos foram atendidos"
    # """
    
lista_cliente = []

for i in range(10):
    cliente = input(f"Digite o nome do {i + 1}° para entrar na fila ")
    lista_cliente.append(cliente)

for i in range(len(lista_cliente)):
    proximoFila = lista_cliente.pop(0)
    print(f"Próximo cliente:  {proximoFila}")    

# %%

    # """
    #     Exempo 5 - Crie um programa que solicite três informações: Nome, idade e especialidade 10 vezes.
    #     Em seguida, crie uma estrutura para inserir o custo da consulta, em função da especialidade. Por fim, crie
    # um estrutura para retirar as informações dos clientes por ordem de prioridade.
    
    # Especialidades
    
    # Clinico geral - 500,00
    # Dermatologista - 600,00
    # cardiologista - 800,00
    # Ortopedista - 550,00
    
   # """
    
fila_consulta = []
custo = []

for i in range(2):
    print(f"\n--- {i + 1}º Cliente ---")
    nome = input(f"Digite o nome: ")
    idade = int(input("Idade: "))
    epecialidade = int(input("Selecione a especialidade (1-4): "))
    dados_cliente = [nome, idade, epecialidade]
    fila_consulta.append(dados_cliente)
    
print(fila_consulta)

for j in range(len(fila_consulta)):
    match fila_consulta[j][2]:
        case 1:
            custo = 500
            epecialidade = "Clinico geral"
        case 2:
            custo = 600
            epecialidade = "Dermatologista"
        case 3:
            custo = 800
            especialidade = "Cardiologista"
        case 4:
            custo = 550
            especialidade = "Ortopedista"
        case _:
            custo = 0
            epecialidade = "Especialidade não encontrada"
            
    fila_consulta[j].extend([custo, especialidade])

print(fila_consulta)
    
# %%
"""Exercício feito pelo professor

    Utilizando Dicionário
"""
lista_clientes = {
    "nome" : [],
    "idade": [],
    "epecialidade": [],
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
    especialidade = lista_clientes['epecialidade'].pop(0)
    custo = lista_clientes['custo'].pop(0)
    
    print(f'{i + 1}.Nome: {nome} \nIdade:{idade} \nEspecialidade:{especialidade} \nR${custo}')

# %%

"""
    Exemplo 6. Utilizando lambda

"""

lista_cliente = {
    "nome" : [],
    "idade": [],
    "epecialidade": [],
    "custo": []
}

calcular_custo = lambda custos: {
    500 if custo == "clinico geral" else
    600 if custo == "dermatologista" else
    800 if custo == "cardiologista" else
    550 if custo == "ortopedista" else
    0
}

for i in range(3):
    print(f"---{i + 1}° cliente")
    nome = input("Insira o nome: ")
    idade = int(input("Digite a idade: "))
    especialidade = input("Digite especialidade: ").lower()
    
    custo = calcular_custo(epecialidade)    # custo depende da especialidade

    lista_clientes['nome'].append(nome)
    lista_clientes['idade'].append(idade)
    lista_clientes['especialidade'].append(especialidade)
    lista_clientes['custo'].append(custo)
    
# Inclua a função para atender os clientes


# %%
