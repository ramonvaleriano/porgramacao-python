"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Modulos e Funções
    Arquivo: controllers.py
    Dado: Controledores de fluxos
"""

import os

def finaliza_app():
    os.system('cls')
    print('Finalizando o APP.')

def controle_de_opcoes(opcao, validador):
    if validador:
        match opcao:
            case 1:
                print("Cadastrar Restaurante")

            case 2:
                print("Listar Restaurantes")

            case 3:
                print("Ativar Restaurante")

            case 4:
                print("Sair do APP.")

                finaliza_app()
        
    else:
        print("Opção invalida.")
    