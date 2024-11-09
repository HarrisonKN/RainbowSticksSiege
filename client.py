import pygame
from player import Player

pygame.init()

width = 1280
height = 720

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("CLIENT")

clientNumber = 0 #holds current client

def redrawWindow(win, player): #Updates the window
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

def main(): #runs the game loop checking for things
    run = True

    player = Player(50,50,100,100, (0,0,255))



    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()

        player.move()
        redrawWindow(win, player)


main()