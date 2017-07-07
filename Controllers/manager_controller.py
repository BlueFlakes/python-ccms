from Models.student import Student
from Controllers.instances_manager import InstancesList
from View.codecooler_view import CodecoolerView
from Controllers.mentor_controller import MentorController
from Models.manager import Manager
from Models.mentor import Mentor
from data_manager import DataManager
import os
import sys

class ManagerController:
    user_welcome = None
    main_menu = ['List mentors', 'Edit mentors', 'List Students']
    mentor_edit_menu = ['Add mentor', 'Delete mentor', 'Modify mentor name',
                        'Modify mentor surname', 'Modify mentor password',
                        'Modify mentor email']

    @classmethod
    def start_controller(cls, name, surname, idx):
        cls.user_welcome = "Welcome {} {}".format(name, surname)
        cls.start_main_menu()

    @classmethod
    def start_main_menu(cls):
        user_request = None

        while user_request != "0":
            os.system("clear")
            CodecoolerView.print_menu(cls.user_welcome, cls.main_menu, "Exit")
            user_request = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

            cls.handle_main_menu_requests(user_request)


    @classmethod
    def handle_main_menu_requests(cls, user_request):
        if user_request == '1':
            cls.get_mentors_list()

        elif user_request == '2':
            cls.start_mentor_edit_menu()

        elif user_request == '3':
            cls.get_students_list()

        elif user_request == '0':
            MentorController.save_mentors_data()
            sys.exit()

    @classmethod
    def start_mentor_edit_menu(cls):
        user_request = None

        while user_request != "0":
            os.system("clear")
            CodecoolerView.print_menu(cls.user_welcome, cls.mentor_edit_menu, "Exit")
            user_request = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

            cls.handle_mentor_edit_requests(user_request)

    @classmethod
    def handle_mentor_edit_requests(cls, user_request):
        if user_request == '1':
            MentorController.add_mentor()

        elif user_request == '2':
            MentorController.remove_mentor()

        elif user_request == '3':
            MentorController.change_mentor_name()

        elif user_request == '4':
            MentorController.change_mentor_surname()

        elif user_request == '5':
            MentorController.change_mentor_password()

        elif user_request == '6':
            MentorController.change_mentor_email()

    @classmethod
    def get_mentors_list(cls):
        titles = ["Idx", "Password", "Name", "Surname", "Email"]
        mentors = InstancesList.prepare_data_to_visualize(Mentor.mentor_list)
        CodecoolerView.print_table(titles, mentors)

    @classmethod
    def get_students_list(cls):
        titles = ["Idx", "Password", "Name", "Surname", "Email"]
        students = InstancesList.prepare_data_to_visualize(Student.student_list)
        CodecoolerView.print_table(titles, students)

    @staticmethod
    def load_managers(data):
        Manager.manager_list = InstancesList.convert_data_to_object('manager', data)

    @staticmethod
    def save_managers_data():
        data = InstancesList.prepare_data_to_visualize(Manager.manager_list)
        DataManager.save_file('csv/managers.csv', data)





        #
