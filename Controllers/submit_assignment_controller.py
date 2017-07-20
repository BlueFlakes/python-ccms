from View import codecooler_view
from data_manager import DataManager
from Models.assignment import Assignment
from Models.submit_assignment import SubmitAssignment
from Models.grade import Grade
from time import sleep
from prettytable import PrettyTable, ALL


def start_controller(position, idx):
    """
    Determines user role in Codecool. Allow user perform assign tasks.

    Args:
        position (string): user role in Codecool
        assignments (list of :obj: `SubmitAssignment`): list of assigemts
        idx (string): uniqe student id
    """
    if position == "student":
        student_side(idx)
    elif position == "mentor":
        mentor_side()


def mentor_side():
    """
    Allow mentor to grade submited assigemts. Then list of assigemts is save to csv file.

    Args:
        submited_assignments (list of :obj: `SubmitAssignment`): list of assigemts
    """
    submited_assignments = SubmitAssignment.get_submit_assignments_list()
    user_choice = codecooler_view.get_inputs("Please provide task's name", ["Task"])[0]

    for submitted_task in submited_assignments:
        if user_choice == submitted_task.name:
            codecooler_view.clear_window()
            codecooler_view.print_result("Student idx: {} | Date: {}".format(submitted_task.idx, submitted_task.date))
            codecooler_view.print_result("Assignment name: {}".format(submitted_task.name))
            codecooler_view.print_result("Link: {}\n".format(submitted_task.link))

            task_grade = _grade_assigement()
            if task_grade != 'no graded assignment':
                Grade.add_grade(submitted_task.idx, user_choice, task_grade)
            break
    else:
        codecooler_view.print_error_message("Wrong task\'s name!")
        sleep(2)

    codecooler_view.clear_window()


def show_assignments(existing_assignments):
    assignments = [[assign.title, assign.status] for assign in existing_assignments]
    title = ['Assignment title', 'Status']
    codecooler_view.print_table(title, assignments)


def find_assignment(user_choice, existing_assignments):
    found_assigment = None

    for assignment in existing_assignments:
        if user_choice == assignment.title:
            found_assigment = assignment
            break

    if found_assigment is None and user_choice != '0':
        codecooler_view.print_error_message("Wrong assignment name!\n")
        sleep(1.5)

    return found_assigment


def find_belonging_task(idx, submit_assignments, assignment_title):
    found_submit_assignment = None

    for submit_assignment in submit_assignments:
        if idx == submit_assignment.idx and submit_assignment.name == assignment_title:
            found_submit_assignment = submit_assignment

    return found_submit_assignment


def student_side(idx):
    """
    Allows student to submit assignment

    Args:
        idx (string): uniqe student id
    """
    existing_assignments = Assignment.get_assignments_list()
    user_choice = None

    while user_choice != '0':
        codecooler_view.clear_window()
        codecooler_view.print_menu('Assigment management', ['Submit your assignment'], 'Exit')
        user_choice = codecooler_view.get_inputs("", ["Your choice"])[0]

        if user_choice == '1':
            manage_request(idx, existing_assignments)

        elif user_choice == '0':
            pass

        else:
            codecooler_view.print_error_message('No possible action!')
            sleep(1.5)


def manage_request(idx, existing_assignments):
    submit_assignments = SubmitAssignment.get_submit_assignments_list()
    codecooler_view.clear_window()
    show_assignments(existing_assignments)
    user_choice = codecooler_view.get_inputs("", ["Assignment name"])[0]

    found_assigment = find_assignment(user_choice, existing_assignments)

    if found_assigment:
        author_assignment = find_belonging_task(idx, submit_assignments, found_assigment.title)
        assignment_management_controller(found_assigment, author_assignment)


def assignment_management_controller(found_assigment, student_submit_assignment):
    menu = ['Show assignment details', 'Attach link']
    user_choice = None
    prettytable = prepare_prettytable(found_assigment)

    while user_choice != '0':
        codecooler_view.clear_window()
        show_assignments([found_assigment])
        codecooler_view.print_menu('Lets submit Assignment', menu, 'Exit')
        user_choice = codecooler_view.get_inputs("", ["Your choice"])[0]

        if user_choice == '1':
            print(prettytable)
            codecooler_view.state_locker()

        elif user_choice == '2':
            # attach link and deadline

        elif user_choice == '0':
            pass

        else:
            codecooler_view.print_error_message('No possible action!')
            sleep(1.5)

def prepare_prettytable(found_assigment):
    prettytable = PrettyTable(hrules=ALL)
    table_data = [['Title', found_assigment.title], ['Description', found_assigment.description],
                  ['Deadline', found_assigment.deadline]]

    for record in table_data:
        prettytable.add_row(record)

    return prettytable

def _grade_assigement():
    """
    Allow mentor to eval student's assigment by Danish scale. Show menu with grades assigne to menu options
    """

    grade = 0
    eval_categories = ["Stability", "Conform to requirements", "Python basics", "Git workflow", "Teamwork"]
    possible_eval_options = ["12.0 pts", "10.0 pts", "7.0 pts", "4.0 pts", "2.0 pts", "0.0 pts", "-1.0 pts", "-3.0 pts"]

    for category in eval_categories:
        user_choice = None

        while user_choice not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            codecooler_view.print_menu(category, possible_eval_options, "Exit evaluation for student")
            user_choice = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]
            grades_scale = {'1': 12, '2': 10, '3': 7, '4': 4, '5': 2, '6': 0, '7': -1, '8': -3}

            if user_choice in grades_scale:
                grade += grades_scale[user_choice]

            else:
                codecooler_view.print_error_message('Wrong choice!')

        if user_choice == "0":
            grade = 'no graded assignment'
            break

    return grade
