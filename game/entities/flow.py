from game.entities.entity import Entity

class Flow(Entity):
    running = False
    stage = 0
    level = 0
    
    def __init__(self, pygame):
        super().__init__(pygame)
        self.events.append(self.game.QUIT)

    def init(self):
        self.running = True
        pass

    def do(self, event):
        if event.type == self.game.QUIT:
            self.running = False