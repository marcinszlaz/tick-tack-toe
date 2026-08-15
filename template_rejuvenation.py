class RejuvenatesTemplate:
    
    def __init__(self, dictionary, template):
        self.dictionary = dictionary
        self.template = template

    def __str__(self):
        return self.template.format(**self.dictionary)

class Exit(Exception):
    """ 
    It's only way in Python
    to handle with exit from program
    uses multiple recurention, its very bad
    architectonic chose but it's fancy xD 
    """
    pass

