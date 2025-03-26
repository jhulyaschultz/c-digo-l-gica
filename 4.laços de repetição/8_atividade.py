import os

os.system("cls||clear")

nota = int(input("digite sua nota : "))

while True:
    nota = float(input("digite sua nota :"))

    if nota < 0 or nota >10:
        print("a nota deve ser entre 0 e 10.")
    else:
       break
    
print(f"nota {nota}")