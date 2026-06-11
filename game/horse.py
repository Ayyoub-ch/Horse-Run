import pygame


class Horse(pygame.sprite.Sprite):
    
    def __init__(self, name, speed):
        super().__init__()
        self.speed = speed  # vitesse horizontale ou rapidité de déplacement sur l'axe X
        self.image = pygame.image.load("assets/sprites/horse/horse.png")
        self.rect = self.image.get_rect()  # rectangle de collision et position du sprite
        self.rect.x = -250  # position de départ horizontale du cheval

        # variables de physique pour le saut
        self.vy = 0.0  # vitesse verticale actuelle (positive = descente, négative = montée)
        self.g = 0.5  # gravité appliquée chaque frame pour faire descendre le cheval
        self.is_jumping = False  # indique si le cheval est en train de sauter ou non
        self.ground_y = None  # hauteur du sol en pixels, utilisée pour détecter l'atterrissage
        self.initial_vy = -15  # impulsion verticale de départ du saut (plus petit = saut plus haut)
        
    def start_jump(self, initial_vy=None):
        """Déclenche le saut en appliquant une impulsion verticale."""
        # Le cheval ne peut sauter que s'il n'est pas déjà en train de sauter
        if not self.is_jumping:
            # Si une vitesse initiale est fournie, l'utiliser ; sinon, utiliser la valeur par défaut
            if initial_vy is None:
                initial_vy = self.initial_vy
            self.vy = initial_vy
            self.is_jumping = True
    

    def update(self, dt=1, ground_y=None):
        """Met à jour la position du cheval chaque frame.

        dt: facteur de temps par frame.
        ground_y: coordonnée Y du sol (en pixels).
        """
        # Si ground_y n'est pas fourni, utiliser self.ground_y
        if ground_y is None:
            ground_y = self.ground_y
        if ground_y is None or not self.is_jumping:
            return
        # Appliquer la gravité et mettre à jour la position verticale
        self.vy += self.g * dt
        self.rect.y += self.vy * dt

        # Vérifier si le cheval a touché le sol
        if self.rect.bottom >= ground_y: # si le bas du rectangle du cheval dépasse ou touche le sol
            # Repositionner le cheval sur le sol et réinitialiser les variables de saut
            self.rect.bottom = ground_y
            self.vy = 0
            self.is_jumping = False

    def jump(self):
        self.start_jump()