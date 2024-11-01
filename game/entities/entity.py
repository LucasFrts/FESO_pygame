class Entity():
    game = None
    on_load = False
    events = []
    def __init__(self, pygame, ondload = False):
        self.game = pygame
        self.on_load = ondload

    def init(self):
        pass

    def draw(self):
        pass