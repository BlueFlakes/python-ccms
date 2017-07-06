from Models.attendance import AttendanceModel
from View.codecooler_view import CodecoolerView


class AttendanceController:

    def start_controller(students):
        students_attendance = DataManager.read_file("csv/attendance.csv")
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
                attendance_student_list = get_attendnace_list(students_attendance)      # here we need add print table
                self.calculate_attendnace(students_attendance, choosen_student[0])

        DataManager.save_file("csv/attendance.csv", students_attendance)

    @staticmethod
    def calculate_attendnace(students_attendance, student_idx):
        attendance_sum = 0
        for attendance in students_attendance:
            if attendance[0] == student_idx:
                attendance_sum += attendance[1]

            try:
                attendance_procent = round((attendance_sum/len(attendance_list)*100), 2)
            except ZeroDivisionError:
                print("This student have no attendance")
                pass
            else:
                print("Student attendance {}%".format(attendance_procent))

    def check_attendance(self, students_attendance, students):
            for student in students:
                question = "Check attendance for {} {}".format(student.name, student.surname)
                student_detail = CodecoolerView.get_inputs("{}".format(question), ["Attendance state"])

                attendance = AttendanceModel(student[0], student_detail[1])
                students_attendance.append(attendance)

    @staticmethod
    def get_attendnace_list(students_attendance):
        attendance_student_list = []

        for attendance in students_attendance:
            if attendance[0] == student_idx:
                attendance_student_list.append(attendance)

        return attendance_student_list
