from Models.codecooler import Codecooler
from Data import tools

class Mentor(Codecooler):
    """
    This class represents Codecoole mentor

    Attributes:
        mentor_list (list): list of Codecool mentors

    """
    mentor_list = []
    _file_name = 'csv/mentors.csv'

    @classmethod
    def get_mentor_list(cls):
        return cls.mentor_list

    @classmethod
    def load_mentors(cls):
        cls.mentor_list = tools.get_data_from_file(cls._file_name, Mentor)

    @classmethod
    def save_mentors(cls):
        tools.save_data_to_file(cls._file_name, cls.mentor_list, staff=True)
