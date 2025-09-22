''' Revisão sobre estruturas com filas e pilhas:
duas listas = alta e baixa
estrutura de repetição infinita (while True)
solicita as duas variáveis (documento e prioridade)
primeira estrutura de condição (1. adicionar documento)
incluir a estrutura para enviar os documentos com alta e baixa prioridade para as listas
segunda estrutura de condição (imprimir os documentos seguindo as estruturas FIFO ( pop(0) )
terceira estrutura de condição (parar estrutura de repetição infinita) '''
# %% 
# Ex. 1
# Resolução do exercício da aula anterior

fila_alta = []
fila_baixa = []
while True:
    print("Selecione uma opção (1-3): ")
    opcao = input("1. Adicionar Documenteo\n2. Imprimir documento \n3. Sair da estrutura\n")

    if opcao == "1":
        tipo = input("Digite um ducumento: ")
        prioridade = input("Digite a prioridade ( alta e baixa )")

        if prioridade == "alta":
            fila_alta.append(tipo)
        else:
            fila_baixa.append(tipo)

    elif opcao == "2":
        if fila_alta:
            print(f"Imprimindo fila alta: \n{fila_alta.pop(0)}")
        elif fila_baixa:
            print(f"Imprimindo fila baixa: \n{fila_baixa.pop(0)}")
        else:
            print("Nenhum documento na fila")

    elif opcao == '3':
        break

# %%

"""
Um hospital recebe pacientes e os coloca em uma filla de atendimento. Cada paciente tem um nível de urgência que varia de 1 (menos urgênte) e
5 (mais urgente).


Exercício: Crie um programa que adicione pacientes à fila e atenda primeiro aqueles em maior nível de urgência. Se houver empate, siga ordem de chegada 
"""
fila = []

while True:
    print("Selecione uma opção (1-3): ")
    opcao = input("1. Adicionar Paciente\n2. Atender todos os pacientes \n3. Sair da estrutura\n")

    if opcao == "1":
        qtd_pacientes = int(input("Digite a quantidade de pacientes a serem atendidos"))
        for i in range(qtd_pacientes):
            paciente = []
            nome_paciente = input(f"Digite o {len(fila) + 1}° paciente a entrar na fila: ")
            prioridade = input("Digite a prioridade entre 1 (menos urgente) e 2 (mais urgente) do paciente: ")
            ordem_chegada = len(fila)

            paciente.append(nome_paciente)
            paciente.append(ordem_chegada)
            paciente.append(prioridade)
            fila.append(paciente)

        ordem_atendimento.sort(reverse=True)
        ordem_atendimento = sorted(fila, key=lambda X: (X[-1], X[1]))
        
    elif opcao == "2":
        print("Atendendo fila")
        print(f"Fila atual {ordem_atendimento}")
        
        while ordem_atendimento:
            proximo_paciente, ordem_chegada ,proxima_prioridade = ordem_atendimento.pop()

            print(f"Atendendo paciente: {proximo_paciente} com prioridade de: {proxima_prioridade}")

    elif opcao == '3':
        break

# %%

"""Melhorando o último código"""

fila = []

while True:
    print("\nSelecione uma opção (1-3): ")
    opcao = input("1. Adicionar Paciente\n2. Atender todos os pacientes \n3. Sair\n")

    if opcao == "1":
        nome_paciente = input("Digite o nome do paciente: ")
        
        # Validação de prioridade válida
        while True:
            prioridade_str = input("Digite a prioridade (1-5): ")
            if prioridade_str.isdigit():
                prioridade = int(prioridade_str)
                if 1 <= prioridade <= 5:
                    break
            print("Prioridade inválida. Por favor, digite um número entre 1 e 5.")
        
        ordem_chegada = len(fila)
        
        paciente = [nome_paciente, prioridade, ordem_chegada]
        fila.append(paciente)
        print(f"Paciente '{nome_paciente}' adicionado à fila com prioridade {prioridade}.\n")

    elif opcao == "2":
        if not fila:
            print("Não há pacientes na fila para atender.")
            continue
        
        print("\n--- ATENDENDO A FILA ---")

        # ORdenando a lista com os mesmos critérios porém com listas
        # [1] prioridade, [2] ordem de chegada
        fila_atendimento = sorted(fila, key=lambda p: (-p[1], p[2]))
        
        # Atender o paciente
        while fila_atendimento:
            proximo_paciente = fila_atendimento.pop(0)
            nome, prioridade, _ = proximo_paciente
            print(f"Atendendo paciente: '{nome}' (Prioridade: {prioridade})")
            
        fila.clear() # limpar a fila para parar de bugar
        print("\nTodos os pacientes foram atendidos. A fila está vazia.")

    elif opcao == '3':
        print("\n===Saindo do programa===")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
# %%


# Repertório: 
# Python é ótimo para: Ciência de dados e construções de modelos

# AWS Academy = Da acesso a todos os cursos da AWS onde disponibiliza a teoria e os labs para ferramentas para conseguir se certificar
