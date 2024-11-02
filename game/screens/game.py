from game.engines.container import Container

class Game(Container):
    stage = 1
    entities = []
    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)

    def draw(self):
        self.setting.screen.fill("#0b0b0b")
        
        points_text      = f"Pts: 0"
        points_surface   = self.setting.fonts.bigger.render(points_text, True, (0, 255, 0))
        points_rect      = points_surface.get_rect(center=(self.setting.screen.get_width() // 2, 150))

        self.setting.screen.blit(points_surface, points_rect)
    
    def render(self):
        super().render()
    