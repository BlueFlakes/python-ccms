from Models.student import Student
from View import employee_view


def get_student_list():
    """
    Method for get student list from Student model

    Returns:
        :obj: list of :obj: `Student`: list off students
    """
    return Student.student_list


def check_given_grade(grade):
    is_correct = try_str_convert(grade)

    while not is_correct:
        grade = employee_view.single_input("Please provide grade from 1 to 100: ")
        is_correct = try_str_convert(grade)

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
