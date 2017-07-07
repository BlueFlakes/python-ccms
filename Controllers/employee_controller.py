from Models.student import Student


class EmployeeController():
    '''Class with controll methods for all employeers'''

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
        """
        Check if user email is vaidate
        """

        if "@" in email and "." in email:
            is_correct = True
        else:
            is_correct = False

        while not is_correct:
            email = input("Please provide correct email: ")
            if "@" in email and "." in email:
                is_correct = True

        return email
