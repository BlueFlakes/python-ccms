import os
from View.codecooler_view import CodecoolerView
from data_manager import DataManager


class OfficeManagerController:

    @classmethod
    def start_controller(self, name, surname):

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
