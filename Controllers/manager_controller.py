from Models.student import Student
from View.codecooler_view import CodecoolerView
from Controllers.mentor_controller import MentorController
import os
import sys


class ManagerController:
    """
    Contain logic for OfficeManagerController

    Attributes:
        user_welcome (None): further change to string greeting actual user.
        main_menu (list of strings): list of user's available options
        mentor_edit_menu (list of strings): list of user's available options in inner menu
    """

    user_welcome = None
    main_menu = ['List mentors', 'Edit mentors', 'List Students']
    mentor_edit_menu = ['Add mentor', 'Delete mentor', 'Modify mentor name',
                        'Modify mentor surname', 'Modify mentor password',
                        'Modify mentor email']

    @classmethod
    def start_controller(cls, name, surname, idx):
        """
        Allow manager user perform assign tasks

        Args:
            name (string): name of user
            surname (string): surname of user
            idx (string): unique user's id
        """
        cls.user_welcome = "Welcome {} {}".format(name, surname)
        cls.start_main_menu()

    @classmethod
    def start_main_menu(cls):
        """
        Call functions that get user input and show menu
        """

        user_request = None

        while user_request != "0":
            os.system("clear")
            CodecoolerView.print_menu(cls.user_welcome, cls.main_menu, "Exit")
            user_request = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

            cls.handle_main_menu_requests(user_request)

    @classmethod
    def handle_main_menu_requests(cls, user_request):
        """
        Call function that perform task from menu choosen by user

        Args:
            user_request (string): option choosen by user
        """
        if user_request == '1':
            # Mentors list
            pass

        elif user_request == '2':
            cls.start_mentor_edit_menu()

        elif user_request == '3':
            # List students
            pass

        elif user_request == '0':
            sys.exit()

    @classmethod
    def start_mentor_edit_menu(cls):
        """Call functions that get user input and show inner menu"""

        user_request = None

        while user_request != "0":
            os.system("clear")
            CodecoolerView.print_menu(cls.user_welcome, cls.mentor_edit_menu, "Exit")
            user_request = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

            cls.handle_mentor_edit_requests(user_request)

    @classmethod
    def handle_mentor_edit_requests(cls, user_request):
        """
        Call function that perform task from inner menu choosen by user

        Args:
            user_request (string): option choosen by user
        """

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
