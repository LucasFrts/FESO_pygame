from game.engines.container import Container
class StartMenu(Container):
    def setup(self):
        self.setting.screen.fill("black")
        text_surface = self.setting.fonts.medium.render("Hello World!", True, "white")
        self.setting.screen.blit(text_surface, (40, 250))

