import pygame
from player import Player
from newNetwork import Network
from character import Character


width = 720
height = 480

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("CLIENT")


def redrawWindow(win, player1, player2, character): #Updates the window
    win.fill((255,255,255))
    player1.draw(win)
    player2.draw(win)

    character.update(pygame.key.get_pressed())
    win.blit(character.image, character.rect)

    pygame.display.update()


def main(): #runs the game loop checking for things
    run = True
    nNetwork = Network()

    player1 = nNetwork.getPos()

    character = Character(100, 100, 'RainbowSticksSiege/Images/Characters/Fighter/Idle.png', speed=5, rows=2, columns=4)

    clock = pygame.time.Clock()



    while run:
        clock.tick(60)

        player2 = nNetwork.send(player1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()

        player1.move()
        redrawWindow(win, player1, player2, character)

    pygame.quit()


main()