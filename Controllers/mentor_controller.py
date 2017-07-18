import os
from Controllers import instances_manager
from Controllers import student_controller
from Controllers import submit_assignment_controller
from Controllers import assignment_controller
from Controllers import attendance_controller
from View import codecooler_view
from Models.mentor import Mentor
from Models.student import Student
from data_manager import DataManager


def start_controller(name, surname, idx):
    """
    Allow mentor user perform assign tasks.
    Call functions to print menu for user and get input of choosen option

    Args:
        name (string): name of user
        surname (string): surname of user
        idx (string): unique user's id
    """

    assignments = student_controller.read_assignments("lists")
    students = Student.student_list

    option = 0
    while not option == "0":
        os.system("clear")

        codecooler_view.print_menu("Welcome {} {}".format(name, surname),
                                  ["Students list", "Add assignment", "Grade assignment",
                                   "Check attendace", "Edit student"], "Exit")
        option = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]

        if option == "1":
            display_student_list(students)
            get_students_grades()

        elif option == "2":
            assignment_controller.start_controller()
        elif option == "3":
            submit_assignment_controller.start_controller("mentor", assignments, idx)
        elif option == "4":
            attendance_controller.start_controller()
        elif option == "5":
            start_student_edit_menu(students)
        elif option == "0":
            student_controller.save_students_data()


def add_mentor():
    """
    Create Mentor object and add to mentor_list
    """

    title = 'Creating mentor'
    instances_manager.add_person(Mentor.mentor_list, Mentor, title)


def remove_mentor():
    """
    Remove Mentor object from mentor_list
    """

    instances_manager.remove_person(Mentor.mentor_list)


def change_mentor_name():
    """
    Change mentor name
    """

    title = 'Modify name'
    task = ['Provide new name']
    instances_manager.modify_person_details(Mentor.mentor_list, 'name', title, task)


def change_mentor_password():
    """
    Change mentor password
    """

    title = 'Modify password'
    task = ['Provide new password']
    instances_manager.modify_person_details(Mentor.mentor_list, 'password', title, task)


def change_mentor_surname():
    """
    Change mentor surname
    """

    title = 'Modify surname'
    task = ['Provide new surname']
    instances_manager.modify_person_details(Mentor.mentor_list, 'surname', title, task)


def change_mentor_email():
    """
    Change mentor email
    """

    title = 'Modify email'
    task = ['Email']
    instances_manager.modify_person_details(Mentor.mentor_list, 'email', title, task)


def start_student_edit_menu(students):
    """
    Call functions that get user input and show inner menu

    Args:
        students (list of :obj: Student): list of all students
    """

    user_request = None
    user_welcome = "Student edit manager"
    student_edit_menu = ['Add student', 'Delete student', 'Modify student name',
                         'Modify student surname', 'Modify student password',
                         'Modify student email']

    while user_request != "0":
        os.system("clear")

        display_student_list(students)

        codecooler_view.print_menu(user_welcome, student_edit_menu, "Exit")
        user_request = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]

        handle_student_edit_requests(user_request)


def handle_student_edit_requests(user_request):
    """
    Call function that perform task from inner menu choosen by user: add student, remove student,
    change details about student

    Args:
        user_request (string): option from menu choosen by user
    """

    if user_request == '1':
        student_controller.add_student()

    elif user_request == '2':
        student_controller.remove_student()

    elif user_request == '3':
        student_controller.change_student_name()

    elif user_request == '4':
        student_controller.change_student_surname()

    elif user_request == '5':
        student_controller.change_student_password()

    elif user_request == '6':
        student_controller.change_student_email()


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


def load_mentors(data):
    """
    Call function to convet data from csv file to Mentor objects

    Args:
        data (lista of list): data to convert from csv file
    """
    Mentor.mentor_list = instances_manager.convert_data_to_object('mentor', data)


def save_mentors_data():
    """
    Call function to save data in csv file
    """
    data = instances_manager.prepare_data_to_visualize(Mentor.mentor_list)
    DataManager.save_file('csv/mentors.csv', data)


def display_student_list(students):
    """
    Call functions to display formatted table with all students

    Args:
        students (list of :obj: Student): list of all students
    """
    titles = ["Idx", "Password", "Name", "Surname", "Email"]
    students = instances_manager.prepare_data_to_visualize(students)
    codecooler_view.print_table(titles, students)
