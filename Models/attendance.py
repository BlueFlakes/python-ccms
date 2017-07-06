from datetime import date


class AttendanceModel:

    def __init__(self, student_idx, state):
        self.date = date.today()
        self.student_idx = student_idx
        self.state = state
