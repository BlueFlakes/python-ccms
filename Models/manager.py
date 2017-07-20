from Models.codecooler import Codecooler
from Data import tools

class Manager(Codecooler):
    """
    This class represents Codecoole manager

    Attributes:
        manager_list (list): list of Codecool managers

    """
    manager_list = []
    _file_name = 'csv/managers.csv'

    @classmethod
    def get_managers_list(cls):
        return cls.manager_list

    @classmethod
    def load_managers(cls):
        cls.manager_list = tools.get_data_from_file(cls._file_name, Manager)

    @classmethod
    def save_managers(cls):
        tools.save_data_to_file(cls._file_name, cls.manager_list, staff=True)
