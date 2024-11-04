from game.entities.entity import Entity

class InputBox(Entity):
    def __init__(self, pygame, setting, x, y, width, height):
        super().__init__(pygame, False)
        self.rect = self.game.Rect(x, y, width, height)
        self.setting = setting
        self.color = self.setting.colors.green
        self.text = ''
        self.font = setting.fonts.big
        self.active = False
        

    def do(self, event):
        if event.type == self.game.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == self.game.KEYDOWN:
            if self.active:
                if event.key == self.game.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < 1:
                    self.text += event.unicode.upper()

    def draw(self):
        self.game.draw.rect(self.setting.screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, self.setting.colors.white)
        self.setting.screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))
