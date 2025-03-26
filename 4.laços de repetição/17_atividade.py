import os 
os.system (" cls || clear")

while True:
    print(""""
CÓDIGO | DESCRIÇÃO
1      | ADICIONAR PESSOAS
2      | EXIBIR RESULTADOS
3      | SAIR
""")
    
    opçao = int(input())

    match opçao:
        case 1:
            idade = int(input("digite sua idade: "))
            sexo = input("digite seu sexo : \n digite 'f' ou 'm': " ).upper()
            salário = input("informe seu salário : ")
        case 2:
            print(f"a idade é: {idade}")
            print(f"seu sexo é: {sexo}")
            print(f"sua média salárial é: {salário}")
        case 3:
            exit ("encerrado!")
        case _:
            ("opção inválida!")
    if idade < menor_idade
    menor_idade = idade