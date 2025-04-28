import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Endereco:
    logradouro: str
    numero: str
@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco

    def exibir_dados(self):
        print(f"nome: {self.nome} , idade:{self.idade} , logradouro: {self.endereco.logradouro} ,número: {self.endereco.numero}")

endereco1 = Endereco("RUA A" , "33")
pessoa1 = Pessoa("Helena" , 24 , endereco1)

print("DADOS PESSOAS: ")

pessoa1.exibir_dados()