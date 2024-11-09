import pygame
from player import Player
from network import Network

pygame.init()

width = 1280
height = 720

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("CLIENT")

clientNumber = 0 #holds current client

def redrawWindow(win, player1, player2): #Updates the window
    win.fill((255,255,255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()

def read_position(str):
    str = str.split(",")
    return int(str[0]),int(str[1])

def send_position(tup):
    return str(tup[0]) + "," +str(tup[1])


def main(): #runs the game loop checking for things
    run = True
    nNetwork = Network()
    startPosition = read_position(nNetwork.getPos()) #gets numbers from server and converts them to usable numbers
    player1 = Player(startPosition[0],startPosition[1],100,100, (0,0,255)) #puts the server positions for player in the players position
    player2 = Player(0,0,100,100, (0,255,0))

    clock = pygame.time.Clock()



    while run:
        clock.tick(60)

        player2Pos = read_position(nNetwork.send(send_position((player1.x, player1.y))))
        player2.x = player2Pos[0]
        player2.y = player2Pos[1]
        player2.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()

        player2.move()
        redrawWindow(win, player1, player2)


main()