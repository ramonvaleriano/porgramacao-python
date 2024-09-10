from datetime import date, datetime

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome
    
    @property
    def salario(Self):
        return Self._salario
    
    @property
    def data_nacimento(self):
        return self._data_nascimento
    
    def idade(self):
        formato = "%d/%m/%Y"

        data = datetime.strptime(self._data_nascimento, formato)

        ano = data.year

        ano_atual = date.today().year
        return ano_atual - ano

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'