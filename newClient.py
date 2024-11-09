import pygame
from player import Player
from newNetwork import Network


width = 720
height = 480

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("CLIENT")


def redrawWindow(win, player1, player2): #Updates the window
    win.fill((255,255,255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()


def main(): #runs the game loop checking for things
    run = True
    nNetwork = Network()

    player1 = nNetwork.getPos()

    clock = pygame.time.Clock()



    while run:
        clock.tick(60)

        player2 = nNetwork.send(player1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()

        player1.move()
        redrawWindow(win, player1, player2)


main()