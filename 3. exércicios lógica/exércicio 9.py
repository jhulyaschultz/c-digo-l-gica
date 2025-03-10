import os
os.system ("clear")

valor_produto = float(input("digite o valor do produto:"))
forma_de_pagamento = int(input("""
1 - a vista
2 - a prazo
digite a forma de pagamento:"""))

match forma_de_pagamento:
    case 1:
        desconto = valor_produto * 0.10
        valor_pagar = valor_produto - desconto

        print(f"\nvalor do produto:R$ {valor_produto}")
        print(f"forma de pagamento: á vista")
        print(f"valor do desconto : R${desconto}")
        print(f"total a pagar: R$ {valor_pagar}")
    case 2:
        quantidade_parcelas = int(input("digite a quantidade de parcelas: "))
        if quantidade_parcelas >= 1 and quantidade_parcelas <=6:
            valor_parcela = valor_produto / quantidade_parcelas
            print(f"\nvalor do produto: R$ {valor_produto}")
            print(f"forma de pagamento: á prazo")
            print(f"quantidade de parcelas: {quantidade_parcelas}")
            print(f"valor por parcela: R$ {valor_parcela:.2f}")
            print(f"total a prazo: R${valor_produto}")
        else: 
            print("0 parcelamento deve ser em até 6 parcelas.")
    case _:
        print("opção inválida.")
        