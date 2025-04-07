import os 
os.system ("cls || clear")

def logo_senai():
    os.system("cls || clear")
    print("=== SENAI DENDEZEIROS ===")

def somar(n1, n2):
    return n1 + n2
def subtrair(n1 , n2):
    return n1 - n2
def multiplicacao(n1, n2):
    return n1 * n2
def divisao(n1, n2):
    return n1 / n2

logo_senai
n1 = int(input("digite o primeiro numero: "))

logo_senai
n2 = int(input("digite o segundo numero: "))

soma = somar (n1, n2)
subtracao = subtrair (n1 , n2)
multiplicacao =  multiplicacao (n1, n2)
divisao = divisao (n1, n2)

logo_senai()
print(f"soma: {soma}")
print(f"subtração: {subtracao}")
print(f"multiplicação: {multiplicacao}")
print(f"divisão: {divisao}")
