from datetime import datetime
from Data import tools

class SubmitAssignment:
    """This class represents students submited assigements

    Attributes:
        assignments (list): list of Codecool students assigemnts
    """
    submit_assignments = []
    _file_name = 'csv/submitted_assgn.csv'

    def __init__(self, idx, link, name, date=None):
        """
        Constructor of SubmitAssignment object.

        Args:
            idx (string): uniqe student id
            link (string): link to gitHub or other website with done assigement
            name (string): name of submited assigemnt
            date (:obj: `datetime.date`): date of assigemnt's submition
        """
        self.idx = idx
        self.link = link
        self.name = name

        if type(date) == str:
            self.date = date
        else:
            date = datetime.today()
            self.date = "{}.{}.{} - {}:{}".format(date.day, date.month, date.year, date.hour, date.minute)


    @classmethod
    def add_assignment(cls, task):
        if type(task) == SubmitAssignment:
            cls.submit_assignments.append(task)

        else:
            raise TypeError('Wrong values you tried to push here.')
            
    @classmethod
    def get_submit_assignments_list(cls):
        return cls.submit_assignments

    @classmethod
    def load_submit_assignments(cls):
        cls.submit_assignments = tools.get_data_from_file(cls._file_name, SubmitAssignment)

    @classmethod
    def get_records_from_objects(cls):
        temp = []

        for task in cls.submit_assignments:
            temp.append([task.idx, task.link, task.name, task.date])

        return temp

    @classmethod
    def save_submit_assignments(cls):
        submit_assignments_data_records = cls.get_records_from_objects()
        tools.save_data_to_file(cls._file_name, submit_assignments_data_records)
