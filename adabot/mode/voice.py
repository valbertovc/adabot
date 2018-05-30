import os
import subprocess

import speech_recognition as sr
from gtts import gTTS
from slugify import slugify

from adabot.mode.type import InputType, OutputType
from adabot import settings


class VoiceInput(InputType):

    def __init__(self):
        self.recognizer = r = sr.Recognizer()

    def input(self):
        return self.listen()

    def listen(self):
        print('Escutando...')

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            print('Escutei...')
            return self.recognize(audio)

    def recognize(self, audio):
        raise NotImplemented


class WitVoiceInput(VoiceInput):

    def __init__(self, wit_ai_key):
        super().__init__()
        self.wit_ai_key = wit_ai_key

    def recognize(self, audio):
        try:
            text = self.recognizer.recognize_wit(audio, key=self.wit_ai_key)
        except sr.UnknownValueError:
            text = 'Não entendi'
        except sr.RequestError as e:
            print(e)
            text = 'Não consegui processar a sua voz'
        return text


class VoiceOutput(OutputType):

    def response(self, statement, *args, **kwargs):
        statement = str(statement)
        return self.speak(statement)

    def speak(self, text):
        tts = gTTS(text=text, lang='pt-BR')
        slug_name = slugify(text) + '.mp3'
        file_name = os.path.join(settings.AUDIO_DIR, slug_name)
        if not os.path.exists(file_name):
            tts.save(file_name)
        subprocess.call(["mpg123", '-q', file_name])
