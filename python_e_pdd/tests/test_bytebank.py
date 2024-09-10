from bytebank import Funcionario

class TestClass:
    def test_caso_positivo_com_data_adequada(self):
        maria = Funcionario('Maria Lopes', '14/09/1989', 3000)

        result = maria.idade()

        assert result == 35