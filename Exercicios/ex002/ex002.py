#declaracao da classe
class Perfil:

    """
    Essa classe cria um perfil que tem nome e idade
    Para criar uma nova pessoa, use:
    variavel = Perfil(nome, idade)
    """
    def __init__(self, n = "Null", i = 0): #metodo construtor
        
    #atributos
        self.nome = n
        self.idade = i

    #metodos de instancia
    def aniversario(self):
        self.idade += 1
    
    
    def __str__(self): #DUNDER METHOD
        return f"Estado: nome = {self.nome}; idade = {self.idade}"
    
   
   
    def __getstate__(self):
            return f"Estado: nome = {self.nome}; idade = {self.idade}"

#declaracao dos objetoss
p = Perfil(n = "Matheus", i = 17)
p.aniversario()
#print(p.mensagem())

p1 = Perfil(n = 'Carlos', i = 45)
#print(p1.mensagem())

#print(p.__doc__) #<-- isso seria dunder attribute
#print(p)
#print(p1.__dict__) #<- 
#print(p1.__getstate__()) #<- personalizavel

p2 = Perfil(n = 'tania', i = 60)
print(p2)
print(p2.__str__())