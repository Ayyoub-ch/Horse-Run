import pygame
from game.game import Game

pygame.init()
clock = pygame.time.Clock()

# Générer la fenêtre de jeu
pygame.display.set_caption("Horse Run", "1.0")
screen = pygame.display.set_mode((1480, 1020))

# Définir la position du sol
ground_y = 1114
ground_y_obstacle = 1080



# Importer l'arrière-plan du jeu
background = pygame.image.load("assets/sprites/background/background2.png")
background_after = pygame.image.load("assets/sprites/background/background_afternoon.png")
background_night = pygame.image.load("assets/sprites/background/background_night.png")

# Charger le jeu
game = Game()

# Positionner l'obstacle au sol dès le départ
game.obstacle.rect.bottom = ground_y_obstacle


# positionner le cheval au sol dès le départ
if game.horse.ground_y is None:
    game.horse.ground_y = ground_y
game.horse.rect.bottom = ground_y

running = True

# Boucle de jeu tant que running est vrai
while running:
    dt = clock.tick(60) / 16

    # Mettre à jour la physique du cheval
    game.horse.update(dt, ground_y)

    # Afficher l'arrière-plan du jeu
    game.screen.blit(game.background, (0, 0)) #injecter l'arrière plan dans la fenêtre de jeu
    
    # Appliquer l'image du joueur dans la fenêtre de jeu
    game.screen.blit(game.horse.image, game.horse.rect) #injecter le joueur dans la fenêtre de jeu
    
    # Appliquer l'image de l'obstacle dans la fenêtre de jeu
    game.screen.blit(game.obstacle.image, game.obstacle.rect) #injecter l'obstacle dans la fenêtre de jeu
    
    # Vérifier si le joueur saute
    if game.pressed_keys[pygame.K_SPACE] and game.horse.rect.x + game.horse.rect.width < screen.get_width() and game.horse.rect.y < 720: # Si la touche espace est appuyée
        game.horse.jump() # Le cheval saute

    # Vérifier la collision entre le cheval et l'obstacle
    if game.horse.rect.colliderect(game.obstacle.rect):
        print("Collision détectée !")
    
    # Afficher le score et la distance parcourue
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {game.score}", True, (255, 255, 255))
    metre_text = font.render(f"Distance: {game.metre} m", True, (255, 255, 255))
    game.screen.blit(score_text, (10, 10))
    game.screen.blit(metre_text, (10, 50))
    
    #mettre à jour la fenêtre de jeu
    # Important : cette ligne doit être à la fin de la boucle de jeu pour que tous les éléments soient affichés avant de rafraîchir l'écran
    pygame.display.flip() 
    
    # Si le joueur ferme la fenêtre, on arrête le jeu
    for event in pygame.event.get():
        # vérifier que l'évenement est "fermeture de la fenêtre"
        if event.type == pygame.QUIT: # Si le joueur ferme la fenêtre
            running = False
            pygame.quit() # Fermer la fenêtre de jeu
            print("Fermeture du jeu")
            
        # Si le joueur appuie sur une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed_keys[event.key] = True
            print("Touche ESPACE appuyee : ", event.key, " - Le cheval saute !")
            
        # Si le joueur relâche une touche du clavier
        elif event.type == pygame.KEYUP:
            game.pressed_keys[event.key] = False
            print("Touche ESPACE relachee : ", event.key, " - Le cheval redescend !")
            
    
    # Condition pour changer l'arrière-plan en fonction de la distance parcourue
    # Boucle afin que cela se répète à chaque fois que le cheval avance
    
