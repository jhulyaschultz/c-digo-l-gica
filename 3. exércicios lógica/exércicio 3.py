import os 
os.system ("clear")

primeiro_numero = float(input("digite o primeiro numero:"))
segundo_numero = float(input("digite o segundo numero:"))

media = (primeiro_numero + segundo_numero) / 2
produto = primeiro_numero + segundo_numero

print (f"média : {media}")

if primeiro_numero < segundo_numero:
  print ("o primeiro_numero é menor que o segundo_numero!")
else :
    print ("o segundo_numero é maior que o primeiro_numero!")
