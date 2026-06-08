import pygame
from game.game import Game

pygame.init()

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

# importer la bannière du jeu
banner = pygame.image.load("assets/sprites/menu/banner.png")
banner = pygame.transform.scale(banner, (900, 500)) # redimensionner la bannière pour qu'elle soit plus petite
banner_rect = banner.get_rect() # position de la bannière dans la fenêtre de jeu
banner_rect.x = screen.get_width() / 2 - banner_rect.width / 2 # centrer la bannière horizontalement

# importer le bouton de jeu
play_button = pygame.image.load("assets/sprites/menu/play_button.png")
play_button = pygame.transform.scale(play_button, (500, 250)) # redimensionner le bouton de jeu pour qu'il soit plus petit
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 2 - play_button_rect.width / 2
play_button_rect.y = banner_rect.y + banner_rect.height - 20

# importer le bouton d'option
option_button = pygame.image.load("assets/sprites/menu/option_button.png")
option_button = pygame.transform.scale(option_button, (500, 250)) # redimensionner le bouton d'option pour qu'il soit plus petit
option_button_rect = option_button.get_rect()
option_button_rect.x = screen.get_width() / 2  - 800
option_button_rect.y = banner_rect.y + banner_rect.height - 25

# importer le bouton de shop
shop_button = pygame.image.load("assets/sprites/menu/shop_button.png")
shop_button = pygame.transform.scale(shop_button, (500, 250)) # redimensionner le bouton de shop pour qu'il soit plus petit
shop_button_rect = shop_button.get_rect()
shop_button_rect.x = screen.get_width() / 2  + 200
shop_button_rect.y = banner_rect.y + banner_rect.height - 25

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
    
    # Afficher l'arrière-plan du jeu
    game.screen.blit(game.background, (0, 0)) #injecter l'arrière plan dans la fenêtre de jeu
    
    # Vérifier si notre jeu a commencé ou pas
    if game.is_playing:
        # Mettre à jour le jeu (déclencher l'affichage du joueur, de l'obstacle, etc.)
        game.update(screen) 
    else:
        # Afficher la bannière du jeu dans le cas où le jeu n'a pas encore commencé
        screen.blit(banner, banner_rect) #injecter la bannière dans la fenêtre de jeu
        screen.blit(play_button, play_button_rect) #injecter le bouton de jeu dans la fenêtre de jeu
        screen.blit(option_button, option_button_rect) #injecter le bouton d'option dans la fenêtre de jeu
        screen.blit(shop_button, shop_button_rect) #injecter le bouton de shop dans la fenêtre de jeu
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
        
        # Si le joueur clique avec la souris sur le bouton de jeu, on démarre le jeu
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si le clic de souris est sur le bouton de jeu
            if play_button_rect.collidepoint(event.pos):
                # Démarrer le jeu en changeant la variable is_playing à True
                game.is_playing = True
                print("Le jeu commence !")

        # Si le joueur clique avec la souris sur le bouton d'option, on affiche les options
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si le clic de souris est sur le bouton d'option
            if option_button_rect.collidepoint(event.pos):
                # Afficher les options en changeant la variable is_options à True
                game.is_options = True
                print("Bienvenue dans les options !")

        # Si le joueur clique avec la souris sur le bouton de shop, on affiche le shop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si le clic de souris est sur le bouton de shop
            if shop_button_rect.collidepoint(event.pos):
                # Afficher le shop en changeant la variable is_shop à True
                game.is_shop = True
                print("Bienvenue dans le shop !")
    
    # Condition pour changer l'arrière-plan en fonction de la distance parcourue
    # Boucle afin que cela se répète à chaque fois que le cheval avance
    
