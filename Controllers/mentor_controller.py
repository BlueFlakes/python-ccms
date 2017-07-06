import os
from Controllers.instances_manager import InstancesList
from Controllers.student_controller import StudentController
from Controllers.submit_assignment_controller import SubmitAssignmentController
from View.codecooler_view import CodecoolerView
from Models.mentor import Mentor
from Models.student import Student
from Controllers.attendance_controller import AttendanceController
from data_manager import DataManager


class MentorController():
    """Contain logic for MentorController"""

    @classmethod
    def start_controller(cls, name, surname, idx):
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
                cls.get_students_list()
            elif option == "2":
                pass     # add assignment
            elif option == "3":
                SubmitAssignmentController.start_controller("mentor", assignments, idx)
            elif option == "4":
                pass    # check attendance
            elif option == "5":
                cls.start_student_edit_menu()

    @staticmethod
    def add_mentor():
        """
        Create Mentor object and add to mentor_list
        """

        title = 'Creating mentor'
        basic_questions = ['password', 'Name', 'Surname', 'email']

        InstancesList.add_person(Mentor.mentor_list, Mentor, title, basic_questions)

    @staticmethod
    def remove_mentor():
        """
        Remove Mentor object from mentor_list
        """

        InstancesList.remove_person(Mentor.mentor_list)

    @staticmethod
    def change_mentor_name():
        """
        Change mentor name
        """

        title = 'Modify name'
        task = ['Provide new name']
        InstancesList.modify_person_details(Mentor.mentor_list, 'name', title, task)

    @staticmethod
    def change_mentor_password():
        """
        Change mentor password
        """

        title = 'Modify password'
        task = ['Provide new password']
        InstancesList.modify_person_details(Mentor.mentor_list, 'password', title, task)

    @staticmethod
    def change_mentor_surname():
        """
        Change mentor surname
        """

        title = 'Modify surname'
        task = ['Provide new surname']
        InstancesList.modify_person_details(Mentor.mentor_list, 'surname', title, task)

    @staticmethod
    def change_mentor_email():
        """
        Change mentor email
        """

        title = 'Modify email'
        task = ['Provide new email']
        InstancesList.modify_person_details(Mentor.mentor_list, 'email', title, task)

    @classmethod
    def start_student_edit_menu(cls):
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

    @classmethod
    def handle_student_edit_requests(cls, user_request):
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

    @classmethod
    def get_students_list(cls):
        students = DataManager.read_file("csv/students.csv")
        titles = ["Idx", "Password", "Name", "Surname", "Email"]
        CodecoolerView.print_table(titles, students)
