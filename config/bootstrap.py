from game.engines.runtime import Runtime
from game.engines.container import Container
from config.setting import Setting
from game.screens.start import StartMenu
from game.screens.game import Game
from game.screens.chose_dificulty import Choose_Dificult
from game.entities.flow import Flow
from game.screens.end import End
from game.screens.ranking import Ranking
import pygame

#tem que importar as configs e adicionar em algum tipo de variavel
class Bootstrap():
    def __init__(self) -> None:
        pass

    def run(self):
        game        = pygame
        flow        = Flow(game)
        flow.stageless = True
        game.init()
        flow.init()

        setting         = Setting(game)
        setting.flow    = flow
        
        runtime         = Runtime(setting, game)  

        start_menu       = StartMenu(game, setting)
        choose_dificulty = Choose_Dificult(game, setting)
        game_screen      = Game(game, setting)
        ranking          = Ranking(game, setting)
        end_game         = End(game, setting)
        flow_container    = Container(game, setting)
        flow_container.entities.append(flow)

        runtime.start(start_menu, choose_dificulty, game_screen, end_game, flow_container, ranking)