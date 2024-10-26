from game.engines.runtime import Runtime
from config.setting import Setting
from game.screens.start import StartMenu

import pygame

#tem que importar as configs e adicionar em algum tipo de variavel
class Bootstrap():
    def __init__(self) -> None:
        pass

    def run(self):
        game = pygame
        game.init()
        
        setting = Setting(game)
        start_menu = StartMenu(setting)

        runtime = Runtime(setting, game)        
        runtime.start(start_menu)
        return;