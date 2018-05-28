from adabot.adabot import Bot
from adabot.mode import voice

if __name__ == '__main__':
    bot = Bot(name='Carolina', train=False)
    bot.in_mode = voice.VoiceInput()
    bot.out_mode = voice.VoiceOutput()

    bot.speak(f'Oi, eu me chamo {bot.name}!')
    bot.speak('Como você se chama?')
    human_name = bot.listen()
    bot.human_name = human_name
    bot.speak(f'Olá {bot.human_name}, em que posso ajudar?')

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
