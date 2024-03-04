"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: classes
    Arquivo: Exercicio05.py
    Dado: Altere o valor do atributo nome para 'Bistrô'.
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