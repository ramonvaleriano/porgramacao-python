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
