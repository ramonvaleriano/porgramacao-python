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
restautante_churrasco = Restaurante('Vaca','Gostosa', True)

# Testando.
print('Testando dado: ')
print(f"Nome: {restaurante_praca.nome}")
print(f"Categoria: {restaurante_praca.categoria}")
print(f"Atividade: {restaurante_praca.ativo}")
print(f"{restaurante_praca.__str__()}")

# Validando essa lista de dados dentro do objeto
print('\n')
Restaurante.exibir_restaurantes()

# Mudando o status.
restaurante_praca.mudar_status(True)
print(restaurante_praca.__str__())