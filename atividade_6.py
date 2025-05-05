import os 
from dataclasses import  dataclass
os.system("clear")

@dataclass 
class Pessoa:
    nome:str
    data_nascimento:int
    rg:int
    cpf:int

def exibir_dados (self):
    print(f"nome: {self.nome} \ndata de nascimento: {self.data_nascimento} \nregistro geral: {self.rg} \ncpf: {self.cpf}\n")
lista_pessoas = []
QUANTIDADE_PESSOAS = 5

for i in range (QUANTIDADE_PESSOAS):
    pessoa = Pessoa(
                    nome = input("digite seu nome: ")
                    data_nascimento = int(input("digite sua data de nascimento: "))
                    rg = int(input("digite seu rg: "))
                    cpf = int(input("digite o cpf: "))
                    )
    lista_pessoas.append(pessoa)

nome_arquivo = "funcionarios.txt" 
with open (nome_arquivo, "w") as arquivo_pessoa: 
        for pessoa in lista_pessoas:
            arquivo_pessoa.write(f"{pessoa.nome}\n{pessoa.data_nascimento}\n{pessoa.rg}\n{pessoa.cpf}\n")
print("Dados salvos com sucesso.")

print("\nexibindo dados.")
for pessoa in lista_pessoas:
    pessoa.exibir_dados()
