from game.entities.flow import Flow
class Runtime():
    containers = []
    pygame = None
    settings = None

    def __init__(self, setting, pygame):
        self.pygame = pygame
        self.settings = setting

    def start(self, *args):
        self.containers = list(args)
    
        for container in self.containers:
            container.start()
        
        flow = Flow(self.pygame)
        flow.init()

        self.containers[0].entities.append(flow)

        while flow.running:
            for event in self.pygame.event.get():
                for artefact in self.containers:
                    for registered in artefact.entities:
                        if event.type in registered.events:
                            registered.do(event.type)
            for container in self.containers:
                container.render()
                
            self.pygame.display.flip()
            
        self.pygame.quit()