from adabot import Bot
from adabot.mode import voice
from adabot.command import WitCommmand, Intent
from adabot.runner import RequestRunner
from adabot import settings


if __name__ == '__main__':
    bot = Bot(name='Carolina', train=False)
    bot.in_mode = voice.WitVoiceInput(wit_ai_key=settings.WIT_AI_KEY)
    bot.out_mode = voice.VoiceOutput()

    bot.speak(f'Oi, eu me chamo {bot.name}!')
    bot.speak('Como você se chama?')
    human_name = bot.listen()
    bot.human_name = human_name
    bot.speak(f'Olá {bot.human_name}, em que posso ajudar?')

    command = WitCommmand(token=settings.WIT_TOKEN,
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
