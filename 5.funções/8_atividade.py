import os
os.system ("cls || clear")

def calcular_media(primeira_nota , segunda_nota):
    return (primeira_nota + segunda_nota) / 2

nota1 = int(input("digite sua primeira nota: "))
nota2 = int(input("digite a segunda nota: "))
media =calcular_media(nota1, nota2)
def aprovado():
    if media >= 7:
        print("aprovado.")
    else:
        print("reprovado.")

aprovado()
print(f"média: {media}")