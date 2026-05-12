import pygame
from bird import Bird
from pillar import Pillar
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 50, bold=True)
pygame.display.set_caption('flappybird')

window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load('image/bg/bg.jpg'), (800, 800)).convert_alpha()
bird = Bird()
pillars = [
    Pillar(1400),  
    Pillar(2070), 
    Pillar(2450)  
]
score = 0
passed = False 
play = True
while play:
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    
    for p in pillars:
        p.update()
        p.draw(window)

        
        if bird.rect.colliderect(p.rect_bottom) or bird.rect.colliderect(p.rect_top) or bird.rect.y >= 750:
            print(f"Игра окончена! Твой счет: {score}")
            pygame.time.delay(1000)
            play = False

        
        if not hasattr(p, 'passed'): p.passed = False 
        
        if bird.rect.x > p.rect_bottom.x + 80 and not p.passed:
            score += 1
            p.passed = True
        
        if p.rect_bottom.x > 850: 
            p.passed = False
    
    bird.update()
    bird.draw(window)

   
    score_img = font.render(f"Счёт: {score}", True, (135, 0, 225))
    window.blit(score_img, (200, 50))

    pygame.display.update()
    clock.tick(60)