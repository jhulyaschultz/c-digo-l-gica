import os
os.system (" cls || clear ")

lista_numeros = []
QUANTIDADE_NUMEROS = 6

def pares_impares(lista):
    pares = 0
    impares = 0 
    for numero in lista:
        if numero % 2 == 0:
                pares += 1
        else:
          impares += 1
    return pares , impares

print("= PARES E IMPARES =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"digite  o {i+1}º número: "))
    lista_numeros.append(numero)

pares, impares = pares_impares(lista_numeros)

        
print("\nMostrando números")

for i, numero in enumerate(lista_numeros, start=1):
        print(f"{i}º número: {numero}")

if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
else:
        quantidade_impares += 1
      
print(f"quantidade de numeros pares:  {quantidade_pares}")
print(f"quantidade de numeros impares: {quantidade_impares}")

