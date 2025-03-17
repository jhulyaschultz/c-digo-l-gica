import os
import  time

os.system("cls")

contagem = int(input("olá digite um numero: "))

print ("\ncontagem regressiva")

for i in range(contagem,0,-1):
    print(f"valor da variavel i: {i}")
    time.sleep(1)

print("fim do progama")