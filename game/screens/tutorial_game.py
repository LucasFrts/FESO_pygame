from game.engines.container import Container
from game.entities.input_box import InputBox
from config.dicts import letter_images, curiosities
from database.db import insert_ranking
from game.helpers.events import get_end_game_event, RESET_GAME_EVENT
from game.entities.entity import Entity
from game.entities.button import Button
from game.helpers.enums import Stage
import random

class Tutorial_Game(Container):
    stage = Stage.TUTORIAL_GAME
    entities = []
    level = 1
    points = 0
    points_multiplicator = 10
    reset_game_listener  = None

    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        self.initial_time = 30
        self.time_left = self.initial_time
        self.last_time_update = pygame.time.get_ticks()
        self.curiosities = curiosities
        self.generateInputAndText()
        
    def finalizar_tutorial(self):
        self.setting.flow.stage = Stage.MENU
        self.generateInputAndText()

    def draw(self):
        self.setting.screen.fill("#0b0b0b")

        points_text = f"Pts: {self.points}"  
        points_surface = self.setting.fonts.small.render(points_text, True, (0, 255, 0))
        self.setting.screen.blit(points_surface, (20, 20))

        lengenda_points = " <-- Seus pontos durante a partida"
        lengenda_points_surface = self.setting.fonts.smaller.render(lengenda_points, True, (189, 33, 48))
        self.setting.screen.blit(lengenda_points_surface, (110, 20))

        current_time = self.game.time.get_ticks()
        if current_time - self.last_time_update >= 1000: 
            self.time_left = max(0, self.time_left - 1)
            self.last_time_update = current_time

        time_text = "Tempo: 00:30"
        time_surface = self.setting.fonts.small.render(time_text, True, (0, 255, 0))
        self.setting.screen.blit(time_surface, (self.setting.screen.get_width() - 200, 20))

        lengenda_time1 = "Fique de olho no seu tempo -->"
        lengenda_time2 = "Você ganha mais tempo com cada"
        lengenda_time3 = "acerto!"
        lengenda_time_surface1 = self.setting.fonts.smaller.render(lengenda_time1, True, (189, 33, 48))
        lengenda_time_surface2 = self.setting.fonts.smaller.render(lengenda_time2, True, (189, 33, 48))
        lengenda_time_surface3 = self.setting.fonts.smaller.render(lengenda_time3, True, (189, 33, 48))
        self.setting.screen.blit(lengenda_time_surface1, (690, 20))
        self.setting.screen.blit(lengenda_time_surface2, (690, 35))
        self.setting.screen.blit(lengenda_time_surface3, (690, 50))
        
        
        lengenda_game1 = "1º Existem dois níveis de dificuldade: Fácil e Médio. O tutorial está no nível Médio."
        lengenda_game2 = "* Fácil: A primeira letra do animal na imagem corresponde à letra na sua posição na palavra."
        lengenda_game3 = "* Médio: O nome do animal indica as letras que você pode escolher para preencher a posição correta"
        lengenda_game4 = "  da palavra."
        lengenda_game5 = "2º  Quando a letra for correta, o quadrado ficará verde. Se estiver errada, ficará vermelho."
        lengenda_game6 = "3º  Descubra a palavra atual para finalizar o tutorial"

        lengenda_game_surface1 = self.setting.fonts.smaller.render(lengenda_game1, True, (189, 33, 48))
        lengenda_game_surface2 = self.setting.fonts.smaller.render(lengenda_game2, True, (189, 33, 48))
        lengenda_game_surface3 = self.setting.fonts.smaller.render(lengenda_game3, True, (189, 33, 48))
        lengenda_game_surface4 = self.setting.fonts.smaller.render(lengenda_game4, True, (189, 33, 48))
        lengenda_game_surface5 = self.setting.fonts.smaller.render(lengenda_game5, True, (189, 33, 48))
        lengenda_game_surface6 = self.setting.fonts.smaller.render(lengenda_game6, True, (189, 33, 48))
        self.setting.screen.blit(lengenda_game_surface1, (40, 510))
        self.setting.screen.blit(lengenda_game_surface2, (60, 527))
        self.setting.screen.blit(lengenda_game_surface3, (60, 542))
        self.setting.screen.blit(lengenda_game_surface4, (60, 557))
        self.setting.screen.blit(lengenda_game_surface5, (40, 580))
        self.setting.screen.blit(lengenda_game_surface6, (40, 600))


        description_surface = self.setting.fonts.smaller.render(self.description_text, True, (0, 255, 0))
        description_rect = description_surface.get_rect(center=(self.setting.screen.get_width() // 2, 150))
        self.setting.screen.blit(description_surface, description_rect)

        total_width = len(self.answer) * 100 - 20
        screen_center_x = self.setting.screen.get_width() // 2
        start_x = screen_center_x - (total_width // 2)  

        for i, image in enumerate(self.loaded_images):
            x_pos = start_x + i * 100
            self.setting.screen.blit(image, (x_pos, 200))

        inputed_text = "";
        for entity in self.entities:
            if isinstance(entity, InputBox):
                inputed_text += entity.text  
        if inputed_text == self.answer:
            self.finalizar_tutorial()

    def generateInputAndText(self):
        curiosity = self.curiosities[1]
        self.answer = curiosity["answer"]
        self.description_text = curiosity["text"]
        self.curiosities.remove(curiosity)
        self.animal_images = []
        self.entities = [artefact for artefact in self.entities if artefact is self.reset_game_listener]
    
        for letter in self.answer:
            letter_dict = [letter_dic for letter_dic in letter_images if letter_dic["letter"] == letter.lower()][0]
            self.animal_images.append(random.choice(letter_dict["images"]))

        self.loaded_images = [
            self.game.transform.scale(self.game.image.load(img_path), (80, 80)) for img_path in self.animal_images
        ]

        total_width = len(self.answer) * 100 - 20 
        screen_center_x = self.setting.screen.get_width() // 2
        start_x = screen_center_x - (total_width // 2)  

        for i, letter in enumerate(self.answer):
            x_pos = start_x + i * 100
            self.setting.screen.blit(self.loaded_images[i], (x_pos, 200))
            input_box = InputBox(self.game, self.setting, x_pos, 400, 80, 80, letter, i, len(self.answer) - 1)
            self.entities.append(input_box)
            