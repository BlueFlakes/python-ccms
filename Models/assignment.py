from data_manager import DataManager
from Data import tools

class Assignment:
    """
    This class represents assigment created by mentor

    Attributes:
        assignments (list): list of created assigments
    """
    assignments = []
    _file_name = 'csv/assignments.csv'

    def __init__(self, title, description, deadline):
        """
        Constructor of assigment object.

        Args:
            title (string): title of assigement
            description (string): description of assigement

        """
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = 'not provided'


    @classmethod
    def get_assignments_list(cls):
        return cls.assignments

    @classmethod
    def load_assignments(cls):
        cls.assignments = tools.get_data_from_file(cls._file_name, Assignment)

    @classmethod
    def get_records_from_objects(cls):
        temp = []

        for task in cls.assignments:
            temp.append([task.title, task.description, task.deadline])

        return temp

    @classmethod
    def save_assignments(cls):
        assignments_data_records = cls.get_records_from_objects()
        tools.save_data_to_file(cls._file_name, assignments_data_records)
