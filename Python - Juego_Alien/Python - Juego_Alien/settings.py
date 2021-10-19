
class Settings:
    """Una clase para almacenar todas las configuraciones para Alien Invasion."""

    def __init__(self):
        """Inicializar las configuraciones del juego."""
        #Configuraciones de Pantalla.
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        #Configuraciones nave.
        self.ship_speed = 2
        self.ship_limit = 3

        #Configuraciones de las balas.
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        #Configuraciones de los aliens.
        self.fleet_drop_speed = 20

        #Incremento velocidad del juego.
        self.speedup_scale = 1.1

        #Incremento puntaje por alien.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializar configuraciones que cambien durante todo el juego."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #fleet_direction de 1 representa derecha; -1 representa izquierda.
        self.fleet_direction = 1

        #Puntaje.
        self.alien_points = 50

    def increase_speed(self):
        """Incrementa configuracion de velocidades y puntos por alien."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)



