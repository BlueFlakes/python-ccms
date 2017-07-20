from data_manager import DataManager

def get_data_from_file(file_name, object_type):
    """
    Convert data from csv file to SubmitAssignment object and add it to list

    Args:
        return_type (string): indicate whta type return will be
    """
    temp_list_of_records = DataManager.read_file(file_name)
    temp_list_of_objects = []

    for record in temp_list_of_records:
        to_append = object_type(*record)

        temp_list_of_objects.append(to_append)

    return temp_list_of_objects

def convert_objects_to_record(person_objects):
    temp = []

    for person in person_objects:
        temp.append([person.idx, person.password, person.name,
                                 person.surname, person.email, person.registration_date])

    return temp

def save_data_to_file(file_name, data, staff=False):
    if staff:
        data = convert_objects_to_record(data)

    DataManager.save_file(file_name, data)
