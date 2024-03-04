"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: classes
    Arquivo: Exercicio04.py
    Dado: Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e
          armazene em uma variável chamada categoria.
"""

# Importando modelos
from modelos.restaurante import Restaurante

# Resolvendo questão
restaurente_modelo = Restaurante('Modelo', 'restaurante_praca', True)

print('Validando se os dados foram inseridos de fato')
print(f"Nome: {restaurente_modelo.nome} -- Categoria: {restaurente_modelo.categoria} -- Ativo: {restaurente_modelo.ativo}")
print(f"A atividade: {restaurente_modelo.atividade}")
print(f"A categória: {restaurente_modelo.categoria}")