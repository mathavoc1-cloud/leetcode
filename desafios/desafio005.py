#Crie a classe Gamer, ond epodemos cadastras nome, nick e os jogos favoritos 
#de uma pessoa. Crie tambem um metodo que permita mostrar a ficha desse gamer. 
from rich import print  
from rich.panel import Panel
from rich.text import Text

class Gamer:

    def __init__(self, nome, nick):

        self.nome = nome
        self.nick = nick
        self.jogo = []

    def etiqueta (self):
        conteudo = Text(justify = "left")
        conteudo.append(f"Nome real: {self.nome}\n Jogos Favoritos:\n")
        for j in self.jogo:
            conteudo.append(f" -{j}\n")
        print(Panel(conteudo, title=f'Jogador <{self.nick}>', width=35))
    
    def favoritos(self, jogo):
        self.jogo.append(jogo)


j1 = Gamer(nome= "Matheus Silva", nick="hairynigga")
j1.favoritos("CS2")
j1.favoritos("PUBG")
j1.favoritos("GTA")
j1.favoritos("War Thunder")
j1.etiqueta()
