class Setting():
    screen = None
    dt = 0
    clock = None
    fonts = None

    def __init__(self, pygame):
        fonts = lambda: None
        fonts.big = pygame.font.Font('./assets/fonts/PressStart2P.ttf', 30)
        fonts.medium = pygame.font.Font('./assets/fonts/PressStart2P.ttf', 22)
        fonts.small = pygame.font.Font('./assets/fonts/PressStart2P.ttf', 14)
        
        self.fonts = fonts
        self.screen = pygame.display.set_mode((800,800))
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 1000
        
        pygame.display.set_caption('BreakCode')
