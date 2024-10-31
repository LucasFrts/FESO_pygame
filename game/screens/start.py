from game.engines.container import Container
class StartMenu(Container):
    def setup(self):
        self.setting.screen.fill("#0b0b0b")
        text_surface = self.setting.fonts.medium.render("BreakCode", True, "white")
        self.setting.screen.blit(text_surface, (self.setting.screen.get_width() / 2, self.setting.screen.get_height() / 2))

