import pygame

class Obstacle(pygame.sprite.Sprite):
    
    def __init__(self, speed, ground_y_obstacle):
        super().__init__()
        self.speed = speed 
        self.image = pygame.image.load('assets/sprites/obstacle/barriere.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.bottom = ground_y_obstacle
        
