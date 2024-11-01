from game.engines.runtime import Runtime
from config.setting import Setting
from game.screens.start import StartMenu

import pygame

#tem que importar as configs e adicionar em algum tipo de variavel
class Bootstrap():
    def __init__(self) -> None:
        pass

    def run(self):
        pygame.init()
        game        = pygame
        
        setting     = Setting(game)
        runtime     = Runtime(setting, game)  

        start_menu  = StartMenu(pygame, setting)

        runtime.start(start_menu)
        return;