from game.engines.container import Container
from game.entities.entity import Entity
from game.entities.button import Button
from game.helpers.events import END_GAME_EVENT
from game.helpers.events import get_reset_game_event
from game.helpers.enums import Stage
class End(Container):
    stage = Stage.END
    entities = []
    end_game_entity = None

    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        end_game_listener = Entity(pygame)
        end_game_listener.events.append(END_GAME_EVENT)
        end_game_listener.do = self.end_game_do
        end_game_listener.draw = self.end_game_draw
        end_game_listener.description_text = ""
        end_game_listener.stageless = True
        self.entities.append(end_game_listener)
        self.end_game_entity = end_game_listener
        return_button = Button(pygame, self.setting, 0, 10, 300, 50, "Voltar", "#0b0b0b", "#0b0b0b", self.return_to_menu)
        return_button.color_text = self.setting.colors.green
        self.entities.append(return_button)

    def draw(self):
        self.setting.screen.fill("#0b0b0b")
        text            = "FIM DO JOGO"
        title_surface   = self.setting.fonts.bigger.render(text, True, self.setting.colors.green)
        title_rect      = title_surface.get_rect(center=(self.setting.screen.get_width() // 2, 100))
        description_surface   = self.setting.fonts.medium.render(self.end_game_entity.description_text, True, self.setting.colors.white)
        description_rect      = description_surface.get_rect(center=(self.setting.screen.get_width() // 2, 300))
        
        self.setting.screen.blit(title_surface, title_rect)
        self.setting.screen.blit(description_surface, description_rect)

        

    def end_game_do(self, event):
        if event.type == END_GAME_EVENT:
            self.end_game_entity.description_text = f"Você alcançou {event.points} Pontos!"

    def end_game_draw(self):
        pass

    def return_to_menu(self):
        self.setting.flow.stage = Stage.MENU
        reset_game = get_reset_game_event(self.game)
        self.game.event.post(reset_game)