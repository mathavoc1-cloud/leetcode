#Crie a classe Churrasco, onde seja possivel informar quantas pessoas vao participar
#e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preco por pessoa
from rich.panel import Panel


class Churrasco: 
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
    
    def etiqueta(self):
        conteudo = f'''Analisando {self.nome} com {self.quantidade}. Cada participante comera 0.4kg e cada kg custa R$82.40. 
        Recomendo comprar {self.calculo} de carne. Custo total de R${self.preco}. Cada pessoa pagara R${self.preco_cada} para participar.'''
        print(Panel(conteudo, title = 'Produto', width = 35 ))

    def analisar(self, valor):
        self.quantidade * 




c1 = Churrasco(titulo = "Churras dos amigos", quantidade = 15)
c1.analisar()

# Consumo padrao: 480g por pessoa
# preco: R$ 82,48/Kg