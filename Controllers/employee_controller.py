from Models.student import Student
from View.employee_view import EmployeeView


def get_student_list():
    """
    Method for get student list from Student model

    Returns:
        :obj: list of :obj: `Student`: list off students
    """
    return Student.student_list


def check_given_email(email):
    """
    Check if given email is vaidate

    Args:
        email (string): givven email

    Returns:
        string: validate email given by user
    """

    if "@" in email and "." in email:
        is_correct = True
    else:
        is_correct = False

    while not is_correct:
        email = EmployeeView.single_input("Please provide correct email: ")
        if "@" in email and "." in email:
            is_correct = True

    return email


def check_given_grade(grade):
    is_correct = EmployeeController.try_str_convert(grade)

    while not is_correct:
        grade = EmployeeView.single_input("Please provide grade from 1 to 100: ")
        is_correct = EmployeeController.try_str_convert(grade)

    return grade


def try_str_convert(mssg):
    try:
        if int(mssg) > 0 and int(mssg) < 101:
            is_correct = True
        else:
            is_correct = False
    except ValueError:
        is_correct = False

    return is_correct
