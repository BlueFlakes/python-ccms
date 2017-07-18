import os
from Models.student import Student
from Models.codecooler import Codecooler
from Models.submit_assignment import SubmitAssignment
from Controllers import submit_assignment_controller
from Controllers import instances_manager
from Controllers import codecooler_controller
from View import codecooler_view
from data_manager import DataManager


def start_controller(name, surname, idx):
    """
    Allow student user perform assign tasks.
    Call functions to print menu for user and get input of choosen option

    Args:
        name (string): name of user
        surname (string): surname of user
        idx (string): unique user's id
    """

    assignments = read_assignments("objects")

    option = 0
    while not option == "0":
        os.system("clear")

        codecooler_view.print_menu("Welcome {} {}".format(name, surname),
                                  ["Submit assignment", "View grades", "Change your password"], "Exit")
        option = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]

        if option == "1":
            submit_assignment_controller.start_controller("student", assignments, idx)
        elif option == "2":
            view_grades(idx)
        elif option == "3":
            codecooler_controller.change_password(idx)

    save_assignments(assignments)
    save_students_data()


def view_grades(idx):
    """
    Read grades from csv file. Allow student to see his/her grades
    """

    students_grades = []
    all_grades = DataManager.read_file("csv/grades.csv")

    for grade in all_grades:
        if idx in grade[0]:
            students_grades.append(grade)

    if len(students_grades) > 0:
        titles = ["Students idx", "Assignment", "Grade"]
        codecooler_view.print_table(titles, students_grades)

    else:
        codecooler_view.print_result("There is no grades!")
        option = codecooler_view.get_inputs("Enter anything to exit", [""])


def read_assignments(return_type):
    """
    Convert data from csv file to SubmitAssignment object and add it to list

    Args:
        return_type (string): indicate whta type return will be
    """
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


def save_assignments(assignments):
    """
    Allow save submitted assigement to csv file
    """
    for i in range(len(assignments)):
        assignments[i] = [assignments[i].idx, assignments[i].link,
                          assignments[i].name, assignments[i].date]

    DataManager.save_file("csv/submitted_assgn.csv", assignments)


def remove_student():
    """
    Remove Student object from student_list
    """

    instances_manager.remove_person(Student.student_list)


def add_student():
    """
    Create Student object and add to student_list
    """

    title = 'Creating student'
    instances_manager.add_person(Student.student_list, Student, title)

def change_student_name():
    """
    Change student name
    """

    title = 'Modify name'
    task = ['Provide new name']
    instances_manager.modify_person_details(Student.student_list, 'name', title, task)


def change_student_password():
    """
    Change student password
    """

    title = 'Modify password'
    task = ['Provide new password']
    instances_manager.modify_person_details(Student.student_list, 'password', title, task)


def change_student_surname():
    """
    Change student surname
    """

    title = 'Modify surname'
    task = ['Provide new surname']
    instances_manager.modify_person_details(Student.student_list, 'surname', title, task)


def change_student_email():
    """
    Change student email
    """

    title = 'Modify email'
    task = ['Email']
    instances_manager.modify_person_details(Student.student_list, 'email', title, task)


def load_students(data):
    Student.student_list = instances_manager.convert_data_to_object('student', data)


def save_students_data():
    data = instances_manager.prepare_data_to_visualize(Student.student_list)
    DataManager.save_file('csv/students.csv', data)
