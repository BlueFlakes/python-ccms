from Models.codecooler import Codecooler
from Data import tools


class OfficeManager(Codecooler):
    """
    This class represents Codecoole office employee

    Attributes:
        office_managers (list): list of Codecool office employee
        _file_name (string): name of file to open
    """

    office_managers_list = []
    _file_name = 'csv/officemanagers.csv'

    @classmethod
    def get_office_managers_list(cls):
        """
        Returns:
            list of :obj: `OfficeManager`: list of all office managers
        """

        return cls.office_managers_list

    @classmethod
    def load_office_managers(cls):
        """
        Call function to open csv file and convert it rows to OfficeManager objects
        """

        cls.office_managers_list = tools.get_data_from_file(cls._file_name, OfficeManager)

    @classmethod
    def save_office_managers(cls):
        """
        Call functions to save OfficeManager to csv file
        """

        tools.save_data_to_file(cls._file_name, cls.office_managers_list, staff=True)
