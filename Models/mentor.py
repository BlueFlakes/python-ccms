from Models.codecooler import Codecooler
from Data import tools


class Mentor(Codecooler):
    """
    This class represents Codecoole mentor

    Attributes:
        mentor_list (list): list of Codecool mentors
        _file_name (string): name of file to open
    """

    mentor_list = []
    _file_name = 'csv/mentors.csv'

    @classmethod
    def get_mentor_list(cls):
        """
        Returns:
            list of :obj: `Mentor`: list of all mentros
        """

        return cls.mentor_list

    @classmethod
    def load_mentors(cls):
        """
        Call function to open csv file and convert it rows to Mentor objects
        """

        cls.mentor_list = tools.get_data_from_file(cls._file_name, Mentor)

    @classmethod
    def save_mentors(cls):
        """
        Call functions to save Mentor to csv file
        """

        tools.save_data_to_file(cls._file_name, cls.mentor_list, staff=True)
