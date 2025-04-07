import os
os.system ("cls || clear")

def logo_senai():
    os.system("cls || clear")
    print("=== SENAI DENDEZEIROS ===")

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1 , n2):
    return n1 / n2

logo_senai
n1 = int(input("digite o primeiro numero: "))

logo_senai
n2 = int(input("digite o segundo numero: "))

multiplicacao = multiplicar (n1, n2)
divisao = dividir (n1 , n2)

logo_senai()
print(f"multiplicação: {multiplicacao}")
print(f"divisão: {divisao}")
