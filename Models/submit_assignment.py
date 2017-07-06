from datetime import datetime


class SubmitAssignment:
    """This class represents students submited assigements

    Attributes:
        assignments (list): list of Codecool students assigemnts
    """

    assignments = []

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
