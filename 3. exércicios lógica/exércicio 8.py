import os
os.system ("clear")

#desenvolva um algoritmo que a pessoa digite um numero e apareça o mes.

mes = int(input("digite um número para o mes:"))

#processamento
match mes:
    case 1:
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3:
        print("março")
    case 4:
        print("abril")
    case 5:
        print("maio")
    case 6:
        print("junho")
    case  7:
        print("julho")
    case  8:
        print("agosto")
    case  9:
        print("setembro")
    case  10:
        print("outubro")
    case  11:
        print("novembro")
    case  12:
        print("dezembro")
    case  _:
        print("opção inválida")

