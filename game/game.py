import pygame
from game.horse import Horse
from game.obstacle import Obstacle
clock = pygame.time.Clock()

class Game:
    
    def __init__(self):
        # Définit si le jeu a commencé ou non
        self.is_playing = False
        
        # générer le joueur
        self.horse = Horse("Spirit", 10)
        # générer l'obstacle
        self.obstacle = Obstacle("Barriere", 10)
        # générer la fenêtre de jeu
        self.screen = pygame.display.set_mode((1480, 720))
        
        # Importer l'arrière plan de l'écran de menu
        self.background = pygame.image.load("assets/sprites/background/background.png")
        
        # Importer l'arrière plan du jeu
        self.background_play = pygame.image.load("assets/sprites/background/background_long.png").convert()
        self.background_after = pygame.image.load("assets/sprites/background/background_afternoon.png").convert()
        self.background_night = pygame.image.load("assets/sprites/background/background_night.png").convert()
        self.background_x = 0
        self.background_speed = 5
        
        # Dictionnaire des touches pressées
        self.pressed_keys = {
            pygame.K_SPACE: False,
        }
        
        # Score et distance parcourue
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
    
            
    def scroll_background(self):
        # Défiler le background_play de façon infinie
        self.background_x -= self.background_speed # faire défiler le background vers la gauche
        if self.background_x <= -self.background_play.get_width(): # si le background a complètement défilé vers la gauche
            self.background_x = 0 # réinitialiser la position du background pour qu'il recommence à défiler

        self.screen.blit(self.background_play, (self.background_x, 0)) # afficher le background à la position actuelle
        self.screen.blit(self.background_play, (self.background_x + self.background_play.get_width(), 0)) # afficher une deuxième copie du background juste à côté de la première pour créer l'illusion d'un défilement continu

    # Condition pour changer l'arrière-plan en fonction de la distance parcourue
    # Boucle afin que cela se répète à chaque fois que le cheval avance
    def background_change(self):
        if self.metre < 100:
            self.screen.blit(self.background_play, (0, 0))
        elif self.metre < 200:
            self.screen.blit(self.background_after, (0, 0))
        else:
            self.screen.blit(self.background_night, (0, 0))
        
        
                
        
    def update(self, screen):
        dt = clock.tick(60) / 16

        # Mettre à jour la physique du cheval
        self.horse.update(dt, self.horse.ground_y)

        self.background_change()
        self.scroll_background()

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
        
    # def game_over(self):
    #     if self.horse.rect.colliderect(self.obstacle.rect):
    #         print("Game Over !")
    #         # réinitialiser le jeu
    #         self.is_playing = False
    #         self.score = 0
    #         self.metre = 0
    #         self.horse.rect.x = -250
    #         self.horse.rect.bottom = self.horse.ground_y
    #         self.obstacle.rect.x = 1000