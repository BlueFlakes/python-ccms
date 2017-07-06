import os
from Models.student import Student
from Models.codecooler import Codecooler
from Models.submit_assignment import SubmitAssignment
from View.codecooler_view import CodecoolerView
from Controllers.submit_assignment_controller import SubmitAssignmentController
from Controllers.instances_manager import InstancesList
from data_manager import DataManager


class StudentController:

    @classmethod
    def start_controller(cls, name, surname, idx):
        assignments = cls.read_assignments("objects")

        option = 0
        while not option == "0":
            os.system("clear")

            CodecoolerView.print_menu("Welcome {} {}".format(name, surname),
                                      ["Submit assignment", "View my grades"], "Exit")
            option = CodecoolerView.get_inputs("Please choose a number", ["Number"])[0]

            if option == "1":
                SubmitAssignmentController.start_controller("student", assignments, idx)
            elif option == "2":
                cls.view_grades(idx)

        cls.save_assignments(assignments)

    @classmethod
    def view_grades(cls, idx):
        students_grades = []
        all_grades = DataManager.read_file("csv/grades.csv")

        for grade in all_grades:
            if idx in grade[0]:
                students_grades.append(grade)

        if len(students_grades) > 0:
            titles = ["Students idx", "Assignment", "Grade"]
            CodecoolerView.print_table(titles, students_grades)
        else:
            CodecoolerView.print_result("There is no grades!")
            option = CodecoolerView.get_inputs("Enter anything to exit", [""])


    @staticmethod
    def read_assignments(return_type):
        assignments_list = DataManager.read_file("csv/submitted_assgn.csv")
        assignments = SubmitAssignment.assignments

        for i in range(len(assignments_list)):

            to_append = SubmitAssignment(assignments_list[i][0], assignments_list[i][1],
                                         assignments_list[i][2], assignments_list[i][3])
            assignments.append(to_append)

        if return_type == "objects":
            return assignments
        elif return_type == "lists":
            return assignments_list

    @staticmethod
    def save_assignments(assignments):
        for i in range(len(assignments)):
            assignments[i] = [assignments[i].idx, assignments[i].link,
                              assignments[i].name, assignments[i].date]

        DataManager.save_file("csv/submitted_assgn.csv", assignments)

    @staticmethod
    def remove_student():
        InstancesList.remove_person(Student.student_list)

    @staticmethod
    def add_student():
        title = 'Creating student'
        basic_questions = ['password', 'Name', 'Surname', 'email']

        InstancesList.add_person(Student.student_list, Student, title, basic_questions)

    @staticmethod
    def change_student_name():
        title = 'Modify name'
        task = ['Provide new name']
        InstancesList.modify_person_details(Student.student_list, 'name', title, task)

    @staticmethod
    def change_student_password():
        title = 'Modify password'
        task = ['Provide new password']
        InstancesList.modify_person_details(Student.student_list, 'password', title, task)

    @staticmethod
    def change_student_surname():
        title = 'Modify surname'
        task = ['Provide new surname']
        InstancesList.modify_person_details(Student.student_list, 'surname', title, task)

    @staticmethod
    def change_student_email():
        title = 'Modify email'
        task = ['Provide new email']
        InstancesList.modify_person_details(Student.student_list, 'email', title, task)
