#CRIE A CLASE ControleRemoto, onde vamos simular
#o funcionamento de um controle simples (canal, volume e liga/desliga)
from rich import print
from rich.panel import Panel
from rich.text import Text


class ControleRemoto:

    def __init__(self, canal=0, volume = 0, liga = False, desliga = True):
        self.canal = canal
        self.volume = volume
        self.liga = liga
        self.desliga = desliga

    def etiqueta(self):
        conteudo = Text(justify = "left")
        if self.liga == True:
            conteudo.append("A TV esta desligada")
        else:
            conteudo.append("A TV esta ligada")

    