from View import codecooler_view
from data_manager import DataManager
from Models.assignment import Assignment
from Models.submit_assignment import SubmitAssignment
from Controllers import student_controller
from time import sleep
from datetime import date


def start_controller(students):
    """
    Contain main logic for AssignmentController.
    Ask user about assigemnt details and add it to assigments list
    """
    "is_empty = True"
    questions = ["Title", "Description"]
    deadline_questions = ["Deadline day", "Deadline month", "Deadline year"]

    assgn_details = codecooler_view.get_inputs("Add assignment", questions)
    deadline_details = codecooler_view.get_inputs("Provide deadline", deadline_questions)
    is_empty = is_empty_input(assgn_details)

    if not is_empty:
        try:
            deadline = set_deadline(*deadline_details)
            Assignment.assignments.append(Assignment(*assgn_details, deadline))
            codecooler_view.print_result('Succesfuly added assignment.')
            _create_student_assigments(students, assgn_details[0])
        except ValueError:
            codecooler_view.print_result("Provided deadline is impossible!")

    else:
        codecooler_view.print_error_message('Wrong type of title or description.')

    sleep(2)


def is_empty_input(assgn_details):

    for answer in assgn_details:
        if len(answer) < 1:
            return True

    return False


def _create_student_assigments(students, title):

    for student in students:
        student_assigment = SubmitAssignment(student.idx, "link", title, "date")
        SubmitAssignment.add_assignment(student_assigment)

def set_deadline(d_day, d_month, d_year):
    deadline = date.today()
    deadline = deadline.replace(day=int(d_day), month=int(d_month), year=int(d_year))
    check_date(deadline)

    return deadline

def check_date(deadline):
    if deadline == date.today() or deadline < date.today():
        raise ValueError
