import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class pessoa:
    nome: str
    idade: int
    peso: int
    altura: int

print("SOLICITANDO DADOS: ")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))


pessoa1 = pessoa (nome=nome , idade=idade ,peso=peso, altura=altura) 

print("DADOS PESSOAIS: ")

print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade}")
print(f"Peso: {pessoa1.peso}")
print(f"Altura: {pessoa1.altura}")