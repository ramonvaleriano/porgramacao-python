"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: classes
    Arquivo: Exercicio01.py
    Dado: Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
"""

# Importando modelos
from modelos.restaurante import Restaurante

# Resolvendo questão
restaurente_modelo = Restaurante('Modelo', 'restaurante_praca', True)

print('Validando se os dados foram inseridos de fato')
print(f"Nome: {restaurente_modelo.nome} -- Categoria: {restaurente_modelo.categoria} -- Ativo: {restaurente_modelo.ativo}")