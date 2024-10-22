"""test_bytecode.py

   Arquivo responsável por testar o arquivo bytecode.py
"""
# Arquivo que será testado
from codigo.bytecode import Funcionario

# Bibliotecas python
from datetime import datetime, timedelta


def test_retorno_do_nome():
    maria = Funcionario("Maria", "30/09/90", 25000)
    nome_maria = maria.nome

    assert nome_maria == "Maria"

def test_retorno_do_salario():
    maria = Funcionario("Maria", "30/09/90", 25000)
    salario_maria = maria.salario

    assert salario_maria == 25000

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

