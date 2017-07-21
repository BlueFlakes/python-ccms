class Message:
    """
    This class represents model of massage in talkbox
    """

    def __init__(self, author, sentence):
        """
        Constructor of Message object.

        Args:
            author (string): author of massage
            sentence (string): massage
        """

        self.author = author
        self.sentence = sentence

    def compilated_message(self):
        """
        Returns:
            list of strings: autro with massage as list
        """

        return [self.author, self.sentence]
