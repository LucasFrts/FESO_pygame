from ..engines.runtime import Runtime
#tem que importar as configs e adicionar em algum tipo de variavel
class Bootstrap():
    def __init__(self) -> None:
        pass

    def run(self):
        runtime = Runtime()        
        runtime.start()
        pass