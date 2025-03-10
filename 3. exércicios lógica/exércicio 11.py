import os
os.system ("clear")

aluno = input("digite o seu nome:")
primeira_nota = float(input("digite a primeira nota: "))
segunda_nota  = float(input("digite a segunda nota: "))

media = ( primeira_nota + segunda_nota ) / 2

print (f"media : (media)")
if media >= 9:
    conceito = "A"
elif media > 7.5:
    conceito = "B"
elif media>= 6:
    conceito = "C"
elif media>= 4:
    conceito = "D"
else:
    conceito = "E"

match conceito:
    case "A" |"B" |"C":
        print(f"conceito: {conceito}")
        print("aprovado!")
    case "D"|"E":
        print(f"conceito: {conceito}")
        print ("reprovado!")
    case _:
        print("opção inválida!")    

