from game.engines.runtime import Runtime
from config.setting import Setting
from game.screens.start import StartMenu
from game.screens.game import Game
from game.entities.flow import Flow

import pygame

#tem que importar as configs e adicionar em algum tipo de variavel
class Bootstrap():
    def __init__(self) -> None:
        pass

    def run(self):
        game        = pygame
        flow        = Flow(game)
        
        game.init()
        flow.init()

        setting         = Setting(game)
        setting.flow    = flow
        
        runtime         = Runtime(setting, game)  

        start_menu  = StartMenu(game, setting)
        game        = Game(game, setting)

        runtime.start(start_menu, game)
        return;