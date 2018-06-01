import requests
from adabot.utils import logging

logger = logging().getLogger(__name__)


class CommandRunner(object):
    error = ''

    def run(self, *args, **kwargs):
        raise NotImplementedError


class RequestRunner(CommandRunner):
    def __init__(self, url, **kwargs):
        self.url = url
        self.params = kwargs
        self.response = None

    def set_params(self, **kwargs):
        self.params = kwargs

    def run(self, *args, **kwargs):
        try:
            response = requests.get(self.url, kwargs)
            self.response = response
            return response.status_code == 200
        except requests.exceptions.ConnectionError as e:
            logger.exception('ConnectionError: %s', e)
            self.error = 'Houve um erro na conexão'
            return False
