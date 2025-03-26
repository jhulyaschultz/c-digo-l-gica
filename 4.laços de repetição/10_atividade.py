import os

os.system ("cls|| clear")

login_ = "Jhulya"
senha_ = "524120"

while True:
    login = input("digite seu login: ")
    senha = input("digite sua senha: ")

    if login_ == login and senha_ == senha:
        print("usuario e senhas corretos!")
        break
    else:
        print("login ou senhas inválidos.")

print(f"login{login}")
print(f"senha {senha}")

print("fim.")