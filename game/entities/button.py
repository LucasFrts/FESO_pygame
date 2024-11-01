from game.entities.entity import Entity

class Button(Entity):
    def __init__(self, pygame, setting, x, y, width, height, text, color_btn, color_hover, action=None):
        super().__init__(pygame, True)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color_btn = color_btn
        self.color_hover = color_hover
        self.action = action
        self.pressionado = False
        self.setting = setting
        self.is_hovered = False  # Controle de hover
        self.events.append(self.game.MOUSEBUTTONDOWN)
        self.events.append(self.game.MOUSEBUTTONUP)
        self.events.append(self.game.MOUSEMOTION)  # Adiciona evento de movimento do mouse

    def draw(self):
        mouse = self.game.mouse.get_pos()
        self.is_hovered = (self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y)

        cor_atual = self.color_hover if self.is_hovered else self.color_btn
        self.game.draw.rect(self.setting.screen, cor_atual, (self.x, self.y, self.width, self.height), border_radius=20)

        texto_surf = self.setting.fonts.medium.render(self.text, True, (255, 255, 255))
        texto_rect = texto_surf.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.setting.screen.blit(texto_surf, texto_rect)

    def do(self, event):
        if event == self.game.MOUSEBUTTONDOWN:
            if self.is_hovered: 
                self.pressionado = True
        elif event == self.game.MOUSEBUTTONUP:
            if self.pressionado:
                self.pressionado = False
                if self.is_hovered and self.action: 
                    self.action()