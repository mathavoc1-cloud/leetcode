#CRIE UMA CLASSE FUNCIONARIO, 
#ONDE PODEMOS CADASTRAR: NOME, SETOR E CARGO.
#CRIE TAMBEM UM METODO QUE PERMITA AO FUNCIONARIO SE APRESENTAR.
from rich import print

class Funcionario:
    """
    Cadastra funcionarios pelo nome, setor e cargo
    """

    def __init__(self, nome, setor, cargo):

        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f"Hello, I'm [bold blue]{self.nome}[/bold blue] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Video"
    

c1 = Funcionario (nome = "Matheus", setor = "TI", cargo = "DEV Junior")
print(c1)

c2 = Funcionario (nome = "Roberta", setor = "Financeiro", cargo = "Diretor(a)")
print(c2)