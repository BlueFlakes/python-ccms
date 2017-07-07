import os
from Controllers.instances_manager import InstancesList
from Controllers.student_controller import StudentController
from Controllers.submit_assignment_controller import SubmitAssignmentController
from View.codecooler_view import CodecoolerView
from Models.mentor import Mentor
from Models.student import Student
from Controllers.attendance_controller import AttendanceController
from data_manager import DataManager


class MentorController():

    @classmethod
    def start_controller(cls, name, surname, idx):
        assignments = StudentController.read_assignments("lists")
        students = Student.student_list

        option = 0
        while not option == "0":
            os.system("clear")

            CodecoolerView.print_menu("Welcome {} {}".format(name, surname),
                                      ["Students list", "Add assignment", "Grade assignment",
                                       "Check attendace", "Edit student"], "Exit")
            option = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

            if option == "1":
                titles = ["Idx", "Password", "Name", "Surname", "Email"]
                students = InstancesList.prepare_data_to_visualize(Student.student_list)
                CodecoolerView.print_table(titles, students)

            elif option == "2":
                pass # add assignment
            elif option == "3":
                SubmitAssignmentController.start_controller("mentor", assignments, idx)
            elif option == "4":
                pass # check attendance
            elif option == "5":
                cls.start_student_edit_menu()
            elif option == "0":
                StudentController.save_students_data()


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

    @classmethod
    def start_student_edit_menu(cls):
        user_request = None
        user_welcome = "Student edit manager"
        student_edit_menu = ['Add student', 'Delete student', 'Modify student name',
                            'Modify student surname', 'Modify student password',
                            'Modify student email']

        while user_request != "0":
            os.system("clear")
            CodecoolerView.print_menu(user_welcome, student_edit_menu, "Exit")
            user_request = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

            cls.handle_student_edit_requests(user_request)

    @classmethod
    def handle_student_edit_requests(cls, user_request):
        if user_request == '1':
            StudentController.add_student()

        elif user_request == '2':
            StudentController.remove_student()

        elif user_request == '3':
            StudentController.change_student_name()

        elif user_request == '4':
            StudentController.change_student_surname()

        elif user_request == '5':
            StudentController.change_student_password()

        elif user_request == '6':
            StudentController.change_student_email()

    @classmethod
    def get_students_list(cls):
        students = DataManager.read_file("csv/students.csv")
        titles = ["Idx", "Password", "Name", "Surname", "Email"]
        CodecoolerView.print_table(titles, students)


    @staticmethod
    def load_mentors(data):
        Mentor.mentor_list = InstancesList.convert_data_to_object('mentor', data)

    @staticmethod
    def save_mentors_data():
        data = InstancesList.prepare_data_to_visualize(Mentor.mentor_list)
        DataManager.save_file('csv/mentors.csv', data)
