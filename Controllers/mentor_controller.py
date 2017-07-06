from Controllers.instances_manager import InstancesList
from Models.mentor import Mentor

class MentorController():

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

    @staticmethod
    def add_mentor():
        title = 'Creating mentor'
        basic_questions = ['password', 'Name', 'Surname', 'email']

        InstancesList.add_person(Mentor.mentor_list, Mentor, title, basic_questions)

    @staticmethod
    def remove_mentor():
        InstancesList.remove_person(Mentor.mentor_list)

    @staticmethod
    def change_mentor_name():
        title = 'Modify name'
        task = ['Provide new name']
        InstancesList.modify_person_details(Mentor.mentor_list, 'name', title, task)

    @staticmethod
    def change_mentor_password():
        title = 'Modify password'
        task = ['Provide new password']
        InstancesList.modify_person_details(Mentor.mentor_list, 'password', title, task)

    @staticmethod
    def change_mentor_surname():
        title = 'Modify surname'
        task = ['Provide new surname']
        InstancesList.modify_person_details(Mentor.mentor_list, 'surname', title, task)

    @staticmethod
    def change_mentor_email():
        title = 'Modify email'
        task = ['Provide new email']
        InstancesList.modify_person_details(Mentor.mentor_list, 'email', title, task)
