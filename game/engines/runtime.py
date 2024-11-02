class Runtime():
    containers = []
    pygame = None
    settings = None

    def __init__(self, setting, pygame):
        self.pygame     = pygame
        self.settings   = setting

    def start(self, *args):
        self.containers = list(args)
    
        for container in self.containers:
            container.start()

        while self.settings.flow.running:
            for event in self.pygame.event.get():
                for artefact in self.containers:
                    for registered in artefact.entities:
                        if event.type in registered.events and artefact.stage == self.settings.flow.stage:
                            print(artefact.entities)
                            registered.do(event.type)

            for container in self.containers:
                if container.stage == self.settings.flow.stage:
                    container.render()

            self.pygame.display.flip()
            
        self.pygame.quit()