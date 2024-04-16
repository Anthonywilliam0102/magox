class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def emitir_som(self):
        pass  
    def informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Espécie: {self.especie}"


class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"


meu_cachorro = Cachorro(nome="Rex", idade=3, especie="Cachorro")
print(meu_cachorro.informacoes())
print(meu_cachorro.emitir_som())
