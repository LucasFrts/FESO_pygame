from game.engines.runtime import Runtime
from config.setting import Setting
from game.screens.start import StartMenu

import pygame

#tem que importar as configs e adicionar em algum tipo de variavel
class Bootstrap():
    def __init__(self) -> None:
        pass

    def run(self):
        setting = Setting()
        setting.screen = pygame.display.set_mode((800,800))
        setting.clock = pygame.time.Clock()
        setting.dt = setting.clock.tick(60) / 1000
        
        pygame.display.set_caption('BreakCode')

        start_menu = StartMenu()

        runtime = Runtime(setting, pygame)        
        runtime.start(start_menu)
        return;