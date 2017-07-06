import os
from Models.student import Student
from Models.codecooler import Codecooler
from Models.submit_assignment import SubmitAssignment
from View.codecooler_view import CodecoolerView
from Controllers.submit_assignment_controller import SubmitAssignmentController
from data_manager import DataManager


class StudentController:

    @classmethod
    def start_controller(cls, name, surname, idx):
        assignments = cls.read_assignments()

        option = 0
        while not option == "0":
            os.system("clear")

            CodecoolerView.print_menu("Welcome {} {}".format(name, surname),
                                      ["Submit assignment", "View my grades"], "Exit")
            option = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

            if option == "1":
                SubmitAssignmentController.start_controller("student", assignments)
            elif option == "2":
                cls.view_grades(idx)

        cls.save_assignments(assignments)

    @classmethod
    def view_grades(cls, idx):
        grades = DataManager.read_file("csv/grades.csv")

        print(grades)
        option = CodecoolerView.get_inputs("Enter anything to exit", [""])

    @staticmethod
    def read_assignments():
        assignments_list = DataManager.read_file("csv/submitted_assgn.csv")
        assignments = SubmitAssignment.assignments

        for i in range(len(assignments_list)):

            to_append = SubmitAssignment(assignments_list[i][0], assignments_list[i][1],
                                         assignments_list[i][2], assignments_list[i][3])
            assignments.append(to_append)

        return assignments

    @staticmethod
    def save_assignments(assignments):
        print(assignments)
        for i in range(len(assignments)):
            assignments[i] = [assignments[i].idx, assignments[i].link,
                              assignments[i].name, assignments[i].date]

        DataManager.save_file("csv/submitted_assgn.csv", assignments)
