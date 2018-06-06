from adabot import Bot

if __name__ == '__main__':
    adabot = Bot()
    adabot.bot.train('chatterbot.corpus.portuguese')
    while True:
        your_message = adabot.listen()
        if your_message:
            response = adabot.get_response(your_message)
            adabot.speak(response)
