import os
os.system("cls || clear")

def converter_centimetros(metros):
    return metros * 100;

print(" = converter metros para centimetros =")
metros = float(input("digite um numero: "))

centimetros = converter_centimetros(metros)

print("\n= resultados =")
print(f"{metros}metros é igual a {centimetros} centimetros.")
