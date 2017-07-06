from View.codecooler_view import CodecoolerView


class EmployeeView(CodecoolerView):
    def print_student_list(students):
        for student in students:
            print("{}, {}, {}".format(student.idex, student.name, student.surname))
