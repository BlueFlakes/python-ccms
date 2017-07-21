from Models.codecooler import Codecooler
from Data import tools


class Student(Codecooler):
    """
    This class represents Codecoole students

    Attributes:
        student_list (list): list of Codecool students
        _file_name (string): name of file to open
    """

    student_list = []
    _file_name = 'csv/students.csv'

    @classmethod
    def get_students_list(cls):
        """
        Returns:
            list of :obj: `Student`: list of all students
        """

        return cls.student_list

    @classmethod
    def load_students(cls):
        """
        Call function to open csv file and convert it rows to Student objects
        """

        cls.student_list = tools.get_data_from_file(cls._file_name, Student)

    @classmethod
    def save_students(cls):
        """
        Call functions to save Student to csv file
        """

        tools.save_data_to_file(cls._file_name, cls.student_list, staff=True)
