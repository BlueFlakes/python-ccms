from View import codecooler_view
from data_manager import DataManager
from Models.assignment import Assignment
from Models.submit_assignment import SubmitAssignment
from Models.grade import Grade
from time import sleep
from prettytable import PrettyTable, ALL
from datetime import date, datetime


def start_controller(position, idx):
    """
    Determines user role in Codecool and call proper function.

    Args:
        position (string): user role in Codecool
        idx (string): uniqe student id
    """

    if position == "student":
        student_side(idx)
    elif position == "mentor":
        mentor_side()


def mentor_side():
    """
    Allow mentor to grade submited assigemts. By call proper functions user see all assigments,
    than user can grade choosen assigments of all students.
    """

    submited_assignments = SubmitAssignment.get_submit_assignments_list()
    user_choice = codecooler_view.get_inputs("Please provide task's name", ["Task"])[0]

    if is_assignment_in_submit_assignments(user_choice, submited_assignments):
        assignment = find_and_return_assignment(user_choice)
        for submitted_task in submited_assignments:

            if user_choice == submitted_task.title:
                codecooler_view.clear_window()

                task_return_delay = days_amount(assignment, submitted_task)
                codecooler_view.print_result("Student idx: {}".format(submitted_task.idx))
                deadline = [assignment.deadline, submitted_task.deadline, task_return_delay]
                codecooler_view.print_result("Task deadline: {} | Task provided date: {}{}".format(*deadline))
                codecooler_view.print_result("Assignment name: {}".format(submitted_task.title))
                codecooler_view.print_result("Link: {}\n".format(submitted_task.link))

                task_grade = _grade_assigement()
                if task_grade != 'no graded assignment':
                    Grade.add_grade(submitted_task.idx, user_choice, task_grade)

    else:
        codecooler_view.print_error_message("Wrong task\'s name!")
        sleep(2)

    codecooler_view.clear_window()


def days_amount(assignment, submitted_assignment):
    time_delay = None
    message = ''

    try:
        deadline = datetime.strptime(str(assignment.deadline), "%Y-%m-%d").date()
        submit_date = datetime.strptime(str(submitted_assignment.deadline), "%Y-%m-%d").date()

        if submit_date > deadline:
            time_delay = (submit_date - deadline).days
            message = ' | Late by ' + str(time_delay) + ' days'

    except ValueError:
        pass

    return message


def find_and_return_assignment(user_choice):
    """
    Return Assigment object of given title

    Args:
        user_choice (string): title of assigment

    Returns:
        :obj: Assigment: assigment of name given by user
    """

    assignments = Assignment.get_assignments_list()

    for assignment in assignments:
        if user_choice == assignment.title:
            return assignment


def is_assignment_in_submit_assignments(provided_key, submited_assignments):
    """
    Validate if assigment is submited by user

    Args:
        provided_key (string): assigment title
        submited_assignments (list of :obj: `SubmitAssignment`): list of all submited assigments

    Returns:
        bool: tell if assignement is submited
    """

    found = False

    for assignment in submited_assignments:
        if provided_key == assignment.title:
            found = True
            break

    return found


def show_assignments(student_assignments):
    """
    Display to user list of all assigments with their status.

    Args:
        existing_assignments (list of :obj: `Assignment`): list of all created assigments
    """

    assignments = [[assign.title, assign.status] for assign in student_assignments]

    title = ['Assignment title', 'Status']
    codecooler_view.print_table(title, assignments)


def find_assignment(user_choice, existing_assignments):
    """
    Validate if user give correcs assigment name.

    Args:
        user_choice (string): assigment name give by user
        existing_assignments (list of :obj: `Assignment`): list of all created assigments

    Returns:
        :obj: `Assignment`: assigment choosen by user
    """

    found_assigment = None

    for assignment in existing_assignments:
        if user_choice.lower() == assignment.title.lower():
            found_assigment = assignment
            break

    if found_assigment is None and user_choice != '0':
        codecooler_view.print_error_message("Wrong assignment name!\n")
        sleep(1.5)

    return found_assigment


def find_belonging_task(idx, submit_assignments, assignment_title):
    """
    Return choosen assigment from submit assgiment list to user

    Args:
        idx (string): unique user's id
        submit_assignments (list of :obj: `SubmitAssignment`): list of assigment to sumbit or submited one
        assignment_title (string): title of assigment

    Returns:
        :obj: `SubmitAssignment`: assigment choosen by user
    """

    found_submit_assignment = None

    for submit_assignment in submit_assignments:
        if idx == submit_assignment.idx and submit_assignment.title == assignment_title:
            found_submit_assignment = submit_assignment

    return found_submit_assignment


def find_all_belonging_tasks(idx, submit_assignments):
    """
    Create list of all submited assigment belong to user of given id

    Args:
        idx (string): uniqe person id
        submit_assignments (list of :obj: `SubmitAssignment`): list of all assigment to sumbit or submited one

    Returns:
        list of :obj: `SubmitAssignment`: assigments belong to person of given id
    """

    temp = []

    for submit_assignment in submit_assignments:
        if idx == submit_assignment.idx:
            temp.append(submit_assignment)

    return temp


def student_side(idx):
    """
    Allows student to submit choosen assignment

    Args:
        idx (string): uniqe student id
    """

    assignments = Assignment.get_assignments_list()

    user_choice = None

    while user_choice != '0':
        codecooler_view.clear_window()
        codecooler_view.print_menu('Assigment management', ['Submit your assignment'], 'Exit')
        user_choice = codecooler_view.get_inputs("", ["Your choice"])[0]

        if user_choice == '1':
            manage_request(idx, assignments)

        elif user_choice == '0':
            pass

        else:
            codecooler_view.print_error_message('No possible action!')
            sleep(1.5)


def manage_request(idx, assignments):
    submit_assignments = SubmitAssignment.get_submit_assignments_list()

    codecooler_view.clear_window()
    show_assignments(find_all_belonging_tasks(idx, submit_assignments))
    user_choice = codecooler_view.get_inputs("", ["Assignment name"])[0]

    found_assigment = find_assignment(user_choice, assignments)

    if found_assigment:
        author_assignment = find_belonging_task(idx, submit_assignments, found_assigment.title)
        assignment_management_controller(found_assigment, author_assignment)


def assignment_management_controller(found_assigment, student_submit_assignment):
    menu = ['Show assignment details', 'Attach link']
    user_choice = None
    prettytable = prepare_prettytable(found_assigment)

    while user_choice != '0':
        codecooler_view.clear_window()
        show_assignments([student_submit_assignment])
        codecooler_view.print_menu('Lets submit Assignment', menu, 'Exit')
        user_choice = codecooler_view.get_inputs("", ["Your choice"])[0]

        if user_choice == '1':
            print(prettytable)
            codecooler_view.state_locker()

        elif user_choice == '2':
            link = codecooler_view.get_inputs('', ['Please provide link'])[0]
            student_submit_assignment.link = link
            student_submit_assignment.status = 'Provided'
            student_submit_assignment.convert_deadline(str(date.today()))

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
