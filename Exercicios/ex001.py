#declaracao da classe
class Perfil:
    def __init__(self): #metodo construtor
        
    #atributos
        self.nome = ""
        self.idade = 0

    #metodos de instancia
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f'Ola {self.nome}, voce tem {self.idade} anos de idade!'
   

#declaracao dos objetos
p = Perfil()#<- chamada de instanciacao
p.nome = 'Matheus'
p.idade = 27 #-> n tem parenteses, eh um atributo
p.aniversario()#-> tem parenteses, logo eh um metodo
print(p.mensagem())

p1 = Perfil()
p1.nome = 'Carlos'
p1.idade = 45
p1.aniversario()
print(p.mensagem())
