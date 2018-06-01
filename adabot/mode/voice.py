import os
import subprocess

import speech_recognition as sr
from gtts import gTTS
from slugify import slugify

from adabot.mode.type import InputType, OutputType
from adabot import settings
from adabot.utils import logging

logger = logging().getLogger(__name__)


class VoiceInput(InputType):

    def __init__(self, language=None):
        self.language = language
        self.recognizer = r = sr.Recognizer()

    def input(self):
        return self.listen()

    def listen(self):
        logger.info('Escutando...')
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            logger.info('Escutei...')
            return self.recognize(audio)

    def recognize(self, audio):
        raise NotImplemented


class WitVoiceInput(VoiceInput):

    def __init__(self, wit_ai_key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wit_ai_key = wit_ai_key

    def recognize(self, audio):
        try:
            text = self.recognizer.recognize_wit(audio, key=self.wit_ai_key)
        except sr.UnknownValueError as e:
            logger.exception('UnknownValueError: %s', e)
            text = 'Não entendi'
        except sr.RequestError as e:
            logger.exception('RequestError: %s', e)
            text = 'Não consegui processar a sua voz'
        return text


class GoogleVoiceInput(VoiceInput):

    def recognize(self, audio):
        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
        except sr.UnknownValueError as e:
            logger.exception('UnknownValueError: %s', e)
            text = 'Não entendi'
        except sr.RequestError as e:
            logger.exception('RequestError: %s', e)
            text = 'Não consegui processar a sua voz'
        return text


class VoiceOutput(OutputType):

    def __init__(self, language=None):
        self.language = language


class GoogleVoiceOutput(VoiceOutput):

    def response(self, statement, *args, **kwargs):
        statement = str(statement)
        return self.speak(statement)

    def speak(self, text):
        tts = gTTS(text=text, lang=self.language)
        slug_name = slugify(text) + '.mp3'
        file_name = os.path.join(settings.AUDIO_DIR, slug_name)
        if not os.path.exists(file_name):
            tts.save(file_name)
        subprocess.call(["mpg123", '-q', file_name])
