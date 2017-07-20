class Codecooler:
    """This abstract class represents Codecooler person"""

    def __init__(self, login, password, name, surname, email, registration_date):
        """
        Constructor of Codecooler object.

        Args:
            login (string): uniqe person login
            password (string): uniqe person's password
            name (string): person's name
            surname (string): person's surname
            email (string): person's email

        """
        self.idx = login
        self.password = password
        self.name = name
        self.surname = surname
        self.email = email
        self.registration_date = registration_date
