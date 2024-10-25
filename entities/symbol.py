import entity
class Simbol(entity):
    game = None
    def __init__(self, pygame):
        super().__init__(pygame)

    def init(self):
        self.game