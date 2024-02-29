"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Lista, laços e exeções
    Arquivo: exercicio02.py
    Dado: Crie uma lista para cada informação a seguir:

        Lista de números de 1 a 10;
        Lista com quatro nomes;
        Lista com o ano que você nasceu e o ano atual.
"""

# Funções para resolver os exercícios:

def lista_desejado(inicial, final):
    lista_desejado = list()
    if inicial and final:
        lista_desejado = list(range(inicial, final+1))

    return lista_desejado

def lista_nome(quantidade):
    lista_desejada = list()
    if quantidade:
        for i in range(quantidade):
            nome = input(f"Digite o nome  {i}: ")
            lista_desejada.append(nome)

    return lista_desejada

def lista_dados_pessoais():
    ano_nascimento = int(input("Qual o ano que você nasceu: "))
    ano_atual = int(input("Qual ano que você se encontra"))

    return [ano_nascimento, ano_atual]
