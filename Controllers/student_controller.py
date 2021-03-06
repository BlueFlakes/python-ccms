from Models.student import Student
from Models.codecooler import Codecooler
from Models.submit_assignment import SubmitAssignment
from Controllers import submit_assignment_controller, instances_manager, codecooler_controller, talkbox
from Controllers import assignment_controller
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
        codecooler_view.clear_window()
        codecooler_view.print_menu("Welcome {} {}".format(name, surname),
                                   ["Submit assignment", "View grades", "Students ranking",
                                   "Change your password", "Enter talkbox", "Debt calculator"], "Exit")
        user_choice = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]
        codecooler_view.clear_window()

        if user_choice == "1":
            submit_assignment_controller.start_controller("student", idx)

        elif user_choice == "2":
            view_grades(idx)

        elif user_choice == "3":
            rank = get_ranking()
            codecooler_view.print_table(["Name", "Total points"], rank)
            codecooler_view.state_locker()
            codecooler_view.clear_window()

        elif user_choice == "4":
            codecooler_controller.change_password(idx)

        elif user_choice == "5":
            talkbox.start_talkbox(name, surname)

        elif user_choice == "6":
            show_debt(idx)


def view_grades(idx):
    """
    Allow student to see assigments grades

    Args:
        idx (string): unique user's id
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


def show_debt(idx):
    """
    Call functions to display student's debet

    Args:
        idx (string): unique user's id
    """

    debt = calculate_debt(idx)
    codecooler_view.print_result("If you will leave us now, your debt will be ~{} PLN.\n".format(debt))
    codecooler_view.state_locker()


def calculate_debt(idx):
    """
    Based on current date and date of student's course start calculate student's debet.

    Args:
        idx (string): unique user's id

    Returns:
        int: student's debet
    """

    today = date.today()
    start_date = get_start_date(idx)

    delta = today - start_date

    return (delta.days * 41)


def get_start_date(idx):
    """
    Get course start date of student with given idx

    Args:
        idx (string): unique user's id

    Returns:
        :obj: `date`: student's course start date
    """

    start_date = date.today()
    for person in Student.student_list:
        if person.idx == idx:
            start_date = start_date.replace(day=int(person.registration_date[0:2]))
            start_date = start_date.replace(month=int(person.registration_date[3:5]))
            start_date = start_date.replace(year=int(person.registration_date[6:10]))

    return start_date


def get_ranking():
    """
    Create students ranking with descending order as dictionary.
    Key is student's name and surname, value is student summary grade.

    Returns:
        dict: ranking of students by grades
    """

    students_rank = {}

    for person in Student.student_list:
        grades = get_grades(person)
        info = person.name + " " + person.surname
        students_rank[info] = grades

    rank = sorted(students_rank.items(), key=lambda grades: grades[1], reverse=True)

    return rank


def get_grades(person):
    """
    Count sum of student's grades

    Args:
        person (:obj: `Student`): object representing student

    Returns:
        string: sum of student grade as string
    """

    grades_sum = 0

    for grd in Grade.grades_list:
        if grd.idx == person.idx:
            grades_sum += int(grd.grade)

    return str(grades_sum)
