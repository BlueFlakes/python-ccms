from Data import tools
from datetime import datetime, date


class SubmitAssignment:
    """This class represents students submited assigements

    Attributes:
        assignments (list): list of Codecool students assigemnts
        _file_name (string): name of file to open
    """
    submit_assignments = []
    _file_name = 'csv/submitted_assgn.csv'

    def __init__(self, idx, link, title, deadline, status='not provided'):
        """
        Constructor of SubmitAssignment object.

        Args:
            idx (string): uniqe student id
            link (string): link to gitHub or other website with done assigement
            name (string): name of submited assigemnt
            deadline (:obj: `date`): deadline of assigment
            status (string): tell if assigment is submited
        """

        self.idx = idx
        self.link = link
        self.title = title
        self.deadline = deadline
        self.status = status

    def convert_deadline(self, deadline_update):
        """
        Convert string to date objecs

        Args:
            deadline_update (string): date as string
        """
        self.deadline = datetime.strptime(deadline_update, "%Y-%m-%d").date()

    @classmethod
    def add_assignment(cls, task):
        """
        Add SubmitAssignment object to submit_assignments list

        Args:
            task (:obj: `SubmitAssignment`): assigment to submit by student
        """

        cls.submit_assignments.append(task)

    @classmethod
    def get_submit_assignments_list(cls):
        """
        Returns:
            list of :obj: `SubmitAssignment`: list of all submited assigments
        """

        return cls.submit_assignments

    @classmethod
    def load_submit_assignments(cls):
        """
        Call function to open csv file and convert it rows to SubmitAssignment objects
        """

        cls.submit_assignments = tools.get_data_from_file(cls._file_name, SubmitAssignment)

    @classmethod
    def get_records_from_objects(cls):
        """
        Get specified attributes from object

        Returns:
            list of lists: list with attributes of all SubmitAssignment objects
        """

        temp = []

        for task in cls.submit_assignments:
            temp.append([task.idx, task.link, task.title, str(task.deadline), task.status])

        return temp

    @classmethod
    def save_submit_assignments(cls):
        """
        Call functions to save SubmitAssignment to csv file
        """

        submit_assignments_data_records = cls.get_records_from_objects()
        tools.save_data_to_file(cls._file_name, submit_assignments_data_records)
