import os

os.system ("cls || clear")

print("somando números:")
soma = 0

for i in range(5):
    nota = float(input(f"digite a {i + 1}a nota: "))
    soma = soma + nota

print()
print(f"soma: {soma}")

print ("\nfim do progama.")