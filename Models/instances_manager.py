class InstancesList():

    @staticmethod
    def get_person(a_list, login):
        """Check is there such user

        Args:
            login (str): user login

        Return:
            accounts_list (object) or None if couldn't find user.

        """
        accounts_list = dict([[person.login, person] for person in a_list])

        try:
            return accounts_list[login]

        except KeyError:
            print('This login doesn\'t exit in our database.')

    @staticmethod
    def remove_person(a_list, login):
        """Remove given user if he exist.

        Args:
            login (str): user login

        Return:
            None

        """
        try:
            a_list.remove(self.get_person(login))
            print('Succesful')

        except ValueError:
            pass


    @staticmethod
    def add_person(a_list, person):
        """Add person to the list

        Args:
            person (object): Student or mentor object in this case

        Return:
            None

        """
        a_list.append(person)
