import os

try:
    from settings_dev import *
except ImportError:
    pass

BASE_DIR = os.getcwd()
AUDIO_DIR = os.path.join(BASE_DIR, 'adabot', 'audio')
DATA_DIR = os.path.join(BASE_DIR, 'adabot', 'data')

LANGUAGE='pt-BR'

# Define url address for arduino
# ARDUINO_URL = ''

# Enable for use with wit.ai
# WIT_TOKEN = ''
# WIT_AI_KEY = ''

INTENT_WORDS = ['acenda', 'acender', 'acende',
                'ligue', 'ligar', 'liga',
                'desligar', 'desliga', 'desligue',
                'portao', 'portão',
                'lampada', 'lâmpada', 'luz', 'sala', 'garagem',
                'banheiro',
                'externo', 'externa',
                'abra', 'abre', 'abrir',
                'feche', 'fecha', 'fechar']
