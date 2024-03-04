"""
    Curso: Python: Aplicando a Orientação a Objetos
    Diretório: classes
    Arquivo: Exercicio07.py
    Dado: Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
          Mude o estado da instância restaurante_pizza para ativo.
          Imprima no console o nome e a categoria da instância restaurante_praca.
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

restaurente_fast = Restaurante('Pizza Place', 'Fast Food', False)
print(f"Nome: {restaurente_fast.nome} -- Categoria: {restaurente_fast.categoria} -- Ativo: {restaurente_fast.ativo}")
print(f"A atividade: {restaurente_fast.atividade}")
print(f"A categória: {restaurente_fast.categoria}")

test = 'Fast Food'
if restaurente_fast.categoria == test.lower():
    print('É sim!')


novo_ativo = restaurente_fast.altera_status(True)
print(f"A ativo: {restaurente_fast.ativo}")
