"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: contruindo_e_instanciando_objetos\modelos
    Arquivo: restaurante.py
    Dado: Classe modelo para restaurante.
"""

class Restaurante:
    restaurantes = list()

    def __init__(self, nome: str, categoria: str, ativo: bool = False):
        self.__nome: str = nome
        self.__categoria: str = categoria
        self.__ativo: bool = ativo
        Restaurante.restaurantes.append(self)

    @property
    def nome(self):
        return self.__nome
    
    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def ativo(self):
        return self.__ativo
    
    def __str__(self) -> str:
        mensagem = f"Classe: Restaurante; Dados: {self.nome} | {self.categoria} | {self.ativo}"
        return mensagem
    
    def exibir_restaurantes():
        for restaurente in Restaurante.restaurantes:
            print(restaurente.__str__())

