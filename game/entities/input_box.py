from game.entities.entity import Entity

class InputBox(Entity):
    
    text = ""
    active = False
    correct_text = ""

    def __init__(self, pygame, setting, x, y, width, height, correct_text):
        super().__init__(pygame, False)
        self.rect = self.game.Rect(x, y, width, height)
        self.setting = setting
        self.font = setting.fonts.big
        self.correct_text = correct_text
        self.events.append(self.game.MOUSEBUTTONDOWN)
        self.events.append(self.game.KEYDOWN)
        

    def do(self, event):
        if event.type == self.game.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == self.game.KEYDOWN:
            if self.active:
                if event.key == self.game.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text = event.unicode.upper()
                    self.active = False

    def draw(self):
        
        color = self.setting.colors.red

        if self.text == self.correct_text:
            color = self.setting.colors.green
        elif self.active:
            color = self.setting.colors.yellow
        elif self.text == "":
            color = self.setting.colors.white

        self.game.draw.rect(self.setting.screen, color, self.rect, 2)
        text_surface = self.font.render(self.text, True, self.setting.colors.white)

        self.setting.screen.blit(text_surface, (self.rect.x + 25, self.rect.y + 25))
            