"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Manipulação de Strings
    Arquivo: exercicio02.py
    Dado: Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
"""

# Usando um função para realizar esse processo
def coleta_variavel(mensagem):
    variavel = input(mensagem)

    return variavel


def nome_idade(nome, idade):
    print(f"Meu nome: {nome} e tenho {idade} anos.")


# Testando o desejado.
    
nome = coleta_variavel("Qual o seu nome: ")
idade = coleta_variavel("Qual a sua idade: ")

nome_idade(nome, idade)
