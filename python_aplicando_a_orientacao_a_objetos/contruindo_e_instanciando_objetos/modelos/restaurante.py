"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: contruindo_e_instanciando_objetos\modelos
    Arquivo: restaurante.py
    Dado: Classe modelo para restaurante.
"""

class Restaurante:

    def __init__(self, nome: str, categoria: str, ativo: bool = False):
        self.__nome: str = nome
        self.__categoria: str = categoria
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
    
    
