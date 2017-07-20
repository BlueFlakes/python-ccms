from Data import tools

class SubmitAssignment:
    """This class represents students submited assigements

    Attributes:
        assignments (list): list of Codecool students assigemnts
    """
    submit_assignments = []
    _file_name = 'csv/submitted_assgn.csv'

    def __init__(self, idx, link, title, date='', status='not provided'):
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
        self.title = title
        self.date = self.add_date(date)
        self.status = status


    def add_date(self, date):
        try:
            self.date = date(date)

        except TypeError:
            self.date = date

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
        print(cls.submit_assignments)

    @classmethod
    def get_records_from_objects(cls):
        temp = []

        for task in cls.submit_assignments:
            temp.append([task.idx, task.link, task.title, task.status, task.date])

        return temp

    @classmethod
    def save_submit_assignments(cls):
        submit_assignments_data_records = cls.get_records_from_objects()
        tools.save_data_to_file(cls._file_name, submit_assignments_data_records)
