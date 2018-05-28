from adabot.adabot import Bot

if __name__ == '__main__':
    human_name = input(f'Digite aqui o seu nome: ')
    bot = Bot(name='Alícia', human_name=human_name, train=False)

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
