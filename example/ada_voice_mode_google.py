from adabot import Bot
from adabot.mode import voice
from adabot.command import WitCommand, Intent
from adabot.runner import RequestRunner
from adabot import settings


if __name__ == '__main__':
    bot = Bot(name='Cristina', train=False)
    bot.in_mode = voice.GoogleVoiceInput(language=settings.LANGUAGE)
    bot.out_mode = voice.GoogleVoiceOutput(language=settings.LANGUAGE)

    bot.speak(f'Oi, eu me chamo {bot.name}!')
    bot.speak('Como você se chama?')
    human_name = bot.listen()
    bot.human_name = human_name
    bot.speak(f'Olá {bot.human_name}, em que posso ajudar?')

    command = WitCommand(token=settings.WIT_TOKEN,
                          runner=RequestRunner(url=settings.ARDUINO_URL),
                          intent=Intent(min_words=2, keywords=settings.INTENT_WORDS))

    while True:
        your_message = bot.listen()
        if your_message:
            response = bot.get_response(your_message)
            bot.speak(response)
            success, response_error = command.run(your_message)
            if success:
                bot.speak(f'Pronto')
            elif response_error:
                bot.speak(response_error)
