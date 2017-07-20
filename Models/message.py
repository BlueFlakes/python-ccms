class Message:

    def __init__(self, author, sentence):
        self.author = author
        self.sentence = sentence

    def compilated_message(self):
        return [self.author, self.sentence]
