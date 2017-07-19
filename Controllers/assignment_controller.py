from View import codecooler_view
from Models.assignment import Assignment
from data_manager import DataManager
from time import sleep
from Models.submit_assignment import SubmitAssignment
from Controllers import student_controller


def start_controller(students):
    """
    Contain main logic for AssignmentController.
    Ask user about assigemnt details and add it to assigments list
    """
    is_empty = True

    assgn_details = codecooler_view.get_inputs("Add assignment", ["Title", "Description", "Deadline"])
    is_empty = is_empty_input(assgn_details)

    if not is_empty:
        Assignment.assignments.append(Assignment(assgn_details[0], assgn_details[1], assgn_details[2]))
        save_assignment(assgn_details)
        codecooler_view.print_result('Succesfuly added assignment.')
        _create_student_assigments(students, assgn_details[0])

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


def _create_student_assigments(students, title):
    # print(assignments)
    # print(students)
    # print(title)
    for student in students:
        student_assigment = SubmitAssignment(student.idx, "None", title, "None")
        # print(student_assigment)
        # print(student_assigment.idx)
        assignments = student_controller.read_assignments("objects")
        assignments.append(student_assigment)

        student_controller.save_assignments(assignments)
