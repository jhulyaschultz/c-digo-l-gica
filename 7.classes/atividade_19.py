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

    def cadastrar_aluno():
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

    def exibir_alunos():
        if alunos:
            for aluno in alunos:
                aluno.exibir_dados()
        else:
            print("Nenhum aluno cadastrado.")

    def atualizar_aluno():
        ra = input("Digite o RA do aluno a ser atualizado: ")
        for aluno in alunos:
            if aluno.ra == ra:
                print("Digite os novos dados do aluno (pressione Enter para manter o valor atual):")
                nome = input(f"Nome ({aluno.nome}): ") or aluno.nome
                data_nascimento = input(f"Data de nascimento ({aluno.data_nascimento}): ") or aluno.data_nascimento
                curso = input(f"Curso ({aluno.curso}): ") or aluno.curso

                logradouro = input(f"Logradouro ({aluno.endereco.logradouro}): ") or aluno.endereco.logradouro
                numero = input(f"Número ({aluno.endereco.numero}): ") or aluno.endereco.numero
                cidade = input(f"Cidade ({aluno.endereco.cidade}): ") or aluno.endereco.cidade
                estado = input(f"Estado ({aluno.endereco.estado}): ") or aluno.endereco.estado

                aluno.nome = nome
                aluno.data_nascimento = data_nascimento
                aluno.curso = curso
                aluno.endereco = Endereco(logradouro, numero, cidade, estado)

                print("Aluno atualizado com sucesso!")
                return
        print("Aluno com RA informado não encontrado.")

    def deletar_aluno():
        ra = input("Digite o RA do aluno a ser deletado: ")
        for i, aluno in enumerate(alunos):
            if aluno.ra == ra:
                del alunos[i]
                print("Aluno deletado com sucesso!")
                return
        print("Aluno com RA informado não encontrado.")

    while True:
        print("\nMenu de Opções:")
        print("1 - Cadastrar aluno")
        print("2 - Exibir alunos")
        print("3 - Atualizar aluno")
        print("4 - Deletar aluno")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            exibir_alunos()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            deletar_aluno()
        elif opcao == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
