class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return f"{self.nome} foi aprovado com média {media:.2f}"
        else:
            return f"{self.nome} foi reprovado com média {media:.2f}"


estudante1 = Estudante(nome="Maria", idade=20, notas=[8, 7, 9, 6])


media = estudante1.calcular_media()
resultado = estudante1.verificar_aprovacao()

print(resultado)
