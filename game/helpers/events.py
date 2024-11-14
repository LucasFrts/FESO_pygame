from pygame.locals import USEREVENT

END_GAME_EVENT = USEREVENT +1
RESET_GAME_EVENT = USEREVENT +2
TYPED_GAME_EVENT = USEREVENT +3

def get_end_game_event(points, game):
    return game.event.Event(END_GAME_EVENT, {"points":points})


def get_reset_game_event(game):
    return game.event.Event(RESET_GAME_EVENT, {"message": "resetando o game"})

def get_typed_event(game, position):
    return game.event.Event(TYPED_GAME_EVENT, {"position":position})