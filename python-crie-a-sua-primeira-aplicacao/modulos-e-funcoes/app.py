"""
    Aplicação principal
"""

from validadores import (
    valida_opcoes,
    valida_inteiro
)

print("""
      

█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      
""")

print("1 - Cadastrar Restaurente")
print("2 - Listar Restaurente")
print("3 - Ativar Restaurente")
print("4 - Sair do Restaurante")

print('\n')

opcao_esolhida = input("Digte a opção desejada: ")
opcao_esolhida = valida_inteiro(opcao_esolhida)

print(f"A opção desejado é: {opcao_esolhida}")

opcoes = [1, 2, 3, 4]
    
validacao_das_opcoes = valida_opcoes(opcoes, opcao_esolhida)

if validacao_das_opcoes:
    print('Deu bom!')
