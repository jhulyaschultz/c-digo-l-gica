import os
os.system ("cls || clear")

def tabuada(numero):
   for i in range(1,11):
         print(f"{numero} x {i} = {numero * i}")

print("= TABUADA =")
numero = int(input("digite um numero: "))
tabuada(numero)

print ("fim.")

