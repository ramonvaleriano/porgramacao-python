"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: contruindo_e_instanciando_objetos\modelos
    Arquivo: restaurante.py
    Dado: Classe modelo para restaurante.
"""
from modelos.avaliacao import Avaliacao


class Restaurante:
    restaurantes = list()

    def __init__(self, nome: str, categoria: str, ativo: bool = False):
        self.__nome: str = nome
        self.__categoria: str = categoria
        self.__ativo: bool = ativo
        Restaurante.restaurantes.append(self)
        self._avaliacao = list()

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
    
    @classmethod
    def exibir_restaurantes(cls):
        for restaurente in cls.restaurantes:
            print(restaurente.__str__())

    def mudar_status(self, status_bool):
        self.__ativo = status_bool
        return self.__ativo
    
    def adicionar_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)

        media = round(soma_das_notas / quantidade_notas)

        return media 
