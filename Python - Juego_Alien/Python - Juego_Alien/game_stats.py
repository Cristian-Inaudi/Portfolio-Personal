class GameStats:
    """Seguimiento de estadisticas para Alien Invasion."""

    def __init__(self, ai_game):
        """Inicializar estadisticas."""
        self.settings = ai_game.settings
        self.reset_stats()

        #Comenzar Alien Invasion en un estado activo.
        self.game_active = False

        #Record puntaje nunca debe reiniciarse.
        self.high_score = 0

    def reset_stats(self):
        """Inicializar las estadisticas que puedan cambiar durante el juego."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

