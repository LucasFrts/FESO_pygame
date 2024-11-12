import pygame
from game.entities.button import Button
from game.engines.container import Container
from database.db import get_ranking
from game.helpers.enums import Stage

class Ranking(Container):
    stage = Stage.RANKING
    entities = []
    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        returnMenu   = Button(self.game, self.setting, 25, 10, 150, 40, "Voltar", "#0b0b0b", "#0b0b0b", self.return_to_menu)
        returnMenu.color_text = self.setting.colors.green 

        self.entities.append(returnMenu)

    def return_to_menu(self):
        self.setting.flow.stage = Stage.MENU

    def draw(self):
        self.setting.screen.fill("#0b0b0b")

        # Título
        title_text = "Ranking"
        title_surface = self.setting.fonts.bigger.render(title_text, True, self.setting.colors.green)
        title_rect = title_surface.get_rect(center=(self.setting.screen.get_width() // 2, 100))
        self.setting.screen.blit(title_surface, title_rect)

        # Cabeçalho das colunas do ranking
        header_text = ["Posição", "Level", "Score", "Pts."]
        header_height = 30  
        y_position = 250  

        self.draw_table_header(header_text, y_position, header_height)

        y_position += header_height  

        line_height = 30  
        border_radius = 5  

        column_width = (self.setting.screen.get_width() // len(header_text)) - 150  

        total_table_width = column_width * len(header_text)
        table_start_x = (self.setting.screen.get_width() - total_table_width) // 2

        ranking_data = get_ranking()

        for i, row in enumerate(ranking_data):
            rank = i + 1
            levels = row[0]  
            score = row[1]  
            finished = row[2]  

            data = [str(rank), str(levels), str(score), str(finished)]

            self.draw_table_row(data, y_position, line_height, column_width, border_radius, table_start_x)

            y_position += line_height  


    def draw_table_header(self, header_texts, y_position, height):
        """Função para desenhar o cabeçalho da tabela."""
        font = self.setting.fonts.small
        column_width = (self.setting.screen.get_width() // len(header_texts)) - 150  

        total_table_width = column_width * len(header_texts)
        table_start_x = (self.setting.screen.get_width() - total_table_width) // 2

        for idx, text in enumerate(header_texts):
            header_rect = pygame.Rect(table_start_x + idx * column_width, y_position, column_width, height)
            pygame.draw.rect(self.setting.screen, '#0b0b0b', header_rect)  
            header_surface = font.render(text, True, self.setting.colors.green)  
            header_text_rect = header_surface.get_rect(center=header_rect.center)  
            self.setting.screen.blit(header_surface, header_text_rect)

    def draw_table_row(self, data, y_position, height, column_width, border_radius, table_start_x):
        """Função para desenhar uma linha de dados na tabela."""
        font = self.setting.fonts.small  
        padding = 5  

        for idx, cell_data in enumerate(data):
            row_rect = pygame.Rect(table_start_x + idx * column_width + padding, y_position + padding, column_width - padding * 2, height - padding * 2)

            pygame.draw.rect(self.setting.screen, "#0b0b0b", row_rect, border_radius)

            cell_surface = font.render(cell_data, True, self.setting.colors.green)
            cell_rect = cell_surface.get_rect(center=row_rect.center)
            self.setting.screen.blit(cell_surface, cell_rect)


