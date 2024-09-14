from bytebank import Funcionario

class TestClass:
    def test_caso_positivo_com_data_adequada(self):
        maria = Funcionario('Maria Lopes', '14/09/1989', 3000)

        result = maria.idade()

        assert result == 35

    def test_sobre_nome_coerente(self):
        maria = Funcionario('Maria Lopes', '14/09/1989', 3000)

        result = maria.sobrenome()

        assert result == 'Lopes'

    def test_apenas_o_primeiro_nome(self):
        maria = Funcionario('Maria', '14/09/1989', 3000)

        result = maria.sobrenome()

        assert result is None

    def test_nome_positivo(self):
        maria = Funcionario('Maria Lopes', '14/09/1989', 3000)

        result = maria.nome

        assert result == 'Maria Lopes'

    def test_decrescimo_de_10_porcento(self):
        # Testando funcionabilidade de redução dos 10%.

        salario = 100000
        nome_direto = "Paulo Bragança"
        resultado = 90000.0

        funcionario = Funcionario(nome_direto, '07-09-1990', salario)

        funcionario.decrescimo_salario

        result = funcionario.salario

        assert result == resultado

    def test_calcular_bonus_positivo(self):
        # Testando o caso do bonus ser ativo.

        salario = 1000
        nome_direto = "Ana Liz"
        resultado = 100

        funcionario = Funcionario(nome_direto, '07-09-1990', salario)

        bonus = funcionario.calcular_bonus()

        assert resultado == bonus
