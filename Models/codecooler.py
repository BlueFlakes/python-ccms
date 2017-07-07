class Codecooler:
    """This abstract class represents Codecooler person"""

    def __init__(self, idx, password, name, surname, email):
        """
        Constructor of Codecooler object.

        Args:
            idx (string): uniqe person id
            password (string): uniqe person's password
            name (string): person's name
            surname (string): person's surname
            email (string): person's email
        """
        self.idx = idx
        self.password = password
        self.name = name
        self.surname = surname
        self.email = email
