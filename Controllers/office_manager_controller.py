import os
from Controllers.employee_controller import EmployeeController
from View.codecooler_view import CodecoolerView


class OfficeManagerController(EmployeeController):

    @classmethod
    def start_controller(self, name, surname):

        option = 0
        while not option == "0":
            os.system("clear")

            CodecoolerView.print_menu("Welcome {} {}".format(name, surname), ["Show student list"], "Exit")
            options = CodecoolerView.get_inputs("Please choose a number", ["Number"])
            option = options[0]

            if option == "1":
                students = self.get_student_list()
                EmployeeView.print_student_list(students)
