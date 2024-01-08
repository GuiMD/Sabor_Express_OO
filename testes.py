class ContaBancaria:
    def __init__(self, titular='', saldo='', ativo=False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    
    def __str__(self):
        return f'Conta de {self.titular} - Saldo = R${self.saldo}'
    
    @classmethod
    def ativar_conta(cls, self):
        self._ativo = not self._ativo
        return f'Conta = {self._ativo}'
    
conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)
conta3 = ContaBancaria("Carlos", 200)

print(conta1)
print(conta2)
print(conta3)

ContaBancaria.ativar_conta(conta3)
print(f'conta 3 atividade: {conta3.ativo}')