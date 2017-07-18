from Models.student import Student
from Models.office_manager import OfficeManager
from Controllers import instances_manager
from View import codecooler_view
from data_manager import DataManager
import os

def start_controller(name, surname):
    """
    Allow office manager user perform assign tasks.
    Call functions to print menu for user and get input of choosen option: show students list

    Args:
        name (string): name of user
        surname (string): surname of user
    """

    option = 0
    while not option == "0":
        os.system("clear")

        codecooler_view.print_menu("Welcome {} {}".format(name, surname), ["Show student list"], "Exit")
        options = codecooler_view.get_inputs("Please choose a number", ["Number"])
        option = options[0]

        if option == "1":
            titles = ["Idx", "Password", "Name", "Surname", "Email"]
            students = InstancesList.prepare_data_to_visualize(Student.student_list)
            codecooler_view.print_table(titles, students)

def load_office_managers(data):
    OfficeManager.office_managers_list = instances_manager.convert_data_to_object('officemanager', data)
