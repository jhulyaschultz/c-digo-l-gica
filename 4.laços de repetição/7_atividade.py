import os
os.system ("cls || clear")

print("notas e médias: ")

soma = 0
for i in range (3):
    nota = float(input(f"digite a {i + 1} nota:"))
    soma = soma + nota
    media = soma / 3
if media > 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

print(f"media: {media}")
print("\nFim")