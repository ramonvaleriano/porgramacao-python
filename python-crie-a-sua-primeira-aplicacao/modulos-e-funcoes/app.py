"""
    Aplicação principal
"""

from validadores import (
    valida_opcoes,
    valida_inteiro
)

from controllers import (
    finaliza_app
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
    if opcao_esolhida == 1:
        print("Cadastrar Restaurante")

    elif opcao_esolhida == 2:
        print("Listar Restaurantes")

    elif opcao_esolhida == 3:
        print("Ativar Restaurante")

    elif opcao_esolhida == 4:
        print("Sair do APP.")
        finaliza_app()

else:
    print("Opção invalida.")

finaliza_app()