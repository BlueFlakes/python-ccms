import os
from Models.student import Student
from Models.codecooler import Codecooler
from View.student_view import StudentView
from View.codecooler_view import CodecoolerView
from data_manager import DataManager


class StudentController:

    @classmethod
    def start_controller(cls, name, surname, idx):

        option = 0
        while not option == "0":
            os.system("clear")

            CodecoolerView.print_menu("Welcome {} {}".format(name, surname),
                                      ["Submit assignment", "View my grades"], "Exit")
            option = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

            if option == "1":
                cls.submit_assignment()

            elif option == "2":
                cls.view_grades(idx)

    @classmethod
    def submit_assignment(cls):
        pass

    @classmethod
    def view_grades(cls, idx):
        grades = DataManager.read_file("csv/grades.csv")

        print(grades)
        option = CodecoolerView.get_inputs("Enter anything to exit", [""])
