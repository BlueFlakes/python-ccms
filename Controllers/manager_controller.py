from Models.student import Student
from Models.manager import Manager
from Models.mentor import Mentor
from Controllers import instances_manager, talkbox
from Controllers import student_controller, mentor_controller, codecooler_controller
from View import codecooler_view
from data_manager import DataManager
import sys


def start_controller(name, surname, idx):
    """
    Call functions that get user input and show menu

    Args:
        name (string): name of user
        surname (string): surname of user
        idx (string): unique user's id
    """

    user_welcome = "Welcome {} {}".format(name, surname)
    main_menu = ['List mentors', 'Edit mentors', 'List Students', "Students ranking",
                 'Change your password', "Enter talkbox"]
    user_request = None

    while user_request != "0":
        codecooler_view.print_menu(user_welcome, main_menu, "Exit")
        user_request = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]

        handle_main_menu_requests(user_request, idx, name, surname)


def handle_main_menu_requests(user_request, idx, name, surname):
    """
    Call function that perform task from menu choosen by user: see list of students, mentors,
    edit mentors

    Args:
        user_request (string): option choosen by user
    """
    if user_request == '1':
        get_mentors_list()

    elif user_request == '2':
        start_mentor_edit_menu()

    elif user_request == '3':
        get_students_list()

    elif user_request == "4":
        rank = student_controller.get_ranking()
        codecooler_view.print_table(["Name", "Total points" ], rank)
        codecooler_view.state_locker()
        codecooler_view.clear_window()

    elif user_request == '5':
        codecooler_controller.change_password(idx)

    elif user_request == "6":
        talkbox.start_talkbox(name, surname)


def start_mentor_edit_menu():
    """
    Call functions that get user input and show inner menu
    """
    mentor_edit_menu = ['Add mentor', 'Delete mentor', 'Modify mentor name',
                        'Modify mentor surname', 'Modify mentor password',
                        'Modify mentor email']
    user_welcome = "Mentors edit manager"
    user_request = None

    while user_request != "0":
        get_mentors_list()
        codecooler_view.print_menu(user_welcome, mentor_edit_menu, "Exit")
        user_request = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]

        handle_mentor_edit_requests(user_request)

    codecooler_view.clear_window()

def handle_mentor_edit_requests(user_request):
    """
    Call function that perform task from inner menu choosen by user: add mentor, remove mentor,
    chenge mentros details

    Args:
        user_request (string): option choosen by user
    """

    if user_request == '1':
        mentor_controller.add_mentor()

    elif user_request == '2':
        mentor_controller.remove_mentor()

    elif user_request == '3':
        mentor_controller.change_mentor_name()

    elif user_request == '4':
        mentor_controller.change_mentor_surname()

    elif user_request == '5':
        mentor_controller.change_mentor_password()

    elif user_request == '6':
        mentor_controller.change_mentor_email()


def get_mentors_list():
    """
    Call functions to display formatted table with all Mentor objects details
    """
    titles = ["Idx", "Password", "Name", "Surname", "Email"]
    mentors = instances_manager.prepare_data_to_visualize(Mentor.mentor_list)
    codecooler_view.print_table(titles, mentors)


def get_students_list():
    """
    Call functions to display formatted table with Student object details
    """
    titles = ["Idx", "Password", "Name", "Surname", "Email"]
    students = instances_manager.prepare_data_to_visualize(Student.student_list)
    codecooler_view.print_table(titles, students)
    get_students_grades()


def get_students_grades():
    """
    Call functions to display detail about choosen student grades
    """
    check_grades = codecooler_view.get_inputs("Do you want to see grades of any student?",
                                             ["Yes/no"])
    check_grades = check_grades[0].lower()
    if check_grades == "yes":
        idx = codecooler_view.get_inputs("Please provide idx of the student", ["Idx"])[0]
        student_controller.view_grades(idx)
    else:
        codecooler_view.clear_window()
