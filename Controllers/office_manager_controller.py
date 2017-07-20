from Models.student import Student
from Models.office_manager import OfficeManager
from Controllers import instances_manager, codecooler_controller, student_controller, talkbox
from View import codecooler_view
from data_manager import DataManager

def start_controller(name, surname, idx):
    """
    Allow office manager user perform assign tasks.
    Call functions to print menu for user and get input of choosen user_choice: show students list

    Args:
        name (string): name of user
        surname (string): surname of user
    """
    user_choice = None

    while user_choice != "0":

        codecooler_view.print_menu("Welcome {} {}".format(name, surname),
                                   ["Show student list", "Students ranking", "Change your password",
                                    "Enter talkbox"], "Exit")
        user_choices = codecooler_view.get_inputs("Please choose a number", ["Number"])
        user_choice = user_choices[0]

        if user_choice == "1":
            titles = ["Idx", "Password", "Name", "Surname", "Email"]
            students = instances_manager.prepare_data_to_visualize(Student.student_list)
            codecooler_view.print_table(titles, students)

        elif user_choice == "2":
            rank = student_controller.get_ranking()
            codecooler_view.print_table(["Name", "Total points" ], rank)
            codecooler_view.state_locker()
            codecooler_view.clear_window()

        elif user_choice == "3":
            codecooler_controller.change_password(idx)

        elif user_choice == "4":
            talkbox.start_talkbox(name, surname)
