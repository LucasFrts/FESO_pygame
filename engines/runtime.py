import pygame

class runtime():
    containers = []
    def __init__(self, *args):
        self.containers = args

    def start(self):
        for event in pygame.event.get():
            for artefacts in self.containers:
                for registered in artefacts:
                    if registered.event == event:
                        registered.do(event)