from Models.student import Student
from Models.codecooler import Codecooler
from View.student_view import StudentView
from View.codecooler_view import CodecoolerView


class StudentController:

    @classmethod
    def start_controller(cls, name, surname):

        CodecoolerView.print_menu("Welcome {} {}".format(name, surname),
                                  ["Submit assignment", "View my grades"], "Exit")

        option = 0
        while not option == "0":
            options = CodecoolerView.get_inputs("Please choose a number", [""])
            option = options[0]

            if option == "1":
                self.submit_assignment()
            elif option == "2":
                self.view_grades(name, surname)

    def submit_assignment(self):
        pass

    def view_grades(self, name, surname):
        pass
