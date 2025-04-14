import os
os.system ("cls || clear")

peso = float(input("Digite Seu Peso: "))
altura = float(input("Digite Sua Altura: "))

def calcular_imc(peso, altura):
 imc = peso / altura ** 2
 return imc

if calcular_imc (peso , altura) < 18.5:
    print("Abaixo Do Peso.")
elif calcular_imc (peso , altura) < 24.9:
    print("Peso Normal.")
elif calcular_imc ("peso , altura") < 29.9:
    print("Sobrepeso.")
elif calcular_imc(peso , altura) < 34.9:
    print("Obesidade Grau 1.")
elif calcular_imc(peso , altura) < 39.9:
    print("Obesidade Grau 2.")
else:
    print("Obesidade Grau 3.")

print(f"O SEU IMC É: {calcular_imc(peso,altura)}")


