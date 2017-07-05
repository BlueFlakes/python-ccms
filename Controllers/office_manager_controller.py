from Controllers.employee_controller import EmployeeController
from View.employee_view import EmployeeView


class OfficeEmployeeController(EmployeeController):
    def start_controller():

        CodecoolerView.print_menu("Welcome {} {}", ["Show studen list"], "Exit")

        choice = None
        while choice != "0":
            students = self.get_student_list()
            print_menu()
            choice = get_choice()

            if choice == "1":
                print_student_list(students)
