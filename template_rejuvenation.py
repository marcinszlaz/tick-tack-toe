class RejuvenatesTemplate:
    
    def __init__(self, dictionary, template):
        self.dictionary = dictionary
        self.template = template

    def __str__(self):
        return self.template.format(**self.dictionary)


