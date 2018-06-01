from adabot import Bot
from adabot import settings
from adabot.command import WitCommand, Intent
from adabot.runner import RequestRunner


if __name__ == '__main__':
    human_name = input(f'Digite aqui o seu nome: ')
    bot = Bot(name='Alícia', human_name=human_name, train=False)

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
