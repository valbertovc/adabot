from wit import Wit


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

    keywords = ['acenda', 'acender', 'acende', 'ligue', 'ligar','liga', 'desligar', 'desliga', 'desligue',
                'portao', 'portão', 'lampada', 'lâmpada', 'luz', 'sala', 'garagem',
                'banheiro', 'externo', 'externa', 'abra', 'abre', 'abrir', 'feche', 'fecha', 'fechar']

    def __init__(self, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wit = Wit(token)

    def run(self):
        self.process_wit_response()
        return super().run(**self.params)

    def is_valid(self):
        MIN_WORDS = 2
        if self.text:
            words = self.intent_words(self.text)
            if len(words) >= MIN_WORDS:
                return True
        return False
    
    def process_wit_response(self):
        response = self.wit.message(self.text)
        entities = response['entities']
        for entitie, data in entities.items():
            self.params[entitie] = data[0]['value']

    def intent_words(self, text):
        words = str(text).lower().split()
        return [word for word in self.keywords if word in words]
