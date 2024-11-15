from game.engines.container import Container
from game.entities.entity import Entity
from game.entities.button import Button
from game.helpers.enums import Stage,Dificulty

class Choose_Dificult(Container):
    stage = Stage.CHOOSE_DIFICULT
    entities = []

    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        medium = self.chooseButtonFactory(280, "Fácil", self.choose_medium)
        hard  = self.chooseButtonFactory(420, "Médio", self.choose_hard) 

        return_button = Button(pygame, self.setting, 25, 10, 150, 40, "Voltar", "#0b0b0b", "#0b0b0b", self.return_to_menu)
        return_button.color_text = self.setting.colors.green

        self.entities.append(medium)
        self.entities.append(hard)
        self.entities.append(return_button)

    def draw(self):
        self.setting.screen.fill("#0b0b0b")

        text_easy            = "A letra abaixo do animal será sempre a primeira letra do nome do animal"
        text_hard            = "A letra abaixo do animal poderá ser qualquer letra do nome do animal"

        easy_surface   = self.setting.fonts.small.render(text_easy, True, self.setting.colors.white)
        easy_rect      = easy_surface.get_rect(center=(self.setting.screen.get_width() // 2, 240))
        hard_surface   = self.setting.fonts.small.render(text_hard, True, self.setting.colors.white)
        hard_rect      = hard_surface.get_rect(center=(self.setting.screen.get_width() // 2, 380))
        
        
        self.setting.screen.blit(easy_surface, easy_rect)
        self.setting.screen.blit(hard_surface, hard_rect)

    def chooseButtonFactory(self, position_y, text, action):
        return Button(self.game, self.setting, 440, position_y, 300, 50, text, self.setting.colors.brown, self.setting.colors.light_brown, action)


    def choose_medium(self):
        self.choose(Dificulty.MEDIUM)

    def choose_hard(self):
        self.choose(Dificulty.HARD)

    def choose(self, dificulty):
        self.setting.dificulty = dificulty
        self.setting.flow.stage = Stage.GAME

    def return_to_menu(self):
        self.setting.flow.stage = Stage.MENU