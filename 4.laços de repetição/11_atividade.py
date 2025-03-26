import os

os.system ("cls|| clear")

login_ = "Jhulya"
senha_ = "524120"

QUANTIDADE_DE_TENTATIVAS = 3

for i in range (QUANTIDADE_DE_TENTATIVAS):

    login = input("digite seu login: ")
    senha = input("digite sua senha: ")

    if login_ == login and senha_ == senha:
        print("usuario e senhas corretos!")
        break

    else:
        print("login ou senhas inválidos.")
    if i == 2:
        print("voce chegou ao limite máximo")
print("fim.")