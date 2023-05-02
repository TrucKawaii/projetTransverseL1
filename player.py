import pygame
from arme import armes

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100  # vie du joueur
        self.max_health = 100  # vie max du joueur
        self.attack = 1  # point d'attaque varie selon les armes
        self.velocity = 10  # vitesse du joueur
        self.ensemble_balle = pygame.sprite.Group()
        self.image = pygame.image.load("assets/persoD.png")
        self.image = pygame.transform.scale(self.image, (150, 150))  # fonction qui permet de changer la taille du joueur
        self.rect = self.image.get_rect()  # permet de récupérer la position d'une image et de la déplacer
        self.rect.x = 250
        self.rect.y = 676
        self.masse = 1
        self.is_jump = False
        self.reload = True
        self.jump_speed = 100
        self.gravity = 3
        self.jump_count = 10
        self.start_y = self.rect.y  # Ajouter une variable pour stocker la hauteur de départ du joueur
        self.sens = "right"
        self.lunch = "right"

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
        if not self.is_jump:
            self.is_jump = True
            self.jump_count = 10

    def apply_gravity(self):
        if self.rect.y < 676:  # Modifier la hauteur minimale (676 dans cet exemple)
            self.rect.y += self.gravity
        else:
            self.rect.y = self.start_y  # Réinitialiser la hauteur du joueur à la hauteur de départ
            self.is_jump = False  # Réinitialiser l'état de saut du joueur

    def update(self):
        if self.is_jump:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jump = False
        else:
            self.apply_gravity()

    def lancement_balle(self):
        #creer une nouvelle instance de la classe armes
        self.ensemble_balle.add(armes(self))
