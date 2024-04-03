"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: classes
    Arquivo: restaurante.py
    Dado: 
"""

class Restaurante:

    def __init__(self, nome: str, categoria: str, ativo: bool = False):
        self.__nome: str = nome.lower()
        self.__categoria: str = categoria.lower()
        self.__ativo: bool = ativo


    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def ativo(self):
        return self.__ativo

    @property
    def atividade(self):
        mensagem = "Restaurante inativo -- {self.__ativo}"

        if self.__ativo:
            mensagem = f"Restaurante Ativo -- {self.__ativo}"

        return mensagem
    
    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def dado_restaurante(self):
        restaurante = {
            "nome": self.nome,
            "categoria": self.categoria,
            "atividade": self.atividade
        }
        return restaurante
    
    def altera_nome(self, novo_nome):
        self.__nome = novo_nome
        return self.__nome

    def altera_status(self, novo_status: bool):
        self.__ativo = novo_status
        return self.__ativo