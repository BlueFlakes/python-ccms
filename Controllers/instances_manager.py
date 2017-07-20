from View import codecooler_view
from Controllers import tools
from Models.manager import Manager
from Models.mentor import Mentor
from Models.student import Student
from Models.office_manager import OfficeManager
from time import sleep
from datetime import date


def get_person(a_list, title, task):
    """
    Check by person's id if person is on list.

    Args:
        a_list (list of :obj:): list of object representation of person
        title (string): title of performed task
        task (list of strings): list that tell user what infromation should be provided
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


def remove_person(a_list):
    """
    Remove object representation of person from list.

    Args:
        a_list (list of :obj:): list of object representation of person

    Raises:
        ValueError: if no person on persons list
    """

    title = 'Remove person'
    task = ['Provide me a idx of person to delete']

    try:
        a_list.remove(get_person(a_list, title, task))
        print('Succesful remove :)')
        sleep(1.5)

    except ValueError:
        pass


def add_person(a_list, obj_to_create, title):
    """
    Add object representation of person from list.

    Args:
        a_list (list of :obj:): list of object representation of person
        obj_to_create (class): class of person that will be created
        title (string): title of performed task

    Examples:
        obj_to_create can be Mentor or Student class depending on place of function call
    """

    person = get_user_details()
    idx = tools.gen_idx(obj_to_create.__name__.lower())
    a_list.append(obj_to_create(idx, *person))
    codecooler_view.print_result('Succesfully added new person.')
    sleep(1.5)


def get_user_details():
    """
    Return detail about person

    Returns:
        list of strings: list of strings with details about person as fallow:
        password, Name, Surname, email

    Raises:
        ValueError: if person email have not proper format
    """

    questions_list = ['password', 'Name', 'Surname', 'email']
    user_details = []

    for question in questions_list:
        user_input = None

        while not user_input:
            user_input = codecooler_view.get_inputs('', [question])[0]
            try:
                user_input = additional_filters_for_user_details(question, user_input)
            except ValueError as err:
                print(err)
                user_input = None

        user_details.append(user_input)

    today = date.today()
    today = "{}.{}.{}".format(today.day, today.month, today.year)
    user_details.append(today)

    return user_details


def additional_filters_for_user_details(question, user_input):
    """
    Validation of person eamil format.

    Returns:
        string: person email

    Raises:
        ValueError: if person email have not proper format
    """

    if question == 'email':
        expected_signs = ['@', '.']

        for sign in expected_signs:
            if sign not in user_input:
                raise ValueError("Not proper email format\n")

    return user_input


def modify_person_details(a_list, choosen_detail, title, task):
    """
    Modify given information about person

    Args:
        a_list (list of :obj:): list of object representation of person
        choosen_detail (string): detail about person we want to change
        title (string): title of performed task
        task (list of strings): list that tell user what infromation should be provided

    Raises:
        ValueError: if person email have not proper format
    """

    person = get_person(a_list, 'Choose person', ['Please provide person idx to modify'])

    if person:
        updated_information = codecooler_view.get_inputs(title, task)[0]

        try:
            updated_information = additional_filters_for_user_details(choosen_detail, updated_information)
        except ValueError as err:
            print(err)
            sleep(1.5)
        else:
            _modify_person_details_request(person, choosen_detail, updated_information)


def _modify_person_details_request(person, choosen_detail, updated_information):
    """
    Use to modify detail about choosen person

    Args:
        person (:obj:): object representation of person
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
