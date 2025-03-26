import os
os.system (" cls || clear")

contador = 0 
soma = 0 

while True:
    nota = float(input("digite uma nota: "))
    resposta = input("deseja inserir mais uma nota? \ndigite 's' ou 'n'").upper()
    if resposta == "n":
        break
    else:
        contador+= 1
        soma += nota
        if contador == 0:
            soma = nota
            contador = 1

            media = soma / contador

            print(f"\nmedia : {media}")