import os
from dataclasses import dataclass

os.system("clear")  

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str
    estado: str

@dataclass
class ALUNO:
    nome: str
    data_nascimento: str
    ra: str
    curso: str
    endereco: Endereco

    def exibir_dados(self):
        print("\n--- Dados do Aluno ---")
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"RA: {self.ra}")
        print(f"Curso: {self.curso}")
        print("Endereço:")
        print(f"  Logradouro: {self.endereco.logradouro}")
        print(f"  Número: {self.endereco.numero}")
        print(f"  Cidade: {self.endereco.cidade}")
        print(f"  Estado: {self.endereco.estado}")

def menu():
    alunos = []
    while True:
        print("\nMenu de Opções:")
        print("1 - Cadastrar aluno")
        print("2 - Exibir alunos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            data_nascimento = input("Digite a data de nascimento: ")
            ra = input("Digite o R.A: ")
            curso = input("Digite o seu curso: ")

            logradouro = input("Digite o logradouro: ")
            numero = input("Digite o número: ")
            cidade = input("Digite a cidade: ")
            estado = input("Digite o estado: ")

            endereco = Endereco(logradouro, numero, cidade, estado)
            aluno = ALUNO(nome, data_nascimento, ra, curso, endereco)
            alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")

        elif opcao == "2":
            if alunos:
                for i in alunos:
                     for i in alunos:
                        i.exibir_dados()
            else:
                print("Nenhum aluno cadastrado.")

        elif opcao == "3":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()