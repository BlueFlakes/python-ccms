from Models.student import Student
from Controllers.instances_manager import InstancesList
from Models.office_manager import OfficeManager
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
                titles = ["Idx", "Password", "Name", "Surname", "Email"]
                students = InstancesList.prepare_data_to_visualize(Student.student_list)
                CodecoolerView.print_table(titles, students)

    @staticmethod
    def load_office_managers(data):
        OfficeManager.office_managers_list = InstancesList.convert_data_to_object('officemanager', data)
