from game.engines.container import Container
from game.entities.button import Button
from game.entities.flow import Flow
class StartMenu(Container):
    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        startBtn = Button(self.game, self.setting, 250, 200, 300, 50, "Iniciar Jogo", (50, 30, 30), (100, 50, 50), self.startGame)
        tutorialBtn = Button(self.game, self.setting, 250, 270, 300, 50, "Tutorial", (50, 30, 30), (100, 50, 50), self.openTutorial)
        rankingBtn = Button(self.game, self.setting, 250, 340, 300, 50, "Ranking", (50, 30, 30), (100, 50, 50), self.openRanking)
        closeBtn = Button(self.game, self.setting, 250, 410, 300, 50, "Sair", (50, 30, 30), (100, 50, 50), self.close)
        
        self.entities.append(startBtn)
        self.entities.append(tutorialBtn)
        self.entities.append(rankingBtn)
        self.entities.append(closeBtn)

    def draw(self):
        self.setting.screen.fill("#0b0b0b")
        title_text = "BreakCode"

        title_surface = self.setting.fonts.big.render(title_text, True, (0, 255, 0))

        title_rect = title_surface.get_rect(center=(self.setting.screen.get_width() // 2, 150))

        self.setting.screen.blit(title_surface, title_rect)
    
    def render(self):
        super().render()

    def startGame(self):
        print("Iniciar Jogo!")

    def openTutorial(self):
        print("Abrir Tutorial!")

    def openRanking(self):
        print("Abrir Ranking!")

    def close(self):
        flow = next((flow for flow in self.entities if isinstance(flow, Flow)), None)
        flow.running = False