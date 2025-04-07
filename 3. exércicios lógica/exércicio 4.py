import os
os.system ("clear")

#considere que os dados do usúario já estão cadastrados.
#caso login e senha estejam corretos,mostre a mensagem:
#"bem-vindo!"
#caso contrário , mostre a mensagem:
#"login ou senha inválidos."

login_cadastrado = "marta"
senha_cadastrada = "123"

login = input ("digite o login:")
senha = input ("digite a semha:")

if login == login and senha == senha_cadastrada:
     print("bem-vindo!")

else:
     print ("login ou senha inválidos!")

         