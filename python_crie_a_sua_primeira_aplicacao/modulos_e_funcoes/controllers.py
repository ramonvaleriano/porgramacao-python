"""
    Curso: Python: Crie a sua primeira Aplicação
    Diretório: Modulos e Funções
    Arquivo: controllers.py
    Dado: Controledores de fluxos
"""

import os
from listas_lacos_excecoes.utils import (
    cadastrar_restaurantes,
    listar_restaurantes,
    ativar_restaurente
)

def finaliza_app():
    os.system('cls')
    print('Finalizando o APP.')

def controle_de_opcoes(opcao, validador, lista_restaurantes=list()):
    if validador:
        match opcao:
            case 1:
                print("Cadastrar Restaurante: ")
                restaurante = input('Digite o nome do restaurante: ')
                status = input('Digite o status do restaurante')

                lista_restaurantes = cadastrar_restaurantes(
                    lista_restaurantes,
                    restaurante,
                    status
                )

                print('Restaurante adicionado')
                
            case 2:
                print("Listar Restaurantes")

            case 3:
                print("Ativar Restaurante")

            case 4:
                print("Sair do APP.")

                finaliza_app()
        
    else:
        print("Opção invalida.")
    