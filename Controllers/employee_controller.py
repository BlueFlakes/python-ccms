from Models.student import Student
from View import employee_view


def get_student_list():
    """
    Method for get student list from Student model

    Returns:
        :obj: list of :obj: `Student`: list off students
    """
    return Student.student_list
