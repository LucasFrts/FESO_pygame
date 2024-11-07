from game.engines.container import Container
from game.entities.input_box import InputBox  # Supondo que você tenha uma classe InputBox para as entradas de letras

class Game(Container):
    stage = 1
    entities = []

    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        self.answer = "PASSARO"
        self.initial_time = 60
        self.time_left = self.initial_time
        self.last_time_update = pygame.time.get_ticks()  # Para controlar o tempo

        # Definir a posição inicial para as imagens dos animais
        self.animal_images = [
            './assets/images/animals/peixe.jpg',
            './assets/images/animals/gato.jpg',
            './assets/images/animals/sapo.jpg',
            './assets/images/animals/sapo.jpg',
            './assets/images/animals/gato.jpg',
            './assets/images/animals/coruja.jpg',
            './assets/images/animals/macaco.jpg'
        ]
        
        self.loaded_images = [
            pygame.transform.scale(pygame.image.load(img_path), (80, 80)) for img_path in self.animal_images
        ]

        # Criar os input boxes para as letras
        x_offset = 240
        i = 0
        for letter in self.answer:
            input_box = InputBox(pygame, setting, x_offset + i * 100, 400, 80, 80, letter)
            self.entities.append(input_box)
            i+=1

    def draw(self):
        self.setting.screen.fill("#0b0b0b")

        points_text = "Pts: 10"  
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

        description_text = "Esse animal é conhecido por sua capacidade de voar e costuma ser visto em bandos."
        description_surface = self.setting.fonts.smaller.render(description_text, True, (0, 255, 0))
        description_rect = description_surface.get_rect(center=(self.setting.screen.get_width() // 2, 100))
        self.setting.screen.blit(description_surface, description_rect)

        x_pos = 240
        for image in self.loaded_images:
            self.setting.screen.blit(image, (x_pos, 200))
            x_pos += 100 
        
        inputed_text = "";
        for entity in self.entities:
            if isinstance(entity, InputBox):
                inputed_text += entity.text
        if inputed_text == self.answer:
            print("ganhou uhuuull")

