try:
    from settings_dev import *
except ImportError:
    pass

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, 'adabot', 'audio')

# Define url address for arduino
# ARDUINO_URL = ''

# Enable for use with wit.ai
# WIT_TOKEN = ''

INTENT_WORDS = ['acenda', 'acender', 'acende',
                'ligue', 'ligar','liga',
                'desligar', 'desliga', 'desligue',
                'portao', 'portão',
                'lampada', 'lâmpada', 'luz', 'sala', 'garagem',
                'banheiro',
                'externo', 'externa',
                'abra', 'abre', 'abrir',
                'feche', 'fecha', 'fechar']