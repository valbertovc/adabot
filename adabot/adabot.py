from chatterbot import ChatBot
from .command import WitCommmand, Intent
from .runner import RequestRunner
from .mode import terminal
from .settings import WIT_TOKEN, ARDUINO_URL, INTENT_WORDS, DATA_DIR


class Bot(object):

    def __init__(self, name='Ada', human_name='Human', train=True, in_mode=None,
                 out_mode=None, confidence=0.7):
        self.name = name
        self.human_name = human_name
        self.command = WitCommmand(
            token=WIT_TOKEN,
            runner=RequestRunner(url=ARDUINO_URL),
            intent=Intent(min_words=2, keywords=INTENT_WORDS))
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

        if train:
            self.bot.train(DATA_DIR)

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
        return statement
