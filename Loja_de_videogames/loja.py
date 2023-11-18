class LojaVideogame:
    def __init__(self):
        self.consoles = []
        self.acessorios = []
        self.jogos = []
        self.checkout = []

    def comprar_consoles(self):
        print("=============CONSOLES/COMPUTADORES=============\nNintendo Switch -- R$2000 [1]\nPlaystation 5 -- R$ 3800 [2]\nXbox Series X -- R$ 3800 [3]\nPC gamer -- R$ 10000 [4]\nNotebook Gamer -- R$8000 [5]")
        console = int(input("Selecione o console desejado: "))
        if console == 1:
            console_preco = 2000
        elif console == 2:
            console_preco = 3800
        elif console == 3:
            console_preco = 3800
        elif console == 4:
            console_preco = 10000
        elif console == 5:
            console_preco = 8000
        else:
            print("Opção Inválida! Tente Novamente")

    def comprar_acessorios(self):
        acessorios = int(input("=============ACESSÓRIOS E PERIFÉRICOS=============\nMicrofone -- R$300 [1]\nHeadset -- R$300 [2]\nControle Xbox -- R$350 [3]\nControle PS5 -- R$350 [4]\nMouse -- R$120 [5]\nTeclado -- R$200 [6]\nWebcam -- R$300 [7]"))
        if acessorios == 1:
            acessorio_preco = 300
        elif acessorios == 2:
            acessorio_preco = 300
        elif acessorios == 3:
            acessorio_preco = 350
        elif acessorios == 4:
            acessorio_preco = 350
        elif acessorios == 5:
            acessorio_preco = 120
        elif acessorios == 6:
            acessorio_preco = 200
        elif acessorios == 7:
            acessorio_preco = 300

    def comprar_jogos(self):
        plataforma = int(input("=============SELECIONE A PLATAFORMA DESEJADA=============\nNintendo Switch [1]\nXbox [2]\nPlaystation [3]\nComputador [4]\nSelecione a plataforma desejada: "))
        if plataforma == 1:
            plataforma = str("Jogo nintendo switch")
            print("=======JOGOS DE NINTENDO SWITCH=======\nThe Legend of Zelda: Tears of the Kingdom -- R$250 [1]\nAnimal Crossing: New Horizons -- R$250 [2]\nSuper Mario Odyssey -- R$250 [3]\nSuper Smash Bros. Ultimate -- R$250 [4]\nSplatoon 3 -- R$250 [5]")
            int(input("Selecione o jogo a ser comprado: "))
            jogo_preco = 250
        elif plataforma == 2:
            print("=======JOGOS DE XBOX=======\nDiablo IV -- R$300 [1]\nStarfield -- R$300 [2]\nElden Ring -- R$300 [3]\nMortal Kombat 1 -- R$300 [4]")
            int(input("Selecione o jogo a ser comprado: "))
            jogo_preco = 300
        elif plataforma == 3:
            print("=======JOGOS DE PLAYSTATION=======\nBaldur's Gate III -- R$300 [1]\nMarvel's Spider-Man 2 -- R$300 [2]\nElden Ring -- R$300 [3]\nFinal Fantasy XVI -- R$300 [4]\nGod of War Ragnarök -- R$300 [5]")
            int(input("Selecione o jogo a ser comprado: "))
            jogo_preco = 300

        elif plataforma == 4:
            print("=======JOGOS DE COMPUTADOR=======\nBaldur's Gate III -- R$250 [1]\nHorizon Forbidden West -- R$250 [2]\nElden Ring -- R$250 [3]\nRed Dead Redemption 2 -- R$250 [4]\nResident Evil 4 Remake -- R$250 [5]")
            int(input("Selecione o jogo a ser comprado: "))
            jogo_preco = 300
        else:
            print("Opção Inválida! Tente novamente")

    def fazer_checkout(self):
        total = jogo_preco + acessorio_preco + console_preco
        print(f"==========CONTA==========\nCONSOLES/COMPUTADORES -- R${console_preco}\nACESSÓRIOS E PERIFÉRICOS -- R${acessorio_preco}\nJOGOS -- R${jogo_preco}\n====================\nTOTAL -- R${total}")