import os
import csv
import time
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome:str
    cpf:str
    cargo:str
    salario:float

def exibindo_dados(self):
    print(
        f"Nome: {self.nome}\n"
        f"CPF: {self.cpf}\n"
        f"Cargo: {self.cargo}\n"
        f"Salário: {self.salario}\n")
    
lista_funcionarios = []

# Exibindo Menu
def exibir_menu():
     print("""
== Sistema de Cadastro de Funcionários ==
          - DENDÊ TECH -
    \n    1 - Cadastrar funcionário
    2 - Listar funcionários
    3 - Atualizar funcionário
    4 - Excluir funcionário
    5 - Salvar dados
    6 - Carregar dados
    7 - Sair
""")

# Função para cadastrar funcionários   
def cadastrar_funcionario():
    nome = input("\nNome: ")
    cpf = input("CPF: ")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))
    lista_funcionarios.append(Funcionario(nome, cpf, cargo, salario))
    print("\nFuncionário cadastrado com sucesso!")

# Função para listar todos os funcionários
def listar_funcionarios():
    if not lista_funcionarios:
        print("\nNenhum funcionário cadastrado.")
        return
    print("\n=== Lista de Funcionários ===")
    for i, funcionario_1 in enumerate(lista_funcionarios, start=1):
        print(f"{i}º: {funcionario_1}")

# Função para atualizar dados de um funcionário
def atualizar_funcionario():
    nome = input("Digite o nome do funcionário a ser atualizado: ")
    for funcionario_1 in lista_funcionarios:
        if funcionario_1.nome == nome:
            funcionario_1.cpf = input(f"Novo cpf: ") or funcionario_1.cpf
            funcionario_1.cargo = input(f"Novo cargo: ") or funcionario_1.cargo
            novo_salario = input(f"Novo salário: ")
            if novo_salario:
                funcionario_1.salario = float(novo_salario)
                print("\nDados do funcionário atualizado com sucesso!")
            return
    print("\nFuncionário não encontrado.")

# Função para excluir um funcionário
def excluir_funcionario():
    nome = input("Digite o nome do funcionário a ser excluído: ")
    for funcionario_1 in lista_funcionarios:
        if funcionario_1.nome == nome:
            lista_funcionarios.remove(funcionario_1)
            print("\nFuncionário removido com sucesso!")
            return
    print("\nFuncionário não encontrado.")

# Função para salvar dados em um arquivo CSV
def salvar_dados():
    try:
        with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Nome', 'CPF', 'Cargo', 'Salario'])
            for func in lista_funcionarios:
                writer.writerow([func.nome, func.cpf, func.cargo, func.salario])
        print("Dados salvos com sucesso em 'funcionarios.csv'.")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

# Função para carregar dados de um arquivo CSV
def carregar_dados():
    if not os.path.exists('funcionarios.csv'):
        return
    try:
        with open('funcionarios.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            lista_funcionarios.clear()
            for row in reader:
                lista_funcionarios.append(Funcionario(row['Nome'], row['CPF'], row['Cargo'], row['Salario']))
        print("\nDados carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

# Função final
def main():
    carregar_dados()
    while True:
        exibir_menu()
        opcao = input("Escolha uma das opções: ")
        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            listar_funcionarios()
            time.sleep(10)
        elif opcao == '3':
            atualizar_funcionario()
        elif opcao == '4':
            excluir_funcionario()
        elif opcao == '5':
            salvar_dados()
        elif opcao == '6':
            carregar_dados()
        elif opcao == '7':
            if lista_funcionarios: # Sugere salvar se houver dados
                 # Poderia adicionar uma verificação mais sofisticada de "dados alterados"
                salvar_ao_sair = input("\nDeseja salvar os dados antes de sair? (S/N): ").strip().lower()
                if salvar_ao_sair == 's':
                    salvar_dados()
            print("\nEncerrando programa")
            break
        else:
            print("\nOpção inválida.\nTente novamente.")
        input("Aperte enter para continuar...")
        os.system("cls || clear")

if __name__ == '__main__':
    main()