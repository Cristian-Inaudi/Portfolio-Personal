import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Una clase para manejar las balas disparadas por la nave."""

    def __init__(self, ai_game):
        """Crear un objeto bala para la posicion actual de la nave."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Crear un rectangulo bala en (0, 0) y despues definir posicion correcta.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Almacenar la posicion de las balas como valor decimal.
        self.y = float(self.rect.y)

    def update(self):
        """Mueve la bala hacia arriba de la pantalla."""
        #Actualiza la posicion decimal de la bala.
        self.y -= self.settings.bullet_speed
        #Actualiza la posicion del rectangulo.
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibuja la bala en la pantalla"""
        pygame.draw.rect(self.screen, self.color, self.rect)
