from Models.attendance import AttendanceModel
from View.codecooler_view import CodecoolerView

class AttendanceController:

    def start_controller(self, students):
        student_detail = CodecoolerView.get_inputs("Check attendance", ["Student idx", "Attendance state"])
        attendance = AttendanceModel(student_detail[0], student_detail[1])

        for student in students:
            if student.idx == student_idx:
                student.attendance_list.append(attendance)
                attendance_procent = self.calculate_attendnace(student)
                print(attendance_procent)

    @staticmethod
    def calculate_attendnace(student):
        attendance_sum = 0
        for index in range(len(attendance_list)):
            attendance_sum += attendance_list[index].state

        return attendance_sum/len(attendance_list)
