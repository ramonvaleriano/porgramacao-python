"""bytecode.py

Arquivo para criar um banco digital
"""

from datetime import datetime


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @staticmethod
    def validador_do_nome(nome: str) -> bool:
        if nome in [None, '', ' ', False, 0] or (isinstance(nome, str) and nome.lower() in ['false', 'none'] ):
            return True
        
        return False

    @property
    def nome(self):
        valida_nome = self.validador_do_nome(self._nome)
        
        if valida_nome:
            return None
        
        name = self._nome

        return name
    
    @property
    def sobrenome(self):
        valida_nome = self.validador_do_nome(self._nome)
        
        if valida_nome:
            return None
        
        nome_completo = self._nome.strip()
        nome_completo_em_lista = nome_completo.split(' ')

        sobrenome = ''

        if len(nome_completo_em_lista) != 1:
            sobrenome = nome_completo_em_lista[-1]

        return sobrenome


    @property
    def salario(self):
        salary = self._salario

        return salary

    @property
    def idade(self):
        """idade
           Método responsável por retornar a idade da pessoa
        Returns:
            (float): Idade da pessoa
        """
        date_of_birth = self.conversor_de_data_string_para_datetime(
            self._data_nascimento
        )
        age = self.descobrindo_idade(date_of_birth)

        if age is not None:
            return age

        return None

    def conversor_de_data_string_para_datetime(self, data_string: str) -> datetime:
        """conversor_de_data_string_para_datetime
           Método responsável por converter uma string de uma data em uma datetime
        Args:
            data_string (str): Data em formato de string
        Returns:
            datetime: Datetime de fato.
        """
        if data_string is None or data_string == "" or data_string == " ":
            return data_string

        data_de_nacimento = data_string

        if isinstance(data_string, str):
            try:
                data_de_nacimento = datetime.strptime(data_string, "%d/%m/%y")

            except Exception:
                
                data_de_nacimento = datetime.strptime(data_string, "%d/%m/%Y")

        return data_de_nacimento

    def descobrindo_idade(self, data_nascimento: datetime) -> float:
        """descobrindo_idade
           Método responsável por retornr a idade de uma pessoa
        Args:
            data_nascimento (datetime): Data de nascimento

        Returns:
            float: Idade de pessoas em float
        """

        if isinstance(data_nascimento, str):
            return None

        hoje = datetime.today()
        diferenca_de_datas = hoje - data_nascimento
        idade_complexo = diferenca_de_datas.days

        if idade_complexo <= 0:
            return None

        idade = idade_complexo / 365

        return int(idade)
