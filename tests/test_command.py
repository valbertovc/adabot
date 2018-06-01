import unittest
from adabot import settings
from adabot.command import WitCommand, Intent
from adabot.runner import RequestRunner


class WitCommandTestCase(unittest.TestCase):

    def setUp(self):
        self.command = WitCommand(token=settings.WIT_TOKEN,
                              runner=RequestRunner(url=settings.ARDUINO_URL),
                              intent=Intent(min_words=2, keywords=settings.INTENT_WORDS))

    def test_can_process_comand_with_false_return(self):
        text = "palavras fora das keywords"
        success, error_message = self.command.run(text)
        self.assertEqual(success, False)
        self.assertEqual(error_message, '')


if __name__ == '__main__':
    unittest.main()
