from datetime import date, datetime

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario
        self.nomes_diretores = [
            "Paulo Bragança"
        ]

    @property
    def nome(self):
        return self._nome.strip()
    
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
    
    def sobrenome(self):
        nome_completo = self._nome.strip()
        
        nome_quebrado = nome_completo.split(' ')
        
        if len(nome_quebrado) == 1:
            return None
        
        return nome_quebrado[-1]

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
    
    @staticmethod
    def valor_da_porcentagem(valor: float, porcentagem: float) -> float:
        """valor_da_porcentagem
           Método responsável por criar o valor de uma determinada porcentagem do valor
        Args:
            valor (float): Valor total
            porcentagem (float): Porcentagem desejada a ser adquirida

        Returns:
            float: valor da porcentagem baseada no valor total.
        """
        if not valor and not porcentagem:
            return 0.0
        
        result = (valor * porcentagem) / 1000
        
        print(result)

        return result
    
    @property
    def decrescimo_salario(self):
        if self._nome not in self.nomes_diretores and self._salario < 100000:
            return self._salario
        
        valor_porecentagem = self.valor_da_porcentagem(self._salario, 10)
        self._salario = self._salario - valor_porecentagem
    