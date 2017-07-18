from View import codecooler_view
from Models.assignment import Assignment
from data_manager import DataManager



def start_controller():
    """
    Contain main logic for AssignmentController.
    Ask user about assigemnt details and add it to assigments list
    """
    is_empty_input = True

    while is_empty_input:
        assgn_details = codecooler_view.get_inputs("Add assignment", ["Title", "Description"])
        is_empty_input = is_empty_input(assgn_details)


    Assignment.assignments.append(Assignment(assgn_details[0], assgn_details[1]))

    save_assignment(assgn_details)


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
            codecooler_view.print_result("You can't make assignment without title or description!")
            return True

    return False
