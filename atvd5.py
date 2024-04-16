class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def atualizar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade

    def calcular_preco_total(self, quantidade):
        return self.preco * quantidade


produto1 = Produto(nome="Camiseta", preco=29.99, quantidade_estoque=100)


produto1.atualizar_estoque(10)


preco_total = produto1.calcular_preco_total(5)
print(f"Preço total para comprar 5 camisetas: R${preco_total}")
