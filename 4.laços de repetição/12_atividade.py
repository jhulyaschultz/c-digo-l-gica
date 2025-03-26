import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3
soma = 0

for i in range (QUANTIDADE_NOTAS):
    while True:
        nota = float(input("digite a nota do aluno: "))
        soma += nota

        media = soma/3
        if nota <0 or nota > 10:
            print("Notas somente de 0 à 10!")
        else:
            soma += nota
            break

if nota >7:
    print("Aprovado")
elif nota <7 and nota >4:
    print("Recuperação")
else:
    print("Reprovado")                 