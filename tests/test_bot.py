import unittest
from adabot import adabot

class BotNames(unittest.TestCase):

    def setUp(self):
        self.bot = adabot.Bot("Ada", "Human", train=False)

    def test_bot_name(self):
        self.assertEqual(self.bot.name, "Ada")

    def test_bot_human_name(self):
        self.assertEqual(self.bot.human_name, "Human")

    def test_can_speak(self):
        text = "Text to speak"
        self.assertTrue(text in self.bot.speak(text))

    def test_can_process_comand(self):
        text = "palavras fora das keywords"
        success, error_message = self.bot.process_command(text)
        self.assertEqual(success, False)
        self.assertEqual(error_message, '')


if __name__ == '__main__':
    unittest.main()
