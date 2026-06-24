#declaracao da classe
class Gafanhoto: 
    def __init__(self): #-> metodo construtor:
    #atributos
        self.nome = ""
        self.idade = 0
        #metodos de instancia
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f'{self.nome} eh um(a) Gafanhoto(a) e tem {self.idade} anos de idade'




#declaracao dos objetos
obj = Gafanhoto() #<- chamada de instanciacao
obj.nome = 'Maria'
obj.idade = 27 #-> n tem parenteses eh um metodo
obj.aniversario() #-> tem parenteses, logo eh um metodo
print(obj.mensagem())


g2 = Gafanhoto ()
g2.nome = "Mauro"
g2.idade = 33
print(g2.mensagem())