from adabot.mode.type import InputType, OutputType

CHAT_WIDTH = 10


class TerminalInput(InputType):
    
    def __init__(self, name='You'):
        self.name = name
        self.template = f'{self.name.ljust(CHAT_WIDTH)}: '

    def input(self):
        return input(self.template)


class TerminalOutput(OutputType):

    def __init__(self, name='bot'):
        self.name = name
        self.template = f'{self.name.ljust(CHAT_WIDTH)}: '

    def response(self, statement, *args, **kwargs):
        print(self.template + str(statement))
