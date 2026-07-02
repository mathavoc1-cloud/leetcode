#Crie a classe Churrasco, onde seja possivel informar quantas pessoas vao participar
#e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preco por pessoa
from rich import print
from rich.panel import Panel


class Churrasco: 
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
        self.calculo = 0
        self.preco = 0
        self.preco_cada = 0
    
    def etiqueta(self):
        conteudo = f'Analisando [green]{self.nome}[/green] com [bold blue]{self.quantidade} convidados[/bold blue]. Cada participante comera 0.4kg e cada kg custa R$82.40. Recomendo comprar [red]{self.calculo:,.2f}kg de carne[/red]. Custo total de R${self.preco:,.2f}. Cada pessoa pagara [yellow]R${self.preco_cada:,.2f}[/yellow] para participar.'
        print(Panel(conteudo, title = 'Produto', width = 35 ))

    def analisar(self):
        self.calculo = self.quantidade * 0.4
        self.preco = self.calculo * 82.40
        self.preco_cada = self.preco / self.quantidade

    




c1 = Churrasco(nome = "Churrasco", quantidade = 6)
c1.analisar()
c1.etiqueta()
# Consumo padrao: 480g por pessoa
# preco: R$ 82,48/Kg