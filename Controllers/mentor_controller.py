from Controllers.employee_controller import EmployeerCotroller
from Controllers.instances_manager import InstancesList


class MentorController(EmployeerCotroller):

    def start_controller():

        choice = None
        while choice != "0":
            students = self.get_student_list()
            print_menu()
            choice = get_choice()

            if choice == "1":
                person = Student()
                InstancesList.add_person(students, person)

            elif choice == "2":
                InstancesList.remove_person(students, self.login)
