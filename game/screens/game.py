from game.engines.container import Container
from game.entities.input_box import InputBox
from config.dicts import letter_images, curiosities
from database.db import insert_ranking
import random

class Game(Container):
    stage = [1]
    entities = []
    level = 1
    points = 0
    points_multiplicator = 10

    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        self.initial_time = 60
        self.time_left = self.initial_time
        self.last_time_update = pygame.time.get_ticks()
        self.curiosities = curiosities
        self.generateInputAndText()
        

    def draw(self):
        self.setting.screen.fill("#0b0b0b")

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
                self.time_left += 30
                self.level += 1
                self.generateInputAndText()
            else:
                insert_ranking(self.level, self.points, True)
                #aqui vamos ter que exibir uma tela de vitoria, mostrar a quantidade de pontos e permitir retornar para o menu ou jogar novamente

        if self.time_left == 0:
            #tem que exibir a mensagem de game over
            #para recomeçar podemos ter algumas alterenativas como resetar os campos e regerar tudo para o jogo poder recomeçar
            #por enquanto vou apenas salvar os resultados e fechar o jogo
            if self.points > 0:
                insert_ranking(self.level, self.points, False)

            self.setting.flow.running = False
        

    def generateInputAndText(self):
        curiosity = random.choice(self.curiosities)
        self.answer = curiosity["answer"]
        self.description_text = curiosity["text"]
        self.curiosities.remove(curiosity)
        self.animal_images = []
        self.entities = []

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
            input_box = InputBox(self.game, self.setting, x_pos, 400, 80, 80, letter)
            self.entities.append(input_box)