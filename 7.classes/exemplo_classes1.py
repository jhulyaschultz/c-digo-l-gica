import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class pessoa:
    nome: str
    idade: int

@dataclass
class pet:
    nome: str
    idade: int
    raca: str

pessoa1 = pessoa("Alice", 30)
pessoa2 = pessoa("Bob", 25)

pet1 = pet("toto", 4,"pastor alemao")
pet2 = pet("hulk",6 , "pitbull")

print("DADOS PESSOAIS: ")

print(f"Nome: {pessoa1.nome} , idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome} , idade: {pessoa2.idade}")

print("DADOS DOS PETS: ")

print(f"nome: {pet1.nome} , idade: {pet1.idade}")
print(f"nome: {pet2.nome} , idade: {pet2.idade}")