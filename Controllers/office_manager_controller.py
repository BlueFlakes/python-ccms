import os
from View.codecooler_view import CodecoolerView
from data_manager import DataManager


class OfficeManagerController:
    """Contain logic for OfficeManagerController"""

    @classmethod
    def start_controller(self, name, surname):
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

            CodecoolerView.print_menu("Welcome {} {}".format(name, surname), ["Show student list"], "Exit")
            options = CodecoolerView.get_inputs("Please choose a number", ["Number"])
            option = options[0]

            if option == "1":
                students = DataManager.read_file("csv/students.csv")
                titles = ["Idx", "Password", "Name", "Surname", "Email"]
                CodecoolerView.print_table(titles, students)
