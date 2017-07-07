from View.codecooler_view import CodecoolerView
from Models.assignment import Assignment
from data_manager import DataManager


class AssignmentController:
    """Contain methods to work on Attendance object"""

    @classmethod
    def start_controller(cls):
        """Contain main logic for AttendanceController. Ask user about assigemnt details"""
        assgn = CodecoolerView.get_inputs("Add assignment", ["Title", "Description"])
        Assignment.assignments.append(Assignment(assgn[0], assgn[1]))

        cls.save_assignment(assgn)

    @staticmethod
    def save_assignment(assgn):
        """Save list of assignments in csv file"""
        DataManager.extend_file("csv/assignments.csv", assgn)
