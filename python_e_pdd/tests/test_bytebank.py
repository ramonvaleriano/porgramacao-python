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
