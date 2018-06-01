from wit import Wit
from adabot.utils import logging

logger = logging().getLogger(__name__)


class Commmand(object):
    error = ''

    def __init__(self, runner, *args, **kwargs):
        self.runner = runner
        self.params = kwargs
        self.text = ''

    def is_valid(self):
        raise NotImplementedError

    def run(self, **kwargs):
        success = self.runner.run(**kwargs)
        if success:
            self.error = ''
        else:
            self.error = self.runner.error
        return success


class WitCommmand(Commmand):

    def __init__(self, token, intent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wit = Wit(token)
        self.intent = intent

    def __run(self):
        self.process_wit_response()
        if self.is_valid():
            return super().run(**self.params)
        return False

    def run(self, text=None):
        if text:
            self.text = text
        error = ''
        success = False
        if self.is_valid():
            logger.info("Executando o comando...")
            success = self.__run()
            error = self.error
        return success, error

    def is_valid(self):
        return self.text and self.intent.is_valid(self.text)

    def process_wit_response(self):
        self.params.clear()
        logger.info(f'Enviando para wit.ai: {self.text}')
        response = self.wit.message(self.text)
        entities = response['entities']
        for entitie, data in entities.items():
            self.params[entitie] = data[0]['value']
        logger.info(f'Parâmetros wit.ai: {self.params}')


class Intent(object):

    def __init__(self, min_words=0, keywords=None, *args, **kwargs):
        self.keywords = keywords if keywords else []
        self.min_words = min_words

    def extract_words(self, text):
        words = str(text).lower().split()
        return [word for word in self.keywords if word in words]

    def is_valid(self, text):
        words = self.extract_words(text)
        return len(words) >= self.min_words
