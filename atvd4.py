class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}"

    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente."
        else:
            self.saldo -= valor
            return f"Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}"

    def mostrar_saldo(self):
        return f"Saldo atual: R${self.saldo}"


conta1 = ContaBancaria(numero_conta="123456", titular="João")
print(conta1.depositar(100))
print(conta1.sacar(50))
print(conta1.mostrar_saldo())
