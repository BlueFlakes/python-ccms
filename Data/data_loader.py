from Models.submit_assignment import SubmitAssignment
from Models.assignment import Assignment
from Models.student import Student
from Models.mentor import Mentor
from Models.manager import Manager
from Models.office_manager import OfficeManager
from Models.grade import Grade
from Models.attendance import AttendanceModel
from Models.talkbox import TalkBox


def load_data_from_files():
    """
    Load data from all csv files as call of proper methods for classes
    """

    SubmitAssignment.load_submit_assignments()
    Assignment.load_assignments()
    Student.load_students()
    Mentor.load_mentors()
    Manager.load_managers()
    OfficeManager.load_office_managers()
    Grade.load_grades()
    AttendanceModel.load_attendance()
    TalkBox.load_talkbox()


def save_data_to_files():
    """
    Save data from all csv files as call of proper methods for classes
    """

    OfficeManager.save_office_managers()
    Student.save_students()
    Mentor.save_mentors()
    Manager.save_managers()
    Assignment.save_assignments()
    SubmitAssignment.save_submit_assignments()
    Grade.save_grades()
    AttendanceModel.save_attendance()
    TalkBox.save_talkbox()
