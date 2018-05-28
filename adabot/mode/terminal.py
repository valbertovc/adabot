from adabot.mode.type import InputType, OutputType

CHAT_WIDTH = 10

class TerminalInput(InputType):
    
    def __init__(self, name='', template=''):
        if not name:
            name = 'You'

        if not template:
            template = f'{name.ljust(CHAT_WIDTH)}: '

        self.name = name
        self.template = template

    def input(self):
        return input(self.template)


class TerminalOutput(OutputType):

    def __init__(self, name='', template=''):
        if not name:
            name = 'Bot'

        if not template:
            template = f'{name.ljust(CHAT_WIDTH)}: '

        self.name = name
        self.template = template

    def response(self, statement, *args, **kwargs):
        print(self.template + str(statement))
