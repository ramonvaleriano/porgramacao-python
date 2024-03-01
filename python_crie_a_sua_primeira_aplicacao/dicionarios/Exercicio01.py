"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Dicionarios
    Arquivo: exercicio01.py
    Dado: Crie um dicionário representando informações sobre uma pessoa,
          como nome,
          idade e
          cidade.
"""

def identidade(nome, idade, cidade):
    dado = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

    return dado

def solicita_dados():
    nome = input('Digit o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    cidade = input('Cidade da pessoa: ')

    return nome, idade, cidade

# Resolução da quetão.
nome, idade, cidade = solicita_dados()
identidade_response = identidade(nome, idade, cidade)

print(identidade_response)