from game.engines.container import Container
from game.entities.input_box import InputBox
from config.dicts import letter_images, curiosities
from database.db import insert_ranking
from game.helpers.events import get_end_game_event, RESET_GAME_EVENT, START_GAME_EVENT
from game.entities.entity import Entity
from game.helpers.enums import Stage, Dificulty
import random

class Game(Container):
    stage = Stage.GAME
    entities = []
    level = 1
    points = 0
    points_multiplicator = 10
    reset_game_listener  = None
    started = False

    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        self.initial_time = 30
        self.time_left = self.initial_time
        self.last_time_update = pygame.time.get_ticks()
        self.curiosities = curiosities

        reset_game_listener = Entity(pygame)
        reset_game_listener.events.append(RESET_GAME_EVENT)
        reset_game_listener.do = self.reset_game
        reset_game_listener.stageless = True
        self.reset_game_listener = reset_game_listener
        self.entities.append(reset_game_listener)

        start_game_listener = Entity(pygame)
        start_game_listener.events.append(START_GAME_EVENT)
        start_game_listener.do = self.start_game
        start_game_listener.stageless = True
        self.entities.append(start_game_listener)
        

    def draw(self):
        self.setting.screen.fill("#0b0b0b")
        if self.started:
            points_text = f"Pts: {self.points}"  
            points_surface = self.setting.fonts.small.render(points_text, True, (0, 255, 0))
            self.setting.screen.blit(points_surface, (20, 20))

            current_time = self.game.time.get_ticks()
            if current_time - self.last_time_update >= 1000: 
                self.time_left = max(0, self.time_left - 1)
                self.last_time_update = current_time

            minutes = self.time_left // 60
            seconds = self.time_left % 60
            time_text = f"Tempo: {minutes:02}:{seconds:02}"
            time_surface = self.setting.fonts.small.render(time_text, True, (0, 255, 0))
            self.setting.screen.blit(time_surface, (self.setting.screen.get_width() - 200, 20))

            description_surface = self.setting.fonts.smaller.render(self.description_text, True, (0, 255, 0))
            description_rect = description_surface.get_rect(center=(self.setting.screen.get_width() // 2, 100))
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
                self.points += self.points_multiplicator * self.time_left
                if len(self.curiosities) > 0:
                    print(self.time_left)
                    self.time_left += 30
                    if self.time_left > 60:
                        self.time_left = 60
                        
                    self.level += 1
                    self.generateInputAndText()
                else:
                    insert_ranking(self.level, self.points, True)
                    self.time_left = 0

            if self.time_left == 0:
                if self.points > 0:
                    insert_ranking(self.level, self.points, False)

                end_game_event = get_end_game_event(self.points, self.game)
                self.game.event.post(end_game_event)
                self.setting.flow.stage = Stage.END
        

    def generateInputAndText(self):
        curiosity = random.choice(self.curiosities)
        self.answer = curiosity["answer"]
        self.description_text = curiosity["text"]
        self.curiosities.remove(curiosity)
        self.animal_images = []
        self.entities = [artefact for artefact in self.entities if artefact is self.reset_game_listener]
        for letter in self.answer:
            letter_dict = [letter_dic for letter_dic in letter_images if letter_dic["letter"] == letter.lower()][0]
            self.animal_images.append(random.choice(letter_dict["images"]) if self.setting.dificulty == Dificulty.HARD else letter_dict["images"][0])

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

    def reset_game(self, event):
        if event.type == RESET_GAME_EVENT:
            self.time_left = self.initial_time
            self.last_time_update = self.game.time.get_ticks()
            self.curiosities = curiosities
            self.points = 0
            self.level = 1
            self.generateInputAndText()
            self.setting.stage = Stage.MENU

    def start_game(self, event):
        if event.type == START_GAME_EVENT:
            self.generateInputAndText()
            self.started = True