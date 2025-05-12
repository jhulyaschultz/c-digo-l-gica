import os 
from dataclasses import  dataclass
os.system("clear")

@dataclass
class Autor:
    nome:str
    biografia:str

class Livro:
    titulo:str
    ano:int
    autor:Autor

    def exibir_detalhes(self):
        print(f"titulo: {self.titulo} \nano: {self.ano} \nautor: {self.autor.nome}")
print("= SOLICITANDO DADOS PARA O USÚARIO = ")

livro = Livro(
            titulo = input("digite o titulo do livro: "),
            ano = int(input("digite o ano de publicação: ")),
            autor = Autor(
                nome = input("digite o nome do autor: "),
                bibliografia = input("digite as informações da bibliografia do autor: ")
                )
)

print("\n Dados salvos com sucesso = ")

print("\n= Lendo dados do arquivo = ")

