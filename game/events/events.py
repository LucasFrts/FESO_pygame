from pygame.locals import USEREVENT

END_GAME_EVENT = USEREVENT +1


def get_end_game_event(points, game):
    return game.event.Event(END_GAME_EVENT, {"points":points})