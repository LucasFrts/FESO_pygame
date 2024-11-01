class Container:
    game = None
    setting = None
    entities = []

    def __init__(self, pygame, setting):
        self.setting = setting
        self.game = pygame
        self.setup()
        

    def register(self, entity):
        self.entities.append(entity)
    
    def start(self):
        for entity in self.entities:
            if entity.on_load:
                entity.init()

    def setup(self):
        pass