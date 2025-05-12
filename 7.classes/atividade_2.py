import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class login():
    nome: str
    email: str
    telefone: float
    endereço: str

    def exibindo_dados(self):
        print("\nexebindo dados: ")
        print(f"nome: {self.nome}, e-mail: {self.email}, telefone: {self.telefone}, endereço{self.endereço}")


nome = input("digite seu nome: ")
email = input("digite seu email: ")
telefone = input("digite seu telefone: ")
endereço = input("digite seu endereço: ")

login = login(nome , email, telefone , endereço)
login.exibindo_dados()
