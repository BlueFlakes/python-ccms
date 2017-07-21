from data_manager import DataManager
from Data import tools
from datetime import date


class Assignment:
    """
    This class represents assigment created by mentor

    Attributes:
        assignments (:obj: `Assignment`): list of created assigments
        _file_name (string): name of file to open
    """
    assignments = []
    _file_name = 'csv/assignments.csv'

    def __init__(self, title, description, deadline):
        """
        Constructor of assigment object.

        Args:
            title (string): title of assigement
            description (string): description of assigement
            deadline (:obj: `date`): deadline of assigment
        """

        self.title = title
        self.description = description
        self.deadline = deadline

    @classmethod
    def get_assignments_list(cls):
        """
        Returns:
            list of :obj: `Assignment`: list of all assigments
        """

        return cls.assignments

    @classmethod
    def load_assignments(cls):
        """
        Call function to open csv file and convert it rows to Assignment objects
        """

        cls.assignments = tools.get_data_from_file(cls._file_name, Assignment)

    @classmethod
    def get_records_from_objects(cls):
        """
        Get specified attributes from object

        Returns:
            list of lists: list with attributes of all assignments objects
        """

        temp = []

        for task in cls.assignments:
            temp.append([task.title, task.description, task.deadline])

        return temp

    @classmethod
    def save_assignments(cls):
        """
        Call functions to save Assignment to csv file
        """

        assignments_data_records = cls.get_records_from_objects()
        tools.save_data_to_file(cls._file_name, assignments_data_records)
