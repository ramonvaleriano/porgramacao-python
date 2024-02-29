"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Modulos e Funções
    Arquivo: exercicio02.py
    Dado: Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else
          para classificar a idade em categorias de acordo com as seguintes condições:

            Criança: 0 a 12 anos;
            Adolescente: 13 a 18 anos;
            Adulto: acima de 18 anos.
"""

# Desenvolvendo função para resolver esse caso:
def margem_de_idade(idade):
    print(f"Idade: {idade}")
    if type(idade) == int or type(idade) == float:
        if idade >= 0 and idade <= 12:
            print('Criança.')
        
        elif idade >= 13 and idade <= 18:
            print('Adolecente.')

        elif idade > 18:
            print('Adulto')

        else:
            print('Não exite essa idade')


if __name__ == '__main__':
    idade = 2
    margem_de_idade(idade)
    idade = 15 
    margem_de_idade(idade)
    idade = 28
    margem_de_idade(idade)
    idade = -1
    margem_de_idade(idade)