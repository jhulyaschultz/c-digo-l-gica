import os 
os.system (" cls || clear")

media_salario = 0
maior_idade = 0
menor_idade = 100
meninas_salario = 0
quantidade = 0


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
            quantidade = int(input("digite a quantidade de pessoas: "))
            for i in range(quantidade):
                idade = int(input(f"digite a {i+1}ª idade:"))
                sexo = input("digite seu sexo(M\F): ").upper()
                salario = float(input(f"digite o {i+1}º salario: "))

                media_salario += salario 

                if idade > maior_idade:
                    maior_idade = idade
                if idade < menor_idade:
                    menor_idade = idade
                if sexo =="F" and salario >= 5000:
                    meninas_salario += 1

                    os.system("cls || clear")

        case 2:

            if quantidade > 0:

                media_salario = media_salario / quantidade
                print(f"media de salario é: {media_salario:.2f}")
                print(f"maior idade do grupo: {maior_idade}")
                print(f"menor idade do grupo: {menor_idade}")
                print(f"quantidade de mulheres com salario a partir de R$5000: {meninas_salario}")
            else:
                print("nenhuma pessoa foi cadastrada.")

        case 3:
           break
        case _:
            print("opção inválida.tente novamente.")