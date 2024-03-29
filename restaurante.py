from avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome='', categoria='', ativo=False):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:                            #Só aceitar notas de 1 a 5.
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property           #Torna possível ler essas informações.
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "not yet"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        #pega a NOTA de todas as avalicoes que existam em self._avaliacao. 
        quantidade_de_nostas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_nostas, 1)
        return media