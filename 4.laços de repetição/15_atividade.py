import os
os.system ("cls || clear ")

soma = 0
contador = 0

while True:
    numero = int(input("digite um numero positivo ou um negativo para sair: "))
    if numero < 0:
        break

    soma += numero 
    contador += 1

if contador > 0:
    media = soma / contador 

    print (f"a media dos numeros é: {media : .2}")

else:
    print("nenhum numero positivo encontrado.")

