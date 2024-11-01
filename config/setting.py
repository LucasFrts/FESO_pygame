class Setting():
    screen = None
    dt = 0
    clock = None
    fonts = None
    colors = None

    def __init__(self, pygame):
        fonts               = lambda: None
        font_path           = './assets/fonts/PressStart2P.ttf'
        fonts.bigger        = pygame.font.Font(font_path, 44)
        fonts.big           = pygame.font.Font(font_path, 30)
        fonts.medium        = pygame.font.Font(font_path, 22)
        fonts.small         = pygame.font.Font(font_path, 14)
        
        colors              = lambda: None
        colors.white        = (255, 255, 255)
        colors.green        = (0, 255, 0)
        colors.brown        = (50, 30, 30)
        colors.light_brown  = (100, 50, 50)

        self.fonts          = fonts
        self.colors         = colors
        self.screen         = pygame.display.set_mode((800,800))
        self.clock          = pygame.time.Clock()
        self.dt             = self.clock.tick(60) / 1000
        
        pygame.display.set_caption('BreakCode')
