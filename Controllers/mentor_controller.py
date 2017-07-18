import os
from Controllers.instances_manager import InstancesList
from Controllers.student_controller import StudentController
from Controllers.submit_assignment_controller import SubmitAssignmentController
from Controllers.assignment_controller import AssignmentController
from View.codecooler_view import CodecoolerView
from Models.mentor import Mentor
from Models.student import Student
from Controllers.attendance_controller import AttendanceController
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

    assignments = StudentController.read_assignments("lists")
    students = Student.student_list

    option = 0
    while not option == "0":
        os.system("clear")

        CodecoolerView.print_menu("Welcome {} {}".format(name, surname),
                                  ["Students list", "Add assignment", "Grade assignment",
                                   "Check attendace", "Edit student"], "Exit")
        option = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

        if option == "1":
            titles = ["Idx", "Password", "Name", "Surname", "Email"]
            students = InstancesList.prepare_data_to_visualize(Student.student_list)
            CodecoolerView.print_table(titles, students)
            cls.get_students_grades()

        elif option == "2":
            AssignmentController.start_controller()
        elif option == "3":
            SubmitAssignmentController.start_controller("mentor", assignments, idx)
        elif option == "4":
            AttendanceController.start_controller()
        elif option == "5":
            cls.start_student_edit_menu()
        elif option == "0":
            StudentController.save_students_data()


def add_mentor():
    """
    Create Mentor object and add to mentor_list
    """

    title = 'Creating mentor'
    basic_questions = ['password', 'Name', 'Surname', 'email']

    InstancesList.add_person(Mentor.mentor_list, Mentor, title, basic_questions)


def remove_mentor():
    """
    Remove Mentor object from mentor_list
    """

    InstancesList.remove_person(Mentor.mentor_list)


def change_mentor_name():
    """
    Change mentor name
    """

    title = 'Modify name'
    task = ['Provide new name']
    InstancesList.modify_person_details(Mentor.mentor_list, 'name', title, task)


def change_mentor_password():
    """
    Change mentor password
    """

    title = 'Modify password'
    task = ['Provide new password']
    InstancesList.modify_person_details(Mentor.mentor_list, 'password', title, task)


def change_mentor_surname():
    """
    Change mentor surname
    """

    title = 'Modify surname'
    task = ['Provide new surname']
    InstancesList.modify_person_details(Mentor.mentor_list, 'surname', title, task)


def change_mentor_email():
    """
    Change mentor email
    """

    title = 'Modify email'
    task = ['Email']
    InstancesList.modify_person_details(Mentor.mentor_list, 'email', title, task)


def start_student_edit_menu():
    """
    Call functions that get user input and show inner menu
    """

    user_request = None
    user_welcome = "Student edit manager"
    student_edit_menu = ['Add student', 'Delete student', 'Modify student name',
                         'Modify student surname', 'Modify student password',
                         'Modify student email']

    while user_request != "0":
        os.system("clear")
        CodecoolerView.print_menu(user_welcome, student_edit_menu, "Exit")
        user_request = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

        cls.handle_student_edit_requests(user_request)


def handle_student_edit_requests(user_request):
    """
    Call function that perform task from inner menu choosen by user: add student, remove student,
    change details about student
    """

    if user_request == '1':
        StudentController.add_student()

    elif user_request == '2':
        StudentController.remove_student()

    elif user_request == '3':
        StudentController.change_student_name()

    elif user_request == '4':
        StudentController.change_student_surname()

    elif user_request == '5':
        StudentController.change_student_password()

    elif user_request == '6':
        StudentController.change_student_email()


def get_students_grades():
    check_grades = CodecoolerView.get_inputs("Do you want to see grades of any student?",
                                             ["Yes/no"])
    check_grades = check_grades[0].lower()
    if check_grades == "yes":
        idx = CodecoolerView.get_inputs("Please provide idx of the student", ["Idx"])[0]
        StudentController.view_grades(idx)


def load_mentors(data):
    Mentor.mentor_list = InstancesList.convert_data_to_object('mentor', data)


def save_mentors_data():
    data = InstancesList.prepare_data_to_visualize(Mentor.mentor_list)
    DataManager.save_file('csv/mentors.csv', data)
