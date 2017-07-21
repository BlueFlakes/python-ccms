from Data import tools


class Grade:
    """
    This class represents grade assign to submited assigment

    Attributes:
        grades_list (list of :obj: `Grade`): list of created grades
        _file_name (string): name of file to open
    """

    grades_list = []
    _file_name = 'csv/grades.csv'

    def __init__(self, idx, title, grade):
        """
        Constructor of grade object.

        Args:
            idx (string): uniqe person id
            title (string): title of assigement
            grade (int): grade of assigment
        """

        self.idx = idx
        self.title = title
        self.grade = grade

    @classmethod
    def get_grades_list(cls):
        """
        Returns:
            list of :obj: `Grade`: list of all grades
        """
        return cls.grades_list

    @classmethod
    def add_grade(cls, idx, title, grade):
        """
        Add new Grade object to grade's list

        Args:
            idx (string): uniqe person id
            title (string): title of assigement
            grade (int): grade of assigment
        """

        cls.grades_list.append(Grade(idx, title, grade))

    @classmethod
    def load_grades(cls):
        """
        Call function to open csv file and convert it rows to Grade objects
        """

        cls.grades_list = tools.get_data_from_file(cls._file_name, Grade)

    @classmethod
    def get_records_from_objects(cls):
        """
        Get specified attributes from object

        Returns:
            list of lists: list with attributes of all Grade objects
        """

        temp = []

        for task in cls.grades_list:
            temp.append([task.idx, task.title, task.grade])

        return temp

    @classmethod
    def save_grades(cls):
        """
        Call functions to save Grade to csv file
        """

        grades_data_records = cls.get_records_from_objects()
        tools.save_data_to_file(cls._file_name, grades_data_records)
