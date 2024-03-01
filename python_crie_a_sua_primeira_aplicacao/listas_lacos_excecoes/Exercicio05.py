"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Lista, laços e exeções
    Arquivo: exercicio05.py
    Dado: Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número,
          indo de 1 a 10.
"""

# Funções para resolver os exercícios:
def validador_de_numero(possivel_numero):
    try:
        numero = float(possivel_numero)
        
        return numero
    
    except:
        print('Não é um número.')
        return False


def solicita_numero():
    validando = True
    contador = 0
    numero = False

    while validando and contador < 3:
        possivel_numero = input('Digite um número deseajdo: ')
        numero = validador_de_numero(possivel_numero)
        
        if numero:
            validando =  False
        
        contador += 1

        if contador == 3:
            print('Você ultrapassou a quantidade máxima de tentativa')
            return False
    
    return numero


def tabuada(numero):

    if not numero:
        return None

    for dado in range(1, 11):
        result = numero * dado
        print(f"{numero} * {dado} = {result}")

# Testando solução.
numero = solicita_numero()
tabuada(numero)