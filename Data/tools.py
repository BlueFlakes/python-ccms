from data_manager import DataManager


def get_data_from_file(file_name, object_type):
    """
    Convert data from csv file to SubmitAssignment object and add it to list

    Args:
        file_name (string): name of file to open
        return_type (:class:): indicate what class return will be

    Returns:
        list of :obj:: temporary list of objects
    """

    temp_list_of_records = DataManager.read_file(file_name)
    temp_list_of_objects = []

    for record in temp_list_of_records:
        to_append = object_type(*record)

        temp_list_of_objects.append(to_append)

    return temp_list_of_objects


def convert_objects_to_record(person_objects):
    """
    Change object to list of attributes and add to list

    Args:
        person_objects (:obj:): object representing person

    Returns
        list of lists: list of list objects attrubutes
    """

    temp = []

    for person in person_objects:
        temp.append([person.idx, person.password, person.name,
                    person.surname, person.email, person.registration_date])

    return temp


def save_data_to_file(file_name, data, staff=False):
    """
    Save given date to file

    Args:
        file_name (string): name of file to open
        data (:obj:): object representing person
        staff (bool): if save to file
    """

    if staff:
        data = convert_objects_to_record(data)

    DataManager.save_file(file_name, data)
