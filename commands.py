class Command(object):
    def __init__(self, name, aliases=[]):
        self.name = name
        self.aliases = aliases

    def run(self, game):
        pass

class QuitCommand(Command):
    def __init__(self):
        super().__init__("quit", [])

    def run(self, game):
        game.lose()

# class GoCommand(Command):
#     pass

ALL = [
    QuitCommand()
]
