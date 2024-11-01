from game.engines.container import Container
from game.entities.button import Button
from game.entities.flow import Flow
class StartMenu(Container):
    def setup(self):
        self.setting.screen.fill("#0b0b0b")
        titulo_texto = "BreakCode"

        titulo_surface = self.setting.fonts.big.render(titulo_texto, True, (0, 255, 0))  # Verde para o título


        titulo_rect = titulo_surface.get_rect(center=(self.setting.screen.get_width() // 2, 150))

        self.setting.screen.blit(titulo_surface, titulo_rect)
        
        startBtn = Button(self.game, self.setting, 300, 200, 200, 50, "Iniciar Jogo", (50, 30, 30), (100, 50, 50), self.startGame)
        tutorialBtn = Button(self.game, self.setting, 300, 270, 200, 50, "Tutorial", (50, 30, 30), (100, 50, 50), self.openTutorial)
        rankingBtn = Button(self.game, self.setting, 300, 340, 200, 50, "Ranking", (50, 30, 30), (100, 50, 50), self.openRanking)
        closeBtn = Button(self.game, self.setting, 300, 410, 200, 50, "Sair", (50, 30, 30), (100, 50, 50), self.close)
        
        self.entities.append(startBtn)
        self.entities.append(tutorialBtn)
        self.entities.append(rankingBtn)
        self.entities.append(closeBtn)



    def startGame(self):
        print("Iniciar Jogo!")

    def openTutorial(self):
        print("Abrir Tutorial!")

    def openRanking(self):
        print("Abrir Ranking!")

    def close(self):
        flow = next((flow for flow in self.entities if isinstance(flow, Flow)), None)
        flow.running = False