import pygame
from game.horse import Horse
from game.obstacle import Obstacle

class Game:
    
    def __init__(self):
        # générer le joueur
        self.horse = Horse("Spirit", 10)
        self.obstacle = Obstacle("Barriere", 10)
        self.screen = pygame.display.set_mode((1080, 720))
        self.background = pygame.image.load("assets/sprites/background/background.png")
        self.pressed_keys = {
            pygame.K_SPACE: False,
        }
        self.score = 0
        self.metre = 0
        
    def metre_passed(self):
        # à chaque fois que le cheval avance, on incrémente la distance parcourue
        if self.horse.rect.right > self.obstacle.rect.left:
            self.metre += 1
        
    def score(self):
        # mettre condition que le cheval a passé l'obstacle
        if self.horse.rect.right > self.obstacle.rect.left:
            self.score += 1
