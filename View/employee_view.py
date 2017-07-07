
class EmployeeView:
    """This class contains logic for prints of student list"""

    def print_student_list(students):
        """
        Prints list of students

        Args:
            students (list of :obj: `Student`): list with all students
        """

        for student in students:
            print("{}, {}, {}".format(student.idex, student.name, student.surname))

    @staticmethod
    def single_input(mssg):
        return input(mssg)
