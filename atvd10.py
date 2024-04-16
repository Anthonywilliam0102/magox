class Pedido:
    def __init__(self):
        self.itens = []
        self.total_a_pagar = 0
        self.status = "Pendente"

    def adicionar_item(self, item, preco):
        self.itens.append((item, preco))
        self.total_a_pagar += preco

    def calcular_total(self):
        return self.total_a_pagar

    def alterar_status(self, novo_status):
        self.status = novo_status


pedido1 = Pedido()

pedido1.adicionar_item("Pizza", 20)
pedido1.adicionar_item("Refrigerante", 5)


total = pedido1.calcular_total()

print(f"Total a pagar: R${total}")


pedido1.alterar_status("Em andamento")
print(f"Status do pedido: {pedido1.status}")
