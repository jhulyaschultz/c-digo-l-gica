import os

os.system ("cls|| clear")

QUANTIDADE_DE_NOTAS = 2
soma = 0

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota = float(input("digite uma nota: "))

        if nota < 0 or nota > 10:
            print("a nota deve ser entre 0 e 10.\n")

        else:
            soma += nota
            break 

    media = soma / QUANTIDADE_DE_NOTAS

    print(f"media: {media}")