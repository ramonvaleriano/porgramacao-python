"""test_bytecode.py

   Arquivo responsável por testar o arquivo bytecode.py
"""
# Arquivo que será testado
from codigo.bytecode import Funcionario

# Bibliotecas python
from datetime import datetime, timedelta

# Testando dados para validar o nome que está vindo.
def test_retorno_do_nome():
    maria = Funcionario("Maria", "30/09/90", 25000)
    nome_maria = maria.nome

    assert nome_maria == "Maria"

# Valiando o retorno do salário.
def test_retorno_do_salario():
    maria = Funcionario("Maria", "30/09/90", 25000)
    salario_maria = maria.salario

    assert salario_maria == 25000

# Retornando a idade adequada.
def test_retorno_do_idade_adequada():
    maria = Funcionario("Maria", "30/09/90", 25000)
    idade_maria = maria.idade

    assert idade_maria == 34

def test_retorno_do_idade_inadequada_uma_ano_a_mais():
    hoje = datetime.now()

    um_ano_depois = hoje + timedelta(days=365)
    
    data_em_string = um_ano_depois.strftime("%d/%m/%y")

    maria = Funcionario("Maria", data_em_string, 25000)
    idade_maria = maria.idade

    assert idade_maria is None

class TestFuncionario:

    def test_nome_incorreto(self):
        funcionario = Funcionario(' ', '14/09/1989', 30000)
        nome = funcionario.nome

        funcionario1 = Funcionario('', '14/09/1989', 30000)
        nome1 = funcionario1.nome

        funcionario2 = Funcionario(None, '14/09/1989', 30000)
        nome2 = funcionario2.nome

        funcionario3 = Funcionario(False, '14/09/1989', 30000)
        nome3 = funcionario3.nome

        funcionario4 = Funcionario("False", '14/09/1989', 30000)
        nome4 = funcionario4.nome


        assert nome is None
        assert nome1 is None
        assert nome2 is None
        assert nome3 is None
        assert nome4 is None

    def test_sobrenome_correto_dois_sobrnome(self):
        maria = Funcionario("Maria Goes Pereira", "14/09/1989",  1000)

        sobrenome = maria.sobrenome

        assert sobrenome == "Pereira"

    def test_sobrenome_correto_um_sobrnome(self):
        maria = Funcionario("Maria Goes", "14/09/1989",  1000)

        sobrenome = maria.sobrenome

        assert sobrenome == "Goes"

    def test_sobrenome_sem_sobrnome(self):
        maria = Funcionario("Maria", "14/09/1989",  1000)

        sobrenome = maria.sobrenome

        assert sobrenome == ''