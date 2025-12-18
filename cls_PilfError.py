
class BcoError:

    def __init__(self, exception_type=Exception, error_text='Default error text. If you see this, I messed up.'):
        self.exception_type = exception_type
        self.error_text = error_text

    
    def throw_error(self):
        match self.exception_type:
            case _: raise Exception(self.error_text)

