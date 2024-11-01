class Container:
    game = None
    setting = None
    entities = []

    def __init__(self, pygame, setting):
        self.setting = setting
        self.game = pygame
        

    def register(self, entity):
        self.entities.append(entity)
    
    def start(self):
        for entity in self.entities:
            if entity.on_load:
                entity.init()

    def draw(self):
        pass

    def render(self):
        self.draw()
        for entity in self.entities:
            if hasattr(entity, 'draw'):
                entity.draw() 