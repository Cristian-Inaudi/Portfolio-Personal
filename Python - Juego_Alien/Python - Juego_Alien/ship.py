import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Una clase para administrar la nave."""

    def __init__(self, ai_game):
        """Inicializar la nave y configurar su posición inicial."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Cargar la imágen de la nave y obtener sus rectángulos.
        self.image = pygame.image.load('imagenes/ship.png')
        self.rect = self.image.get_rect()

        #Comenzar cada nave ubicada al fondo y centrada en la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        #Guardar el valor decimal para la posicion horizontal de la nave.
        self.x = float(self.rect.x)

        #Movimientos bandera
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualizar la posicion de la nave basado en el movimento bandera."""
        #Actualizar el valor X de la nave, no del rectangulo.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Actualizar objeto rectangulo desde self.x.
        self.rect.x = self.x

    def blitme(self):
        """Dibujar la nave en su ubicación actual"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centrar la nave en la pantalla."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
