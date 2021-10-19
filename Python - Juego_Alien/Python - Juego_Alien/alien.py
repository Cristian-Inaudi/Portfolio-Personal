import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Una clase para representar a 1 alien de la flota."""
    def __init__(self, ai_game):
        """Inicializar el alien y asignar su posicion inicial."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Cargar la imagen del alien y asignar sus atributos rectangulos.
        self.image = pygame.image.load('imagenes/alien2.png')
        self.rect = self.image.get_rect()

        #Comenzar cada nuevo alien cerca del limite superior izquierdo de la pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Almacenar la posicion horizontal exacta de los alien.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Retorna True si el alien esta al borde de la pantalla."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True

    def update(self):
        """Mover el alien hacia la derecha o a la izquierda."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x



