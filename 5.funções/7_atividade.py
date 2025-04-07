import os
os.system ("cls || clear")

def numero_negativo(numero):
    if numero <0:
        print("esse número é negativo.")
    elif numero == 0:
        print("0 é neutro.")
    else: 
        print("esse é numero é positivo.")


print("= POSITIVO E NEGATIVO =")
numero = int(input("digite um numero: "))
numero_negativo(numero)

print ("fim.")