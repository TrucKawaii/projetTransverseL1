import pygame
import math

class armes(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 20
        # definir l'image et la taille des muninons
        self.player = player
        self.image = pygame.image.load('munition.png')
        self.image = pygame.transform.scale(self.image, (20, 7))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 50
        self.time = 0
        self.angle = math.radians(50)  # angle de tir en radians (vers le haut)
        self.g = 0.5  # gravité

    def gun(self):
        if self.player.lunch == "right" :
            self.rect.x += self.velocity
        else :
            self.rect.x -= self.velocity
        # supprime la balle quand elle sort des limites de l'écran
        if self.rect.x > 1400 or self.rect.x < 1:
            self.player.ensemble_balle.remove(self)
            self.player.reload = True


    def trajectoire_grenade(self):
        # Mettre en place la trajectoire en courbe parabolique de la grenade
        # Utiliser la formule de la trajectoire d'un projectile en 2D : x = v0 * cos(angle) * t et y = -v0 * sin(angle) * t + 0.5 * g * t^2
        # v0 est la vitesse initiale de la grenade, angle est l'angle de tir, t est le temps écoulé depuis le tir, et g est la gravité
        # Modifier les coordonnées x et y de la grenade en fonction du temps t pour simuler la trajectoire en courbe

        self.time += 0.1  # augmenter le temps écoulé depuis le tir
        x = self.velocity * math.cos(self.angle) * self.time
        y = -self.velocity * math.sin(self.angle) * self.time + 0.5 * self.g * self.time**2
        self.rect.x = self.player.rect.x + x
        self.rect.y = self.player.rect.y + y

        # supprimer la grenade quand elle atteint le sol
        if self.rect.y == 300 or (self.rect.x > 1400 or self.rect.x < 1) :
            self.player.ensemble_balle.remove(self)
            self.player.reload = True