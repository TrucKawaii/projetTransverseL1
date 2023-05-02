import pygame
from game import Game


pygame.init()

pygame.display.set_caption("The war")  # Nom de la fenêtre
screen = pygame.display.set_mode((1546, 867))  # Taille de la fenêtre



# charger notre joueur
game = Game()

background = pygame.image.load('assets/1546x867.png')

running = True

# boucle pour garder la fenêtre ouverte
while running:
    # Régler le fond du jeu
    screen.blit(background, (0, 0))


    # récupere les balle que le joueur envoie
    for arme in game.player.ensemble_balle:
        arme.gun()

    # premet d'afficher les balles tirer par les armes
    game.player.ensemble_balle.draw(screen)

    # Paramètre du joueur
    screen.blit(game.player.image, game.player.rect)

    # vérifier si le joueur veut gauche ou droite
    if game.pressed.get(pygame.K_d) and game.player.rect.x < 1390:
        game.player.image = pygame.image.load("assets/persoD.png")
        game.player.image = pygame.transform.scale(game.player.image, (150, 150))
        game.player.sens = "right"
        game.player.move_right()

    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.image = pygame.image.load("assets/persoG.png")
        game.player.image = pygame.transform.scale(game.player.image, (150, 150))
        game.player.sens = "left"
        game.player.move_left()


    # Check if the player wants to jump
    if game.pressed.get(pygame.K_z):
        game.player.jump()

    game.player.update()  # Mise à jour de la position du joueur en fonction de la gravité

    # MAJ de l'écran
    pygame.display.flip()

    # Si fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture")

        # détecte si le joueur lâche une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_1 and game.player.reload == True:
                game.player.lunch = game.player.sens
                game.player.lancement_balle()
                game.player.reload = False
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
