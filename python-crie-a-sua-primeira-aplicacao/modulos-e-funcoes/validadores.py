"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Modulos e Funções
    Arquivo: validadores.py
    Dado: Realiza as validações que precisamos.
"""

def valida_opcoes(lista_de_opcoes, opcao):
    if opcao not in lista_de_opcoes:
        print(f"Opção não é compativel ao Menu: {opcao} ")
        return False
    
    print("Opção Encontrada.")
    return True

def valida_inteiro(variavel):
    try:
        variavel = int(variavel)
        return variavel
    except:
        print('Esse número não é um inteiro.')
        return variavel