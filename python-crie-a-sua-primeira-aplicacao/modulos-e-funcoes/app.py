"""
    Aplicação principal
"""

from utils import (
    mensagem_principal,
    entrada_de_dados,
    mensagem_opcoes,
)

from validadores import (
    valida_opcoes,
    valida_inteiro
)

from controllers import (
    finaliza_app
)


def main():
    mensagem_principal()
    mensagem_opcoes()

    opcao_esolhida = entrada_de_dados("Digte a opção desejada: ")
    opcao_esolhida = valida_inteiro(opcao_esolhida)

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

if __name__ == '__main__':
    main()