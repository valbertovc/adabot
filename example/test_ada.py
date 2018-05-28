from adabot.adabot import Bot
from adabot.mode import voice


if __name__ == '__main__':
   user_name = input(f'Digite aqui o seu nome: ')
   bot = Bot(name='Carolina', human_name=user_name, in_mode=voice.VoiceInput(),
             out_mode=voice.VoiceOutput(), train=False)

   bot.welcome_chat()

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
