import os

os.system ("cls || clear")

print("numeros impares e pares:")

for i in range (6):
    numero = int(input("digite um numero:"))

    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")

print("\nfim do progama.")
