from game.entities.entity import Entity
from game.helpers.events import TYPED_GAME_EVENT, get_typed_event
class InputBox(Entity):
    
    text = ""
    active = False
    correct_text = ""
    position = 0
    limit = 0
    def __init__(self, pygame, setting, x, y, width, height, correct_text, position, limit):
        super().__init__(pygame, False)
        self.rect = self.game.Rect(x, y, width, height)
        self.setting = setting
        self.font = setting.fonts.big
        self.correct_text = correct_text
        self.position = position
        self.limit = limit
        self.events.append(self.game.MOUSEBUTTONDOWN)
        self.events.append(self.game.KEYDOWN)
        self.events.append(TYPED_GAME_EVENT)

        if position == 0:
            self.active = True

    def do(self, event):
        if event.type == TYPED_GAME_EVENT:
            if event.position == self.position:
                self.active = True
        if event.type == self.game.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == self.game.KEYDOWN:
            if self.active:
                if event.key == self.game.K_BACKSPACE:
                    if self.position > 0:
                        self.goto_event(-1)
                    self.text = self.text[:-1]
                elif event.key == self.game.K_LEFT:
                    if self.position > 0:
                        self.goto_event(-1)
                elif event.key == self.game.K_RIGHT:
                    if self.position + 1 <= self.limit:
                        self.goto_event(1)
                else:
                    self.text = event.unicode.upper()
                    if self.position + 1 <= self.limit:
                        self.goto_event(1)
                    else:
                        self.active = False

    def draw(self):
        
        color       = self.setting.colors.red
        text_color  = self.setting.colors.white

        if self.text == self.correct_text:
            color = self.setting.colors.green
            if self.active:
                text_color = self.setting.colors.yellow
        elif self.active:
            color = self.setting.colors.yellow
            text_color = self.setting.colors.yellow
        elif self.text == "":
            color = self.setting.colors.white

        self.game.draw.rect(self.setting.screen, color, self.rect, 2)
        text_surface = self.font.render(self.text, True, text_color)

        self.setting.screen.blit(text_surface, (self.rect.x + 25, self.rect.y + 25))
            
    def goto_event(self, value):
        self.active = False
        typed_event = get_typed_event(self.game, self.position + value)
        self.game.event.post(typed_event)