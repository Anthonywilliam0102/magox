class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def ligar(self):
        return f'o carro da {self.marca}, modelo {self.modelo} ano {self.ano} cor {self.cor} está ligado.'

    def acelerar(self):
        return f'o carro da {self.marca}, modelo {self.modelo} ano {self.ano} cor {self.cor} está acelerando.'

    def desligar(self):
        return f'o carro da {self.marca}, modelo {self.modelo} ano {self.ano} cor {self.cor} está desligado.'
    
if __name__ == '__main__':
    carro1 = Carro('Volksvagem','Gol','2004','Preto')
    carro2 = Carro('Jeep','Commander','2022','Azul prateado')
    carro3 = Carro('volvo','xc90','2018','preto fosco')
    print(carro1.ligar())
    print(carro2.acelerar())
    print(carro3.desligar())
    print(carro1.desligar())

