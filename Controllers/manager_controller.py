from Models.mentor import Mentor
from Controllers.instances_manager import InstancesList


class ManagerController:
    def start_controller():

        choice = None
        while choice != "0":
            mentors = Mentor.mentor_list
            print_menu()
            choice = get_choice()

            if choice == "1":
                person = Mentor()
                InstancesList.add_person(mentors, person)

            elif choice == "2":
                InstancesList.remove_person(mentors, self.login)
