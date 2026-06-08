import pygame
from game.game import Game

pygame.init()
clock = pygame.time.Clock()

# Générer la fenêtre de jeu
pygame.display.set_caption("Horse Run", "1.0")
screen = pygame.display.set_mode((1080, 720))

# Définir la position du sol
ground_y = 1000


# Importer l'arrière-plan du jeu
background = pygame.image.load("assets/sprites/background/background.png")

# Charger le jeu
game = Game()
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
    
    # Vérifier si le joueur saute
    if game.pressed_keys[pygame.K_SPACE] and game.horse.rect.x + game.horse.rect.width < screen.get_width() and game.horse.rect.y < 720: # Si la touche espace est appuyée
        game.horse.jump() # Le cheval saute

    
    #mettre à jour la fenêtre de jeu
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
            print("Touche appuyee : ", event.key)
            
        # Si le joueur relâche une touche du clavier
        elif event.type == pygame.KEYUP:
            game.pressed_keys[event.key] = False
            print("Touche relachee : ", event.key)