class AttendanceModel:
    """This class represents attendance of students on lessons"""

    def __init__(self, student_idx, date, state):
        """
        Constructor of attendance object.

        Args:
            student_idx (string): uniqe student id
            date (:obj: `datetime.date`): date of cheak attendance
            state (int): status of student attendane

        Exmaples:
            There are three states for attendance: 0 - not present, 0.5 - late
            and 1 - present

        """
        self.student_idx = student_idx
        self.date = date
        self.state = state
