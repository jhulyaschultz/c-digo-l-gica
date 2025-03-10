import os
os.system ("clear")

#faça um algoritmo que mostre um menu com opções deum cardapio de restaurante
#para uma pessoa.
#a pessoa vai escolher o prato desejado digitando o código do prato.
#após escolher o prato, o algoritmo deve mostrar o nome e o valor do prato escolhido.

#entrada
opçao = int(input("""
código\t prato \t\t\t valor
1 \t picanha \t\t R$ 25,00
2 \t lasanha \t\t R$20,00 
3 \t strogonoff \t\t R$ 18,00
4 \t bife acebolado \t\t R$15,00
5 \t pão com ovo \t\t R$05,00

digite a opção desejada:
"""))

#processamento
match opçao:
 case 1 :
  prato = "picanha"
  valor = 20,00
 case 2 :
  prato = "lasanha"
  valor = 25,00
 case 3 :
  prato = "strogonoff"
  valor = 18,00
 case 4 :
  prato = "bife acebolado"
  valor = 15,00
 case 5 :
  prato = "pao com ovo"
  valor  = 5,00    

#saída
print(f"\nprato escolhido:{prato}")
print(f"\nvalor:{valor}")

