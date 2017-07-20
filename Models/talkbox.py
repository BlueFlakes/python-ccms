from Data import tools
from Models.message import Message

class TalkBox:
    talkbox = []
    _file_name = 'csv/talkbox.csv'

    @classmethod
    def get_talkbox(cls):
        return cls.talkbox

    @classmethod
    def add_message(cls, author, sentence):
        cls.talkbox.insert(0, Message(author, sentence))
        cls.talkbox = cls.talkbox[:20]

    @classmethod
    def load_talkbox(cls):
        cls.talkbox = tools.get_data_from_file(cls._file_name, Message)

    @classmethod
    def get_records_from_objects(cls):
        temp = []

        for message in cls.talkbox:
            temp.append(message.compilated_message())

        return temp

    @classmethod
    def save_talkbox(cls):
        talkbox_data_records = cls.get_records_from_objects()
        tools.save_data_to_file(cls._file_name, talkbox_data_records)
