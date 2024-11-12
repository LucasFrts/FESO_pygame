from pygame.locals import USEREVENT

END_GAME_EVENT = USEREVENT +1
RESET_GAME_EVENT = USEREVENT +2


def get_end_game_event(points, game):
    return game.event.Event(END_GAME_EVENT, {"points":points})


def get_reset_game_event(game):
    return game.event.Event(RESET_GAME_EVENT, {"message": "resetando o game"})