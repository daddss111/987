import pygame
import random

class Pillar:
    def __init__(self, x):
        
        self.image_bottom = pygame.transform.scale(pygame.image.load('image/pillar/pillar.png'), (130, 640)).convert_alpha()
        self.image_top = pygame.transform.flip(self.image_bottom, False, True)
        
        self.rect_bottom = self.image_bottom.get_rect()
        self.rect_top = self.image_top.get_rect()


        self.rect_bottom.inflate_ip(-70, -45)
        self.rect_top.inflate_ip(-70, -45)
        
        self.gap = 365
        self.x = x
        self.reset_position()
        self.speed = 4

    def reset_position(self):
        
        random_y = random.randint(240, 460)
        
        
        self.rect_bottom.x = self.x
        self.rect_bottom.y = random_y + (self.gap // 2)
        
       
        self.rect_top.x = self.x
        self.rect_top.y = random_y - (self.gap // 2) - 500 

    def update(self):
        self.rect_bottom.x -= self.speed
        self.rect_top.x -= self.speed
                       
        if self.rect_bottom.x < -450:
                               
            self.rect_bottom.x += 2450 
            self.rect_top.x += 2650
            self.reset_position() 
    def draw(self, window):
        window.blit(self.image_bottom, self.rect_bottom)
        window.blit(self.image_top, self.rect_top)