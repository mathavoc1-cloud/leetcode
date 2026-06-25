class ContaBancaria:
    """
    Cria conta bancaria que permite fazer saques e depositos
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criado com sucesso! Saldo atual de R${self.saldo:,.2f}')

    def __str__(self):
        return f"A conta {self.id}, tem R${self.saldo:,.2f} de saldo!"

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}')
    
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque de {valor:,.2f} negado! Saldo insuficiente!')
        else:
            self.saldo -= valor
            print(f'Saque de {valor:,.2f} autorizado!')
        
        


conta1 = ContaBancaria(id = 112, nome = "Matheus", saldo = 4000)
conta1.depositar(500)
conta1.sacar(7500)
print(conta1)



