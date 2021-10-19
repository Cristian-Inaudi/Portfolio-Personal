import sys
from time import sleep
from button import Button
from scoreboard import Scoreboard

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Clase general para manejar activos del juego y su comportamiento."""
    def __init__(self):
     """Inicializar el juego y crear los recursos."""
     pygame.init()
     self.settings = Settings()

     #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
     #self.settings.screen_width = self.screen.get_rect().width
     #self.settings.screen_height = self.screen.get_rect().height
     self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
     pygame.display.set_caption("Alien Invasion")

     #Crear instancia para almacenar estadisticas del juego y crear tablero de puntaje.
     self.stats = GameStats(self)
     self.sb = Scoreboard(self)

     self.ship = Ship(self)
     self.bullets = pygame.sprite.Group()
     self.aliens = pygame.sprite.Group()

     self._create_fleet()

     #Asignar color de fondo.
     self.bg_color = (230, 230, 230)

     #Crear boton Jugar.
     self.play_button = Button(self, "Jugar")

    def run_game(self):
        """Empezar el bucle principal del juego."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Responde a evento de entrada de teclado o mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Comenzar partida nueva cuando usuario clickea Jugar."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reinicia las estadisticas del juego.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #Eliminar cualquier alien o bala sobrante.
            self.aliens.empty()
            self.bullets.empty()

            #Crear una nueva flota y centrar la nave.
            self._create_fleet()
            self.ship.center_ship()

            #Esconder cursor del mouse.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respuesta a tecla oprimida."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respuesta a tecla desoprimida."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Crea una nueva bala y la agrega al grupo de balas."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Actualizar la posicion de las balas y eliminar las fuera de pantalla."""
        #Actualizar posicion de las balas.
        self.bullets.update()

        #Eliminar balas que desaparecieron.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Responde a la colision bala-alien."""
        #Eliminar dicha bala y alien colisionados.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            #Destruye las balas existentes y crea una nueva flota.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #Incrementar nivel.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """Chequea si la flota esta al borde de la pantalla, despues actualiza la posicion
           de todos los aliens."""
        self._check_fleet_edges()
        self.aliens.update()

        #Buscar colisiones alien-nave.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #Busca aliens colisionados con el fondo de la pantalla.
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Crea la flota de aliens."""
        #Crear un alien y  calcula el numero de aliens en una fila.
        #El espacio entre cada alien es igual al ancho de un alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determinar el numero de filas de aliens que encajaran en la pantalla.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Crear la flota completa de aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
            #Crear un alien y ubicarlo en la fila.
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Responde apropiadamente si algun alien ha llegado al borde de pantalla."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Suelta toda la flota y cambia su direccion."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
            """Chequea si algun alien alcanzo el fondo de la pantalla."""
            screen_rect = self.screen.get_rect()
            for alien in self.aliens.sprites():
                if alien.rect.bottom >= screen_rect.bottom:
                    #Trata de igual forma a cuando la nave colisiona.
                    self._ship_hit()
                    break

    def _ship_hit(self):
        """Responde a la nave siendo colisionada por el alien."""
        if self.stats.ships_left > 0:
            #Decrementa ships_left, y actualiza la pizarra de puntajes.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #Eliminar aliens y balas sobrantes.
            self.aliens.empty()
            self.bullets.empty()

            #Crea una nueva flota y centra a la nave.
            self._create_fleet()
            self.ship.center_ship()

            #Pausar.
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Actualizar imagenes en la pantalla, y pasar a la nueva pantalla."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Dibujar la informacion del puntaje.
        self.sb.show_score()

        #Dibujar boton Jugar si el juego esta inactivo.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    #Crear una instancia del juego y correrlo.
    ai = AlienInvasion()
    ai.run_game()





