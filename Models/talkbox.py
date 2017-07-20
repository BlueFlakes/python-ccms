from Data import tools
from Models.message import Message


class TalkBox:
    """
    This class represents Talkbox

    Attributes:
        talkbox (:obj: `TalkBox`): list of masseges
        _file_name (string): name of file to open
    """

    talkbox = []
    _file_name = 'csv/talkbox.csv'

    @classmethod
    def get_talkbox(cls):
        """
        Returns:
            list of :obj: `TalkBox`: list of all masseges
        """

        return cls.talkbox

    @classmethod
    def add_message(cls, author, sentence):
        """
        Inser Message object to talkbox and leave only last twenty.

        Args:
            author (string): author of massege
            sentence (string): text of massege
        """

        cls.talkbox.insert(0, Message(author, sentence))
        cls.talkbox = cls.talkbox[:20]

    @classmethod
    def load_talkbox(cls):
        """
        Call function to open csv file and convert it rows to Talkbox objects
        """

        cls.talkbox = tools.get_data_from_file(cls._file_name, Message)

    @classmethod
    def get_records_from_objects(cls):
        """
        Get specified attributes from object

        Returns:
            list of lists: list with attributes of all Message objects
        """

        temp = []

        for message in cls.talkbox:
            temp.append(message.compilated_message())

        return temp

    @classmethod
    def save_talkbox(cls):
        """
        Call functions to save Talkbox to csv file
        """

        talkbox_data_records = cls.get_records_from_objects()
        tools.save_data_to_file(cls._file_name, talkbox_data_records)
