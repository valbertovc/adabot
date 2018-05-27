from chatterbot import ChatBot
from command import WitCommmand
from runner import RequestRunner
from mode import voice, terminal
from settings import WIT_TOKEN, ARDUINO_URL


class Ada(object):
    name = 'Ada'

    def __init__(self, human_name=None, in_mode=None, out_mode=None, confidence=0.7, train=True):

        self.command = WitCommmand(token=WIT_TOKEN,
                                   runner=RequestRunner(url=ARDUINO_URL))
        self.bot = ChatBot(
            self.name, 
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database='./database.sqlite3',
            preprocessors=[
                'chatterbot.preprocessors.clean_whitespace'
            ],
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
                    'response_selection_method': 'chatterbot.response_selection.get_first_response'
                },
                {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': confidence,
                    'default_response': 'Me desculpe, mas eu não entendi.'
                }
            ],
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
        
        if not in_mode:
            in_mode = terminal.TerminalInput(human_name)
        if not out_mode:
            out_mode = terminal.TerminalOutput(self.bot.name)

        self.in_mode = in_mode
        self.out_mode = out_mode

        # if train:
            # self.bot.train('chatterbot.corpus.portuguese')
            # self.bot.train('./data/luzes.yml')
            # self.bot.train('./data/portao.yml')

    def welcome_chat(self):
        self.out_mode.response(f'Oi, eu me chamo {self.name}! O que deseja?')

    def process_command(self, text):
        self.command.text = text
        if self.command.is_valid():
            print("Executando o comando...")
            success = self.command.run()
            if success:
                return True, ''
        return False, self.command.error

    def listen(self):
        return self.in_mode.input()

    def get_response(self, statement):
        return self.bot.get_response(statement)
    
    def speak(self, statement):
        self.out_mode.response(statement)
        return response


if __name__ == '__main__':
    user_name = input(f'Digite aqui o seu nome: ')
    bot = Ada(user_name, in_mode=voice.VoiceInput(), out_mode=voice.VoiceOutput())
    bot.welcome_chat()
    while True:
        your_message = bot.listen()
        if your_message:
            response = bot.get_response(your_message)
            bot.speak(response)
            success, response_error = bot.process_command(your_message)
            if success:
                bot.speak(f'Pronto')
            elif response_error:
                bot.speak(response_error)

                