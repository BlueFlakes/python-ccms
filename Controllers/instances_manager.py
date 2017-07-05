class InstancesList:

    def __init__(self):
        self.container = []

    def get_all(self):
        """Give back list with expected people."""
        return self.container

    def get_person(self, login):
        """Check is there such user

        Args:
            login (str): user login

        Return:
            accounts_list (object) or None if couldn't find user.

        """
        accounts_list = dict([[person.login, person] for person in self.container])

        try:
            return accounts_list[login]

        except KeyError:
            print('This login doesn\'t exit in our database.')

    def remove_person(self, login):
        """Remove given user if he exist.

        Args:
            login (str): user login

        Return:
            None

        """
        try:
            self.container.remove(self.get_person(login))
            print('Succesful')

        except ValueError:
            pass

    def add_person(self, person):
        """Add person to the list

        Args:
            person (object): Student or mentor object in this case

        Return:
            None

        """
        self.container.append(person)
