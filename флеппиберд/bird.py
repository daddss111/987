import pygame

class Bird:
    def __init__(self):
        
        self.image = pygame.transform.scale(pygame.image.load('image/bird/bird.png'), (50, 65)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.inflate_ip(-15, -15) 
       
        self.rect.x = 100
        self.rect.y = 300
        
        self.speed = 0 
        self.gravity = 0.4 

    def update(self):
        
        self.speed += self.gravity
        self.rect.y += self.speed

        if self.rect.y < 0:
            self.rect.y = 0
            self.speed = 0

    def jump(self):
        
        self.speed = -7

    def draw(self, window):
        window.blit(self.image, self.rect)