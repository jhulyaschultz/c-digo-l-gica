import os
os.system ("cls || clear")

soma = 0 

while True:
        opçao = int(input("""
código\t prato \t\t\t valor
1 \t picanha \t\t R$ 25,00
2 \t lasanha \t\t R$20,00 
3 \t strogonoff \t\t R$ 18,00
4 \t bife acebolado \t\t R$15,00
5 \t pão com ovo \t\t R$05,00

digite a opção desejada:
"""))

        match opçao:
                case 1:  
                        prato = "picanha"
                        preco = 25
                case 2:
                        prato = "lasanha"
                        preco = 20
                case 3:
                        prato = "strogonoff"
                        preco = 18
                case 4:
                        prato = "bife acebolado"
                        preco = 15
                case 5:
                        prato = "pao com ovo"
                        preco = 5
                case _:
                        prato = "opcao invalida"
                        preco = 0 
        soma += preco 
        continuar = input("deseja escolher outro prato? \n digite 'S' ou 'N' :").lower()

        if continuar == "n":

                break

        os.system("cls || clear")

        print(f"\ntotal a pagar: R$ {soma}")