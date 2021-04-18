from collections import defaultdict

#vertice/no
class  Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
#arresta
class amizade:

    def __init__(self, pessoa1, pessoa2):
        self.pessoa1 = pessoa1
        self.pessoa2 = pessoa2

    def getPessoa1(self):
        return self.pessoa1
    
    def getPessoa2(self):
        return self.pessoa2


#grafo 
class Grafo:

    def __init__(self):
        self.grafo = defaultdict(list)    

    def addAresta (self, p1, p2):
        self.grafo [p1.getNome()].append(p2)
        self.grafo [p2.getNome()].append(p1)

    def imprimirAmigos(self, pessoa):
        for amigos in self.grafo[pessoa.getNome()]:
            print('%s' % amigos.getNome())


g = Grafo()


p1 = Pessoa('Maria', 20)
p2 = Pessoa('Pedro', 30)
p3 = Pessoa('Diego', 18)
p4 = Pessoa('Carol', 23)
p5 = Pessoa('Yankee', 82)


g.addAresta(p1, p2)
g.addAresta(p1, p3)
g.addAresta(p2, p4)
g.addAresta(p4, p3)
g.addAresta(p3, p5)
g.addAresta(p5, p1)


g.imprimirAmigos(p4)