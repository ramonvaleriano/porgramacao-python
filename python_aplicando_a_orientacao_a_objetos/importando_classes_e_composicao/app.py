from modelos.restaurante import Restaurante

def main():
    restaurante_japonse = Restaurante('Japa', 'Japonesa')
    restaurante_mexicano = Restaurante('Mexicano Food', 'Comida Méxicana')
    restaurante_praca = Restaurante('Praça', 'Gourmet, True')

    restaurante_japonse.adicionar_avaliacao('Milla', 10)
    restaurante_japonse.adicionar_avaliacao('Ramon', 7)


if __name__ == '__main__':
    main()
    Restaurante.exibir_restaurantes()
    