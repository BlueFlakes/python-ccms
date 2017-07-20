from Models.student import Student
from Models.codecooler import Codecooler
from Models.submit_assignment import SubmitAssignment
from Controllers import submit_assignment_controller, instances_manager, codecooler_controller, talkbox
from View import codecooler_view
from data_manager import DataManager
from time import sleep
from datetime import date
from Models.grade import Grade

def start_controller(name, surname, idx):
    """
    Allow student user perform assign tasks.
    Call functions to print menu for user and get input of choosen user_choice

    Args:
        name (string): name of user
        surname (string): surname of user
        idx (string): unique user's id
    """
    user_choice = None

    while user_choice != "0":

        codecooler_view.print_menu("Welcome {} {}".format(name, surname),
                                  ["Submit assignment", "View grades", "Change your password",
                                   "Enter talkbox", "Debt calculator"], "Exit")
        user_choice = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]

        if user_choice == "1":
            submit_assignment_controller.start_controller("student", idx)

        elif user_choice == "2":
            view_grades(idx)

        elif user_choice == "3":
            codecooler_controller.change_password(idx)

        elif user_choice == "4":
            talkbox.start_talkbox(name, surname)

        elif user_choice == "5":
            calculate_debt(idx)


def view_grades(idx):
    """
    Read grades from csv file. Allow student to see his/her grades
    """

    students_grades = []
    all_grades = Grade.get_grades_list()

    for grade in all_grades:
        if idx == grade.idx and grade.grade != 0:
            students_grades.append([grade.idx, grade.title, str(grade.grade)])

    if len(students_grades) > 0:
        titles = ["Students idx", "Assignment", "Grade"]
        codecooler_view.print_table(titles, students_grades)
        codecooler_view.state_locker()

    else:
        codecooler_view.print_result("There is no grades!")
        sleep(1.5)


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

def calculate_debt(idx):
    today = date.today()
    start_date = date.today()
