import os
os.system ("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5

print("= Solicitando Números =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"digite  o {i+1}º número: "))
    lista_numeros.append(numero)

maior = max(lista_numeros)
menor = min(lista_numeros)

print("\nMostrando números")

for i, numero in enumerate(lista_numeros, start=1):
        print(f"{i}º número: {numero}")

print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")
