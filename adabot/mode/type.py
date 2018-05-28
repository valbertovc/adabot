class InputType(object):
    """ Interface for input types """

    def input(self, *args, **kwargs):
        raise NotImplementedError

class OutputType(object):
    """ Interface for output types """
    
    def response(self, statement, *args, **kwargs):
        raise NotImplementedError