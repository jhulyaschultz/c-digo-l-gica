import os 
from dataclasses import dataclass
os.system("clear")

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    cpf: str
    funcao: str

    def exibir_dados(self):
        print("\n--- Dados do Funcionário ---")
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"CPF: {self.cpf}")
        print(f"Função: {self.funcao}")

# Função para exibir o menu e interagir com o usuário
def menu():
    funcionarios = []
    while True:
        print("\nMenu de Opções:")
        print("1 - Cadastrar Funcionário")
        print("2 - Exibir Funcionários")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do funcionário: ")
            data_nascimento = input("Digite a data de nascimento: ")
            cpf = input("Digite o CPF: ")
            funcao = input("Digite a função: ")

            funcionario = Funcionario(nome, data_nascimento, cpf, funcao)
            funcionarios.append(funcionario)
            print("Funcionário cadastrado com sucesso!")

        elif opcao == "2":
            if funcionarios:
                for i in funcionarios:
                    i.exibir_dados()
            else:
                print("Nenhum funcionário cadastrado.")

        elif opcao == "3":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()
