

class AttendanceController:

    def start_controller(self):
        attendance = AttendanceModel(student_idx)
        self.set_attendance_state(attendance)

        for student in students:
            if student.idx == student_idx:
                attendance_list.append(attendance)


    @staticmethod
    def set_attendance_state(attendance):
        state = get_state()
        attendance.state = state
