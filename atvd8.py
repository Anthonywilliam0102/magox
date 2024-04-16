class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura

    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)


retangulo1 = Retangulo(altura=5, largura=10)


area = retangulo1.calcular_area()
perimetro = retangulo1.calcular_perimetro()

print(f"Área do retângulo: {area}")
print(f"Perímetro do retângulo: {perimetro}")
