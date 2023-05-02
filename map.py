import pygame
import random

pygame.init()

# Paramètres de la carte
largeur_carte = 800
hauteur_carte = 500
couleur_sol = (50, 205, 50)  # Couleur du sol (vert foncé)
couleur_ciel = (135, 206, 250)  # Couleur du ciel (bleu clair)

# Créer une nouvelle surface pour la carte
carte = pygame.Surface((largeur_carte, hauteur_carte))

# Remplir la surface avec la couleur du ciel
carte.fill(couleur_ciel)

# Dessiner le sol avec la couleur du sol
pygame.draw.rect(carte, couleur_sol, pygame.Rect(0, hauteur_carte // 2, largeur_carte, hauteur_carte // 2))

# Générer des arbres aléatoires
nombre_arbres = 50  # Nombre d'arbres à générer
couleur_arbre = (139, 69, 19)  # Couleur de l'arbre (marron)
taille_max_arbre = 30  # Taille maximale d'un arbre en pixels

for i in range(nombre_arbres):
    taille_arbre = random.randint(5, taille_max_arbre)  # Taille de l'arbre aléatoire
    x = random.randint(0, largeur_carte)  # Coordonnée x de l'arbre aléatoire
    y = random.randint(hauteur_carte // 2 - taille_arbre, hauteur_carte // 2)  # Coordonnée y de l'arbre aléatoire
    pygame.draw.rect(carte, couleur_arbre, pygame.Rect(x, y, taille_arbre, taille_arbre))

# Sauvegarder la carte générée en format JPG
pygame.image.save(carte, "carte_jeu.jpg")

# Fermer Pygame
pygame.quit()

print("La carte du jeu a été générée et enregistrée sous le nom de 'carte_jeu.jpg'.")
