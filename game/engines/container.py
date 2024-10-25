class Container:

    entities = []

    def register(self, entity):
        self.entities.append(entity)
    
    def start(self):
        for entity in self.entities:
            if entity.on_load:
                entity.init()