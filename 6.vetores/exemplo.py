import os
os.system(" cls || clear ")

lista_notas = []

for i in range(3):
    nota = float(input("digite uma nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
print()
for nota in lista_notas:
        print(nota)