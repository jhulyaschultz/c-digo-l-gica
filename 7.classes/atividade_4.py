import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Livro:

    nome:str
    autor:str
    categoria:str
    preço:float

    def exibir_dados (self):
        print(f"nome: {self.nome} \nautor: {self.autor} \ncategoria: {self.categoria} \npreço: {self.preço}\n")
lista_livros = []
QUANTIDADE_LIVROS = 3

for i in range (QUANTIDADE_LIVROS):
    livro = Livro(
                        nome = input("digite o nome do livro: "),
                        autor = input("digite o autor: "),
                        categoria = input("digite a categoria do livro: "),
                        preço = float(input("digite o valor do livro: "))
                    )
    lista_livros.append(livro)

nome_arquivo = "dados_livros.txt"
with open (nome_arquivo, "w") as arquivo_livros:
        for livro in lista_livros:
            arquivo_livros.write(f"{livro.nome}\n {livro.autor}\n {livro.categoria}\n {livro.preço}\n")

print ("dados salvos com sucesso.")

print("\nexibindo dados.")
for livro in lista_livros:
    livro.exibir_dados()