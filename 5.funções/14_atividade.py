import os
os.system ("cls || clear")

print("LENDO NOTAS: ")

soma = 0

def calcular(soma):
    return soma / 2

for i in range(2):
    nota = float(input(f"Digite a {i + 1} nota: "))
    soma += nota

media = calcular(soma)

print(f"média: {media}")

if media <7:
    print("REPROVADO!")
else:
    print("APROVADO!")

print ("\nFIM.")

