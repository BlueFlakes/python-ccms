from Models.student import Student
from Models.office_manager import OfficeManager
from Controllers import instances_manager, codecooler_controller, talkbox
from View import codecooler_view
from data_manager import DataManager

def start_controller(name, surname, idx):
    """
    Allow office manager user perform assign tasks.
    Call functions to print menu for user and get input of choosen option: show students list

    Args:
        name (string): name of user
        surname (string): surname of user
    """

    option = 0
    while not option == "0":

        codecooler_view.print_menu("Welcome {} {}".format(name, surname),
                                   ["Show student list", "Change your password",
                                    "Enter talkbox"], "Exit")
        options = codecooler_view.get_inputs("Please choose a number", ["Number"])
        option = options[0]

        if option == "1":
            titles = ["Idx", "Password", "Name", "Surname", "Email"]
            students = instances_manager.prepare_data_to_visualize(Student.student_list)
            codecooler_view.print_table(titles, students)
        elif option == "2":
            codecooler_controller.change_password(idx)
        elif option == "3":
            talkbox.start_talkbox(name, surname)

    save_office_managers()

def load_office_managers(data):
    OfficeManager.office_managers_list = instances_manager.convert_data_to_object('officemanager', data)

def save_office_managers():
    data = instances_manager.prepare_data_to_visualize(OfficeManager.office_managers_list)
    DataManager.save_file('csv/officemanagers.csv', data)
