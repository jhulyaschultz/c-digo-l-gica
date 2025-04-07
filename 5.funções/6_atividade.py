import os
os.system(" cls || clear ")

def numero_par(numero):
    if numero % 2 == 0:
        print("esse número é par.")
    else:
        print("esse é numero é impar.")

print("= PARES E IMPARES =")
numero = int(input("digite um numero: "))
numero_par(numero)

print ("fim.")