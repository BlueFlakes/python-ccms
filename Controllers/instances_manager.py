from View.codecooler_view import CodecoolerView
from Controllers.tools import Tools
from time import sleep

class InstancesList:

    @staticmethod
    def get_person(a_list, title, task):
        """Check is there such user

        Args:
            login (str): user login

        Return:
            accounts_list (object) or None if couldn't find user.

        """
        idx = CodecoolerView.get_inputs(title, task)[0]
        person = None

        for homie in a_list:
            if homie.idx == idx:
                person = homie
                break

        if person:
            return person

        else:
            print('Not found person !')
            sleep(1.5)


    @classmethod
    def remove_person(cls, a_list):
        """Remove given user if he exist.

        Args:
            login (str): user login

        Return:
            None

        """
        title = 'Remove person'
        task = ['Provide me a idx of person to delete']

        try:
            a_list.remove(cls.get_person(a_list, title, task))
            print('Succesful remove :)')
            sleep(1.5)

        except ValueError:
            pass



    @staticmethod
    def add_person(a_list, obj_to_create ,title, questions):
        """Add person to the list

        Args:
            person (object): Student or mentor object in this case

        Return:
            None

        """
        person = CodecoolerView.get_inputs(title, questions)
        idx = Tools.gen_idx(obj_to_create.__name__.lower())
        a_list.append(obj_to_create(idx, *person))
        print('Succesfully added new person.')
        sleep(1.5)

    @classmethod
    def modify_person_details(cls, a_list, choosen_detail, title, task):
        person = cls.get_person(a_list, 'Choose person', ['Please provide person idx to modify'])

        if person:
            updated_information = CodecoolerView.get_inputs(title, task)[0]
            cls._modify_person_details_requests(person, choosen_detail, updated_information)

    @staticmethod
    def _modify_person_details_requests(person, choosen_detail, updated_information):
        if choosen_detail == 'name':
            person.name = updated_information

        elif choosen_detail == 'password':
            person.password = updated_information

        elif choosen_detail == 'email':
            person.email = updated_information

        elif choosen_detail == 'surname':
            person.surname = updated_information
