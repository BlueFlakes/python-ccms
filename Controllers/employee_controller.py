from Models.student import Student
from codecooler_controller import CodecoolerController


class EmployeeController(CodecoolerController):
    ''' Class with controll methods for all employeers'''

    @staticmethod
    def get_student_list():
        """
        Method for get student list from Student model

        Returns:
            :obj: list of :obj: `Student`: list off students
        """

        return Student.student_list


    view_studen(get_student_list)
