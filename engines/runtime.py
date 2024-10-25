import pygame

class Runtime():
    containers = []
    def __init__(self, *args):
        self.containers = args

    def start(self):
        pygame.init()
        #definir através de um das classes de config ou umas das classes de entidade que escuta eventos genericos
        running  = True
        while running:
            for event in pygame.event.get():
                for artefacts in self.containers:
                    for registered in artefacts:
                        if registered.event == event:
                            registered.do(event)
        pygame.quit()