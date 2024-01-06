class Carro:
    lista_carros: []

    def __init__(self, modelo='', cor='', ano=0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'{self.modelo} | {self.cor}'

ferrari = Carro(
    modelo = 'esportiva', 
    cor = 'vermelho', 
    ano = 2020
    )

carro2 = Carro('casual', 'preto', 2022)

print(ferrari)