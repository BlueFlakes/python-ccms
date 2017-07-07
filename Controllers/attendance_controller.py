from Models.attendance import AttendanceModel
from View.codecooler_view import CodecoolerView
from datetime import date

from Models.student import Student
import os
from data_manager import DataManager


class AttendanceController:
    """Contain methods to work on AttendanceModel object"""

    @classmethod
    def start_controller(cls):
        """
        Contain main logic for AttendanceController.
        """
        students = Student.student_list
        students_attendance = cls.create_students_attendance_list()
        option = 0
        while not option == "0":
            # os.system("clear")

            CodecoolerView.print_menu("", ["Check attendnace", "View student attendance"], "Exit")
            options = CodecoolerView.get_inputs("Please choose a number", ["Number"])
            option = options[0]

            if option == "1":
                cls.check_attendance(students_attendance, students)
            elif option == "2":
                choosen_student = CodecoolerView.get_inputs("Student attendance detail", ["Student idx"])
                attendance_student_list = cls.get_attendnace_list(students_attendance, choosen_student[0])
                # here we need add print table
                cls.calculate_attendnace(students_attendance, choosen_student[0])

        cls.save_attendance(students_attendance)

    @staticmethod
    def calculate_attendnace(students_attendance, student_idx):
        """
        Print attendnace for student with given idx in percent

        Args:
            students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
            student_idx (str): uniqe id number of student
        """
        attendance_sum = 0
        for attendance in students_attendance:
            if attendance.student_idx == student_idx:
                attendance_sum += float(attendance.state)

        try:
            attendance_procent = round((attendance_sum/len(students_attendance)*100), 2)
        except ZeroDivisionError:
            print("This student have no attendance")
            pass
        else:
            print("Student attendance {}%".format(attendance_procent))

    @classmethod
    def check_attendance(cls, students_attendance, students):
        """
        Add AttendanceModel object to proper list.

        Args:
            students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
            students (list of :obj: `StudentModels`):list with detail of all students
        """
        current_date = date.today()
        for student in students:
            question = "Check attendance for {} {}".format(student.name, student.surname)
            student_detail = CodecoolerView.get_inputs(question, ["Attendance state"])

            attendance = AttendanceModel(student.idx, current_date, student_detail[0])
            students_attendance.append(attendance)

    @staticmethod
    def get_attendnace_list(students_attendance, student_idx):
        """
        Create list of attendnace detail for student with given idx

        Args:
            students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
            student_idx (str): uniqe id number of student

        Returns:
            list of list: str: list of attendnace detail for student with given idx
        """
        attendance_student_list = []
        for attendance in students_attendance:
            if attendance.student_idx == student_idx:
                attendance_student_list.append(attendance)

        return attendance_student_list

    @staticmethod
    def create_students_attendance_list():
        """
        Convert data from csv file to AttendanceModel object and add it to list
        """
        students_attendance = []
        attendance_list = DataManager.read_file("csv/attendance.csv")
        for attendance_detail in attendance_list:
            attendnace = AttendanceModel(attendance_detail[0], attendance_detail[1], attendance_detail[2])
            students_attendance.append(attendnace)

        return students_attendance


    @staticmethod
    def save_attendance(students_attendance):
        """
        Save list of attendance of all students in csv file

        Args:
            students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
        """
        for i in range(len(students_attendance)):
            students_attendance[i] = [students_attendance[i].student_idx, students_attendance[i].date,
                                      students_attendance[i].state]

        DataManager.save_file("csv/attendance.csv", students_attendance)
