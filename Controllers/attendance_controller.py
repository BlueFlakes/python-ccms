from Models.attendance import AttendanceModel
from View.codecooler_view import CodecoolerView
from datetime import date


class AttendanceController:
    """Contain methods to work on AttendanceModel object"""

    def start_controller(students):
        """
        Contain main logic for AttendanceController.

        Args:
            students (list of :obj: `StudentModels`):list with detail of all students
        """
        students_attendance = self.create_students_attendance_list()
        option = 0
        while not option == "0":
            os.system("clear")

            CodecoolerView.print_menu("Welcome {} {}".format(name, surname),
                                      ["Check attendnace", "View student attendance"], "Exit")
            options = CodecoolerView.get_inputs("Please choose a number", ["Number"])
            option = options[0]

            if option == "1":
                self.check_attendance(students_attendance, students)
            elif option == "2":
                choosen_student = CodecoolerView.get_inputs("Student attendance detail", ["Student idx"])
                attendance_student_list = get_attendnace_list(students_attendance, choosen_student)
                # here we need add print table
                self.calculate_attendnace(students_attendance, choosen_student[0])

        DataManager.save_file("csv/attendance.csv", students_attendance)

    @staticmethod
    def calculate_attendnace(students_attendance, student_idx):
        """
        Print attendnace for student with given idx in percent

        Args:
            students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
            student_idx (str): uniqe id number of student
        """
        attendance_sum = 0
        for attendance in students_attendance:
            if attendance.student_idx == student_idx:
                attendance_sum += int(attendance.state)

            try:
                attendance_procent = round((attendance_sum/len(attendance_list)*100), 2)
            except ZeroDivisionError:
                print("This student have no attendance")
                pass
            else:
                print("Student attendance {}%".format(attendance_procent))

    def check_attendance(self, students_attendance, students):
        """
        Add AttendanceModel object to proper list.

        Args:
            students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
            students (list of :obj: `StudentModels`):list with detail of all students
        """
        date = datetime.date.today()
        for student in students:
            question = "Check attendance for {} {}".format(student.name, student.surname)
            student_detail = CodecoolerView.get_inputs("{}".format(question), ["Attendance state"])

            attendance = AttendanceModel(student.idx, date, student_detail[2])
            students_attendance.append(attendance)

    @staticmethod
    def get_attendnace_list(students_attendance, student_idx):
        """
        Create list of attendnace detail for student with given idx

        Args:
            students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
            student_idx (str): uniqe id number of student

        Returns:
            list of list: str: list of attendnace detail for student with given idx 
        """
        attendance_student_list = []

        for attendance in students_attendance:
            if attendance.student_idx == student_idx:
                attendance_student_list.append(attendance)

        return attendance_student_list

    @staticmethod
    def create_students_attendance_list():
        """
        Convert data from csv file to AttendanceModel object and add it to list
        """
        students_attendance = []
        attendance_list = DataManager.read_file("csv/attendance.csv")
        for attendance_detail in attendance_list:
            attendnace = AttendanceModel(attendance_detail[0], attendance_detail[1], attendance_detail[2])
            students_attendance.append(attendnace)

        return students_attendance
