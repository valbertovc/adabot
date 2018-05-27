from mode.type import InputType, OutputType

CHAT_WIDTH = 10


class TerminalInput(InputType):
    
    def __init__(self, human_name='You', chat_width=CHAT_WIDTH, *kwargs):
        self.human_name = human_name

    def input(self):
        return input(f'{self.human_name.ljust(CHAT_WIDTH)}: ')


class TerminalOutput(OutputType):

    def __init__(self, bot_name='bot', chat_width=CHAT_WIDTH):
        self.bot_name = bot_name

    def response(self, statement):
        print(f'{self.bot_name.ljust(CHAT_WIDTH)}: {statement}')
