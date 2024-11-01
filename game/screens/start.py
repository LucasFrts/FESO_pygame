from game.engines.container import Container
from game.entities.button import Button
from game.entities.flow import Flow
class StartMenu(Container):
    def __init__(self, pygame, setting):
        super().__init__(pygame, setting)
        startBtn    = self.menuButtonFactory(200, "Iniciar Jogo", self.startGame)
        tutorialBtn = self.menuButtonFactory(270, "Tutorial", self.openTutorial)
        rankingBtn  = self.menuButtonFactory(340, "Ranking", self.openRanking) 
        closeBtn    = self.menuButtonFactory(410, "Sair", self.close)
        
        self.entities.append(startBtn)
        self.entities.append(tutorialBtn)
        self.entities.append(rankingBtn)
        self.entities.append(closeBtn)

    def draw(self):
        self.setting.screen.fill("#0b0b0b")
        title_text      = "BreakCode"
        title_surface   = self.setting.fonts.bigger.render(title_text, True, (0, 255, 0))
        title_rect      = title_surface.get_rect(center=(self.setting.screen.get_width() // 2, 150))

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
        flow            = next((flow for flow in self.entities if isinstance(flow, Flow)), None)
        flow.running    = False
    def menuButtonFactory(self, position_y, text, action):
        return Button(self.game, self.setting, 250, position_y, 300, 50, text, self.setting.colors.brown, self.setting.colors.light_brown, action)