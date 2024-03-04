"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: contruindo_e_instanciando_objetos\modelos
    Arquivo: restaurante.py
    Dado: Classe modelo para restaurante.
"""

class Restaurante:

    def __init__(self, nome: str, categoria: str, ativo: bool = False) -> None:
        self.nome: str = nome
        self.categoria: str = categoria
        self.ativo: bool = ativo

