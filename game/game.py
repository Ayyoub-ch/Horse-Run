import pygame
from game.horse import Horse
from game.obstacle import Obstacle

class Game:
    
    def __init__(self):
        # générer le joueur
        self.horse = Horse("Spirit", 10)
        self.obstacle = Obstacle("Barriere", 10)
        self.screen = pygame.display.set_mode((1480, 820))
        self.background = pygame.image.load("assets/sprites/background/background2.png")
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


    def update(self, screen):
        dt = clock.tick(60) / 16

        # Mettre à jour la physique du cheval
        self.horse.update(dt, self.horse.ground_y)

        self.screen.blit(self.background_play, (0, 0)) #injecter l'arrière plan dans la fenêtre de jeu
        
        # Appliquer l'image du joueur dans la fenêtre de jeu
        self.screen.blit(self.horse.image, self.horse.rect) #injecter le joueur dans la fenêtre de jeu
        
        # Appliquer l'image de l'obstacle dans la fenêtre de jeu
        self.screen.blit(self.obstacle.image, self.obstacle.rect) #injecter l'obstacle dans la fenêtre de jeu
        
        # Vérifier si le joueur saute
        if self.pressed_keys[pygame.K_SPACE] and self.horse.rect.x + self.horse.rect.width < self.screen.get_width() and self.horse.rect.y < 720: # Si la touche espace est appuyée
            self.horse.jump() # Le cheval saute

        # Vérifier la collision entre le cheval et l'obstacle
        if self.horse.rect.colliderect(self.obstacle.rect):
            print("Collision détectée !")
        
        # Afficher le score et la distance parcourue
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        metre_text = font.render(f"Distance: {self.metre} m", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(metre_text, (10, 50))
