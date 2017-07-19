from datetime import date


class Assignment:
    """
    This class represents assigment created by mentor

    Attributes:
        assignments (list): list of created assigments
    """
    assignments = []

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
