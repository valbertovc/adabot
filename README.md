# Ada chatbot

Ada é um chatbot criado com a finalidade de integrar automação residencial com comandos de voz.
Seu objetivo é integrar tecnologias de reconhecimento de comandos do usuário, aprendizagem de
máquina, comunicação por voz e por texto e a plataforma arduino.

Por padrão, Ada é configurada para interagir através do terminal onde você digita textos e
recebe as respostas dela. É possível configurar para interagir através de comandos de voz.

# Instalação

```shell
pip install git+https://github.com/valbertovc/adabot.git
```

> Recomendo configurar previamente um virtualenv para instalação local (virtualenvwrapper).

# Requisitos

- Linux
- Python 3.6
- mpg123

# Exemplo inicial

Executar o comando para baixar o arquivo de exemplo com um código pronto (opcional):

```shell
wget https://github.com/valbertovc/adabot/blob/master/example/ada_terminal_mode.py
```

O código abaixo é um exemplo inicial de como começar a usar adabot como um chatbot comum. Crie um arquivo exemplo.py,
 cole o código dentro e execute com o comando: `python exemplo.py`

```python
from adabot import Bot

if __name__ == '__main__':
    bot = Bot()
    bot.train('chatterbot.corpus.portuguese')
    while True:
        your_message = bot.listen()
        if your_message:
            response = bot.get_response(your_message)
            bot.speak(response)
```

# Comandos

A execução de comandos é o diferencial e permite que adabot entenda e execute-os como você deseja. Para isso
ela pode utilizar serviços web (ou até mesmo uma implementação própria) que permita transformar um texto livre em
parâmetros que resultarão em um comando. Adabot possui a classe WitCommand que permite a comunicação com o serviço
Wit.ai. Este serviço recebe um texto qualquer, interpreta-o e devolve o conjunto de parâmetros identificados. Exemplo:

- Texto: Acenda a luz da sala
- Resposta do wit.ai: {'action': 'acender', 'object': 'lampada', 'local': 'sala'}

O wit.ai precisa ser configurado para receber os texto e interpretá-los corretamente como você deseja. É importante
pensar nos diversos sinônimos de palavras e como as pessoas podem escrever textos diferentes.

# Runners

Os executadores de comandos permitem a configuração da forma como o comando será executado. Adabot possui o
RequestRunner que envia os parâmetros através de um HTTP request do tipo GET. Assim, é possível executar o
comando quando ele for válido. Neste caso, temos uma url de uma ethernet shield acoplada a um arduino que receberá
o request e interpretará os parâmetros enviados para ela.

# Intent

Para identificar quando se trata de um comando ou de uma conversa comum, o comando usa uma casse chamada Intent.
Ela precisa de dois parâmetros básicos, o conjunto de palavras que identificam a intenção de executar um comando
(keywords) e o número mínimo de palavras deste conjunto para que o comando seja executado (min_words). No exemplo
abaixo eu configurei para executar quando existirem pelo menos duas palavras de comando.

# Configurando comandos

- Crie uma conta no wit.ai, configure os comandos que deseja.
- Obtenha a chave de acesso (token) para a comunicação com o wit.ai
- Configure um runner para executar os comandos
- Configure uma intent que identifica as palavras relacionadas a comandos


```python
from adabot import Bot
from adabot import settings
from adabot.command import WitCommand, Intent
from adabot.runner import RequestRunner


if __name__ == '__main__':
    bot = Bot()
    bot.train('chatterbot.corpus.portuguese')
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
                bot.speak('Pronto')
            elif response_error:
                bot.speak(response_error)
```
