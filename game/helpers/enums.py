from enum import Enum
class Stage(Enum):
    MENU = 0
    CHOOSE_DIFICULT = 1
    GAME = 2
    RANKING = 3
    TUTORIAL = 4
    TUTORIAL_GAME = 5
    END = 8

class Dificulty(Enum):
    MEDIUM = 'normal'
    HARD = 'dificil'