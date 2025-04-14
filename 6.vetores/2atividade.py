import os
os.system ("cls || clear")

def calcular_media(lista):
      return sum(lista_notas) / QUANTIDADE_NOTAS

def verificar_resultado(media):
    if media >=7:
      print("APROVADO!")
    elif media >=5:
      print("RECUPERAÇÃO!")
    else:
        print("REPROVADO!")
    return resultado

lista_notas = []
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
        nota = float(input("digite uma nota: "))
lista_notas.append(nota)

media = sum(lista_notas) / QUANTIDADE_NOTAS
resultado = verificar_resultado(media)

print()

for nota in lista_notas:
        print(nota)

print(f"média: {media}")