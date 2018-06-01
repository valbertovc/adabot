import logging as log


def logging():
    log.basicConfig(level=log.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(name)-18s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='adabot.log',
                    filemode='w')
    return log
