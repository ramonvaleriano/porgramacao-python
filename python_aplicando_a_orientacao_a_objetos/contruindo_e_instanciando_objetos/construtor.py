"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: contruindo_e_instanciando_objetos
    Arquivo: restaurante.py
    Dado: Aprendendo o que são construtores
"""

# Puxando a classe restaurante.
from modelos.restaurante import Restaurante

# Instanciando a classe.
restaurante_praca = Restaurante('Praça', 'Gourmet')

# Testando.
print('Testando dado: ')
print(f" Nome: {restaurante_praca.nome}\n Categoria: {restaurante_praca.categoria}\n Ativo: {restaurante_praca.ativo}\n")