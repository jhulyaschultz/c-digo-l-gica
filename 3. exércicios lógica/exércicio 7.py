import os
os.system ("clear")

dia = 0
#processamento
match dia:
    case 1:
        print("domingo")
    case 2:
        print("segunda")
    case 3:
        print("terça")
    case 4:
        print("quarta")
    case 5:
        print("quinta")
    case 6:
        print("sexta")
    case  7:
        print("sábado")
    case _:
        print("opção inválida")
