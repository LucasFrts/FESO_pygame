import pygame
from game.entities.button import Button
from game.engines.container import Container
from game.helpers.enums import Stage
import textwrap

class Tutorial(Container):
    stage = Stage.TUTORIAL
    entities = []

    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        
        continuarTutorial = Button(self.game, self.setting, 490, 580, 230, 40, "Continuar", "#0b0b0b", "#0b0b0b", self.continuar_tutorial)
        continuarTutorial.color_text = self.setting.colors.green
        returnMenu = Button(self.game, self.setting, 25, 10, 150, 40, "Voltar", "#0b0b0b", "#0b0b0b", self.return_to_menu)
        returnMenu.color_text = self.setting.colors.green
        self.entities.append(continuarTutorial)
        self.entities.append(returnMenu)

    def continuar_tutorial(self):
        self.setting.flow.stage = Stage.TUTORIAL_GAME

    def return_to_menu(self):
        self.setting.flow.stage = Stage.MENU

    def desenhar_retangulo_com_borda(self, x, y, largura, altura, espessura_borda, cor_borda):
        """Desenha um retângulo com borda"""
        pygame.draw.rect(self.setting.screen, cor_borda, (x, y, largura, altura), espessura_borda)

    def desenhar_texto_no_retangulo(self, texto, x, y, largura, altura):

        fonte = self.setting.fonts.smaller
        texto_quebrado = textwrap.fill(texto, width=60)  

        # Desenhar cada linha de texto
        linha_y = y + 50  # Margem superior
        for linha in texto_quebrado.splitlines():
            texto_renderizado = fonte.render(linha, True, self.setting.colors.white)  
            texto_rect = texto_renderizado.get_rect(center=(x + largura // 2, linha_y))  # Centraliza na largura do retângulo
            self.setting.screen.blit(texto_renderizado, texto_rect)
            linha_y += fonte.get_height() + 18  # Desloca para a próxima linha

    def draw(self):

        self.setting.screen.fill("#0b0b0b")

        title_text = "Tutorial"
        title_surface = self.setting.fonts.bigger.render(title_text, True, self.setting.colors.green)
        title_rect = title_surface.get_rect(center=(self.setting.screen.get_width() // 2, 100))
        self.setting.screen.blit(title_surface, title_rect)

        self.desenhar_retangulo_com_borda(250, 200, 700, 400, 2, (0, 255, 0))

        texto_explicativo = (
            "Durante o jogo, você verá uma sequência de imagens. Cada imagem corresponde a uma letra. "
            "O nome do animal representado pela imagem indica quais letras você pode escolher para preencher aquela posição na palavra. "
            "   Exemplo: "
            "Se você vê a imagem de um GATO, as letras possíveis para a posição correspondente são G, A, T e O.  "
            "Você acumula pontos e aumenta o tempo de jogo cada vez que resolve um enigma corretamente. "
            "A pontuação é aumentada com base na rapidez com que você resolve o enigma. Quanto mais rápido, mais pontos!  "
            "Se o cronômetro chegar a zero, o jogo acaba e sua pontuação final será exibida."
        )
        self.desenhar_texto_no_retangulo(texto_explicativo, 250, 200, 700, 270)

        


