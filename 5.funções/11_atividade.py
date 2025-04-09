import os
os.system (" cls || clear ")

def produto(valor):
    return valor 
print("PREÇO DO PRODUTO")
produto1 = float(input("Digite o valor do produto: "))
if produto1 >=100:
    taxa = 1.20
else:
    taxa = 1.10     

valor_final = produto1*taxa
print(f" o valor final com juros é: {valor_final}")    

def produto(valor):
    return valor
if produto1 >=100:
    taxa = 0.20
else:
    taxa = 0.10     

valor_final = produto1*taxa
print(f" o valor final sem juros é: {valor_final}")    

