from Models.student import Student
from View.employee_view import EmployeeView


class EmployeeController():
    ''' Class with controll methods for all employeers'''

    @staticmethod
    def get_student_list():
        """
        Method for get student list from Student model

        Returns:
            :obj: list of :obj: `Student`: list off students
        """
        return Student.student_list

    @staticmethod
    def check_given_email(email):
        if "@" in email and "." in email:
            is_correct = True
        else:
            is_correct = False

        while not is_correct:
            email = EmployeeView.single_input("Please provide correct email: ")
            if "@" in email and "." in email:
                is_correct = True

        return email

    @staticmethod
    def check_given_grade(grade):
        is_correct = EmployeeController.try_str_convert(grade)

        while not is_correct:
            grade = EmployeeView.single_input("Please provide grade from 1 to 100: ")
            is_correct = EmployeeController.try_str_convert(grade)

        return grade

    @staticmethod
    def try_str_convert(mssg):
        try:
            if int(mssg) > 0 and int(mssg) < 101:
                is_correct = True
            else:
                is_correct = False
        except ValueError:
            is_correct = False

        return is_correct
