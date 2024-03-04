"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: classes
    Arquivo: Exercicio06.py
    Dado: Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o
          nome 'Pizza Place' e categoria 'Fast Food'.
"""

# Importando modelos
from modelos.restaurante import Restaurante

# Resolvendo questão
restaurente_modelo = Restaurante('Modelo', 'restaurante_praca', True)

print('Validando se os dados foram inseridos de fato')
print(f"Nome: {restaurente_modelo.nome} -- Categoria: {restaurente_modelo.categoria} -- Ativo: {restaurente_modelo.ativo}")
print(f"A atividade: {restaurente_modelo.atividade}")
print(f"A categória: {restaurente_modelo.categoria}")

novo_nome = restaurente_modelo.altera_nome('Pastelaria Eudrem')

print(f"Novo nome: {novo_nome}")
print(f"Nome: {restaurente_modelo.nome} -- Categoria: {restaurente_modelo.categoria} -- Ativo: {restaurente_modelo.ativo}")

restaurente_modelo = Restaurante('Pizza Place', 'Fast Food', True)
print(f"Nome: {restaurente_modelo.nome} -- Categoria: {restaurente_modelo.categoria} -- Ativo: {restaurente_modelo.ativo}")
print(f"A atividade: {restaurente_modelo.atividade}")
print(f"A categória: {restaurente_modelo.categoria}")
