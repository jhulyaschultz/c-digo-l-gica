import os

def logo_senai():
    os.system("cls || clear")
    print("== senai ==")

logo_senai()
nome = input("digite seu nome: ")

logo_senai()
idade = int(input("digite sua idade:"))

logo_senai()
print(f"nome: {nome}")
print(f"idade: {idade}")