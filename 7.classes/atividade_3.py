import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: Endereco

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}")
        print(f"Cidade: {self.endereco.cidade}")

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
logradouro = input("Digite seu logradouro: ")
numero = input("Digite o número da residência: ")
cidade = input("Digite a cidade: ")

endereco1 = Endereco(logradouro=logradouro, numero=numero, cidade=cidade)
pessoa1 = Pessoa(nome=nome, email=email, endereco=endereco1)

print("\nDADOS PESSOAIS:")
pessoa1.exibir_dados()
