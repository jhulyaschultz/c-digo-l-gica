import os
os.system ("cls || clear")

contador = 0

while True:
  #comandos a serem repetidos
  print("repetindo....")

  continua = input("Tecle 's' se deseja continuar:").strip().lower()
  contador += 1

  if continua != 's' :
    break
  if contador == 0 :
    print("o bloco NÃO foi repetido.")
  else:
    print(f"o bloco foi repetido {contador} vezes")
