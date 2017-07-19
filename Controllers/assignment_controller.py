from View import codecooler_view
from Models.assignment import Assignment
from data_manager import DataManager
from time import sleep


def start_controller():
    """
    Contain main logic for AssignmentController.
    Ask user about assigemnt details and add it to assigments list
    """
    is_empty = True

    assgn_details = codecooler_view.get_inputs("Add assignment", ["Title", "Description"])
    is_empty = is_empty_input(assgn_details)

    if not is_empty:
        Assignment.assignments.append(Assignment(assgn_details[0], assgn_details[1]))
        save_assignment(assgn_details)
        codecooler_view.print_result('Succesfuly added assignment.')

    else:
        codecooler_view.print_error_message('Wrong type of title or description.')

    sleep(2)


def save_assignment(assgn):
    """
    Save list of assignments in csv file

    Args:
        assgn (list of :obj: `Assignment`): list with all assigmnts

    """
    DataManager.extend_file("csv/assignments.csv", assgn)


def is_empty_input(assgn_details):

    for answer in assgn_details:
        if len(answer) < 1:
            return True

    return False
