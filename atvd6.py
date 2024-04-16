class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
      
    def registro(self):
        return f' capitão {self.nome}, da idade {self.idade},  possui {self.altura} '   

    def comprimento(self):
        return f'olá, boa tarde, {self.nome},'
if __name__ == "__main__":
   Pessoa1 = Pessoa("anthony","68","1.76") 
   print(Pessoa1.registro())
   print (Pessoa1.comprimento())