from View import codecooler_view
from Controllers import tools
from Models.manager import Manager
from Models.mentor import Mentor
from Models.student import Student
from Models.office_manager import OfficeManager
from time import sleep


def get_person(a_list, title, task):
    """
    Check is there such user

    Args:
        login (str): user login

    Return:
        accounts_list (object) or None if couldn't find user.
    """

    idx = codecooler_view.get_inputs(title, task)[0]
    person = None

    for homie in a_list:
        if homie.idx == idx:
            person = homie
            break

    if person:
        return person

    else:
        print('Not found person!')
        sleep(1.5)


def remove_person(cls, a_list):
    """
    Remove given user if he exist.

    Args:
        login (str): user login
    """

    title = 'Remove person'
    task = ['Provide me a idx of person to delete']

    try:
        a_list.remove(get_person(a_list, title, task))
        print('Succesful remove :)')
        sleep(1.5)

    except ValueError:
        pass


def add_person(a_list, obj_to_create, title, questions):
    """
    Add person to the list

    Args:
        person (object): Student or mentor object in this case
    """

    person = codecooler_view.get_inputs(title, questions)
    idx = tools.gen_idx(obj_to_create.__name__.lower())
    a_list.append(obj_to_create(idx, *person))
    print('Succesfully added new person.')
    sleep(1.5)


def modify_person_details(a_list, choosen_detail, title, task):
    """
    Use to choose person and details we want to modify

    Args:
        a_list (list of :obj:): attribute of choosen class as list of persons
        choosen_detail (string): detail about person we want to change
        title (str): menu title
        task (list): list of questions
    """
    person = get_person(a_list, 'Choose person', ['Please provide person idx to modify'])

    if person:
        updated_information = codecooler_view.get_inputs(title, task)[0]
        _modify_person_details_requests(person, choosen_detail, updated_information)


def _modify_person_details_requests(person, choosen_detail, updated_information):
    """
    Use to modify detail about choosen person

    Args:
        choosen_detail (string): detail about person we want to change
        updated_information (string): updated information
    """

    if choosen_detail == 'name':
        person.name = updated_information

    elif choosen_detail == 'password':
        person.password = updated_information

    elif choosen_detail == 'email':
        person.email = updated_information

    elif choosen_detail == 'surname':
        person.surname = updated_information


def prepare_data_to_visualize(data):
    """
    Get attributes from evry objects in data list
    and add them to inner list as full detail about one object

    Args:
        data (list of :obj:): list objects where evry object is information about person
    """

    person_collection = []

    for person in data:
        person_collection.append([person.idx, person.password, person.name,
                                 person.surname, person.email])
    return person_collection


def convert_data_to_object(given_type, data):
    """
    Convert data from list of elements to proper objec and add it to list of objects

    Args:
        given_type (string): arbitrary name that indicate class of created object
        data (list of lists): list that contains details about persons as inner list

    Returns:
        list of :obj: list of objects from proper class
    """
    temp = []

    for record in data:
        idx = record[0]
        password = record[1]
        name = record[2]
        surname = record[3]
        email = record[4]

        if given_type == 'manager':
            temp.append(Manager(idx, password, name, surname, email))

        elif given_type == 'mentor':
            temp.append(Mentor(idx, password, name, surname, email))

        elif given_type == 'student':
            temp.append(Student(idx, password, name, surname, email))

        elif given_type == 'officemanager':
            temp.append(OfficeManager(idx, password, name, surname, email))

    return temp
