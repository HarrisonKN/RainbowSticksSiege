import pygame

class Player():
    def __init__(self, x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3 #cant be 0.X

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: #left
            self.x -= self.vel
        
        if keys[pygame.K_d]: #Right
            self.x += self.vel

        if keys[pygame.K_s]: #down
            self.y += self.vel

        if keys[pygame.K_w]: #up
            self.y -= self.vel
        
        self.update()

    def update(self):
        self.rect = (self.x,self.y,self.width,self.height)