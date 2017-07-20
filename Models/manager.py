from Models.codecooler import Codecooler
from Data import tools


class Manager(Codecooler):
    """
    This class represents Codecoole manager

    Attributes:
        manager_list (list): list of Codecool managers
        _file_name (string): name of file to open
    """
    manager_list = []
    _file_name = 'csv/managers.csv'

    @classmethod
    def get_managers_list(cls):
        """
        Returns:
            list of :obj: `Manager`: list of all managers
        """

        return cls.manager_list

    @classmethod
    def load_managers(cls):
        """
        Call function to open csv file and convert it rows to Manager objects
        """

        cls.manager_list = tools.get_data_from_file(cls._file_name, Manager)

    @classmethod
    def save_managers(cls):
        """
        Call functions to save Manager to csv file
        """

        tools.save_data_to_file(cls._file_name, cls.manager_list, staff=True)
