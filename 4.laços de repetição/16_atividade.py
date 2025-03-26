import os 
os.system (" cls || clear")

contador_pares = 0
contador_impares = 0
soma_pares = 0
soma_total = 0 
total = 0

while True:
    numero = int(input("digite um numero positivo: "))

    if numero == 0:
        break
    soma_total += numero 
    total == 1

    if numero % 2 == 0:
        contador_pares += 1 
        soma_pares += numero
    else:
        contador_impares += 1

media_pares = soma_pares / contador_pares if contador_pares > 0 else 0

media = soma_total / total if total > 0 else 0

print(f"contador pares: {contador_pares}")
print(f"contador impares: {contador_impares}")
print(f"media dos numeros pares: {media_pares}")
print(f"media geral: {media}")
