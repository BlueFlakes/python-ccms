from Models.attendance import AttendanceModel
from View.codecooler_view import CodecoolerView


class AttendanceController:

    def start_controller(students):
        option = 0
        while not option == "0":
            os.system("clear")

            CodecoolerView.print_menu("Welcome {} {}".format(name, surname),
                                      ["Check attendnace", "View student attendance"], "Exit")
            options = CodecoolerView.get_inputs("Please choose a number", ["Number"])
            option = options[0]

            if option == "1":
                self.check_attendance(students)
            elif option == "2":
                pass


    @staticmethod
    def calculate_attendnace(students_attendance, student_idx):
        attendance_sum = 0
        for attendance in students_attendance:
            if attendance[0] == student_idx:
                attendance_sum += attendance[1]

            return round((attendance_sum/len(attendance_list)*100), 2)

    def check_attendance(self, students):
            for student in students:
                student_detail = CodecoolerView.get_inputs("Check attendance", ["Attendance state"])
                attendance = AttendanceModel(student[0], student_detail[1])

                students_attendance = DataManager.read_file("csv/attendance.csv")

                students_attendance.append(attendance)

                attendance_procent = self.calculate_attendnace(students_attendance, student[0])
                print("Student attendance {}%".format(attendance_procent))

                DataManager.save_file("csv/attendance.csv", students)

    @staticmethod
    def get_attendnace_list():
        attendance_list = []
        choosen_student = CodecoolerView.get_inputs("Student idx", ["Student idx"])

        for attendance in students_attendance:
            if attendance[0] == student_idx:
                attendance_list.append(attendance)

