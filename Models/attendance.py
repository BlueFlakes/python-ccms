from datetime import date


class AttendanceModel:

    def __init__(self, student_idx, state):
        self.student_idx = student_idx
        self.date = date.today()
        self.state = state
