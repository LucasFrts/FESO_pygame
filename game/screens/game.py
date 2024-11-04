from game.engines.container import Container
from game.entities.input_box import InputBox  # Supondo que você tenha uma classe InputBox para as entradas de letras

class Game(Container):
    stage = 1
    entities = []

    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        self.answer = "PASSARO"
        self.input_boxes = []

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
        
        # Carregar as imagens dos animais
        self.loaded_images = [pygame.image.load(img_path) for img_path in self.animal_images]

        # Criar os input boxes para as letras
        x_offset = 200
        for i in range(len(self.answer)):
            input_box = InputBox(pygame, setting, x_offset + i * 60, 400, 50, 50)  # largura e altura de 50x50 para cada caixa
            self.input_boxes.append(input_box)
            self.entities.append(input_box)  # Adicionar cada input box na lista de entidades para renderização e eventos

    def draw(self):
        self.setting.screen.fill("#0b0b0b")

        # Desenhar pontuação
        points_text = "Pts: 10"  # Pontuação fixa por enquanto
        points_surface = self.setting.fonts.big.render(points_text, True, (0, 255, 0))
        self.setting.screen.blit(points_surface, (20, 20))

        # Desenhar contador de tempo
        time_text = "Tempo: 01:00"  # Tempo fixo por enquanto
        time_surface = self.setting.fonts.big.render(time_text, True, (0, 255, 0))
        self.setting.screen.blit(time_surface, (self.setting.screen.get_width() - 150, 20))

        # Descrição do animal
        description_text = "Esse animal é conhecido por sua capacidade de voar e costuma ser visto em bandos."
        description_surface = self.setting.fonts.medium.render(description_text, True, (0, 255, 0))
        description_rect = description_surface.get_rect(center=(self.setting.screen.get_width() // 2, 100))
        self.setting.screen.blit(description_surface, description_rect)

        # Desenhar imagens dos animais
        x_pos = 150
        for image in self.loaded_images:
            self.setting.screen.blit(image, (x_pos, 200))
            x_pos += 70  # espaçamento entre as imagens

        # Desenhar input boxes para resposta
        for input_box in self.input_boxes:
            input_box.draw()  # Supondo que o método draw() exibe a caixa de texto e o que for digitado nela
