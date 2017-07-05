from Models.student import Student
from codecooler_controller import CodecoolerController


class EmployeerCotroller(CodecoolerController):
    ''' Class with controll methods for all employeers'''

    def get_student_list(self):
        """
        Method for get student list from Student model

        Returns:
            :obj: list of :obj: `Student`: list off students
        """

        student_list = Student.student_list

        return student_list
