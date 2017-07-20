from Data import tools
from datetime import datetime


class AttendanceModel:
    """
    This class represents attendance of students on lessons

    Attributes:
        staff_attendance (list of :obj: `AttendanceModel`): list of created attendances
        _file_name (string): name of file to open
    """

    staff_attendance = []
    _file_name = "csv/attendance.csv"

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
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.state = state

    @classmethod
    def get_attendance_list(cls):
        """
        Returns:
            staff_attendance (list of :obj: `AttendanceModel`): list of all attendances
        """

        return cls.staff_attendance

    @classmethod
    def load_attendance(cls):
        """
        Call function to open csv file and convert it rows to AttendanceModel objects
        """

        cls.staff_attendance = tools.get_data_from_file(cls._file_name, AttendanceModel)

    @classmethod
    def get_records_from_objects(cls):
        """
        Get specified attributes from object

        Returns:
            list of lists: list with attributes of all Attendance objects
        """

        temp = []

        for task in cls.staff_attendance:
            temp.append([task.student_idx, task.date, task.state])

        return temp

    @classmethod
    def save_attendance(cls):
        """
        Call functions to save AttendanceModel to csv file
        """

        attendance_data_records = cls.get_records_from_objects()
        tools.save_data_to_file(cls._file_name, attendance_data_records)
