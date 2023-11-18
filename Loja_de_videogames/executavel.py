import sys

from loja import LojaVideogame

loja = LojaVideogame()

while True:

    print("\n=============BEM VINDO(A) A =============")

    print("=============MENU DE NAVEGAÇÃO=============\nConsoles/Computadores -- [1]\nAcessórios -- [2]\nJogos -- [3]\nFazer Checkout -- [4]\nSair -- [5]")
    opcao = int(input("Selecione o menu desejado: "))

    match opcao:
        case 1:
            loja.comprar_consoles()
        case 2:
            loja.comprar_acessorios()
        case 3:
            loja.comprar_jogos()
        case 4:
            loja.fazer_checkout()
        case 5:
            sys.exit()
            break